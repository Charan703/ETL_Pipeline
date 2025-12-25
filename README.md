ETL Pipeline Project
===================

This project implements an ETL (Extract, Transform, Load) pipeline using Apache Airflow and PostgreSQL for data processing and storage.

Overview
========

The ETL pipeline extracts data from various sources, transforms it according to business requirements, and loads it into a PostgreSQL database for analytics and reporting.

Project Structure
================

- **dags/**: Contains Airflow DAG definitions for ETL workflows
- **sql/**: SQL scripts for database schema creation and data transformations
- **config/**: Configuration files for database connections and pipeline settings
- **scripts/**: Utility scripts for data processing and validation
- **requirements.txt**: Python dependencies including PostgreSQL drivers
- **Dockerfile**: Container configuration with PostgreSQL client tools

Database Configuration
=====================

**PostgreSQL Connection Details:**
- Host: localhost
- Port: 5432
- Database: postgres
- Username: postgres
- Password: postgres

**Required Python Packages:**
```
psycopg2-binary
pandas
sqlalchemy
```

Setup Instructions
=================

1. **Start the Environment:**
   ```bash
   astro dev start
   ```

2. **Access Services:**
   - Airflow UI: http://localhost:8080
   - PostgreSQL: localhost:5432

3. **Configure Database Connection:**
   - Connection ID: postgres_default
   - Connection Type: Postgres
   - Host: postgres
   - Schema: postgres
   - Login: postgres
   - Password: postgres
   - Port: 5432

ETL Pipeline Features
====================

- **Data Extraction**: Support for multiple data sources (CSV, JSON, APIs)
- **Data Transformation**: Cleaning, validation, and business logic application
- **Data Loading**: Efficient bulk loading into PostgreSQL tables
- **Error Handling**: Comprehensive logging and error recovery
- **Monitoring**: Pipeline status tracking and alerting

Usage
=====

1. Place source data files in the `include/data/` directory
2. Configure connection parameters in `airflow_settings.yaml`
3. Run ETL DAGs from the Airflow UI
4. Monitor pipeline execution and check PostgreSQL for loaded data

Troubleshooting
==============

- Ensure PostgreSQL container is running before starting DAGs
- Check connection settings if database errors occur
- Verify data file formats match pipeline expectations
- Review Airflow logs for detailed error information
