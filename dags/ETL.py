from airflow import DAG
from airflow.decorators import task
from airflow.providers.http.operators.http import HttpOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils import timezone
from datetime import timedelta
import json


with DAG(
    dag_id = 'nasa_apod_postgres',
    start_date=timezone.utcnow() - timedelta(days=1),
    schedule='@daily',
    catchup=False
) as dag:
    ## step 1: Create the table if it doesnt exits
    @task()
    def create_table():

        postgres_hook = PostgresHook(postgres_conn_id='postgres_connection')

        create_table_query = """
            CREATE TABLE IF NOT EXISTS nasa_apod (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            explanation TEXT,
            url TEXT,
            date DATE,
            media_type VARCHAR(50)
            );
        """

        postgres_hook.run(create_table_query)

    ## step 2: Extract the NASA API DATA (APOD) - Astronomy picture of the Day
    extract_apod = HttpOperator(
        task_id='extract_apod',
        method='GET',
        http_conn_id='nasa_api',
        endpoint='/planetary/apod',
        data={'api_key': "{{conn.nasa_api.extra_dejson.api_key}}"},
        response_filter=lambda response: json.loads(response.text),
        log_response=True
    )

    ## step 3: Transforming the data (Pick the information that i need to save)
    @task()
    def transform_apod_data(response):
        apod_data ={
            'title': response.get('title',''),
            'explanation': response.get('explanation', ''),
            'url': response.get('url', ''),
            'date': response.get('date', ''),
            'media_type': response.get('media_type', '')
        }
        return apod_data

    ## step 4: load the data into Postgres SQL
    @task()
    def load_data_to_postgres(apod_data):
        postgres_hook = PostgresHook(postgres_conn_id='postgres_connection')
        insert_query = """
            INSERT INTO nasa_apod (title, explanation, url, date, media_type)
            VALUES (%s, %s,%s, %s, %s);
        """
        postgres_hook.run(insert_query, parameters=(
            apod_data['title'],
            apod_data['explanation'],
            apod_data['url'],
            apod_data['date'],
            apod_data['media_type']
       
        ))

    ## step 5: verify the data DBViewer

    ## step 6: Define the task dependencies
    create_table() >> extract_apod
    api_response= extract_apod.output
    transform_data = transform_apod_data(extract_apod.output)
    load_data_to_postgres(transform_data)
