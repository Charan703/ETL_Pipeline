# 🚀 NASA APOD ETL Pipeline

> **Extract, Transform, Load pipeline for NASA's Astronomy Picture of the Day using Apache Airflow and PostgreSQL**

## 📋 Overview

This project implements an automated ETL pipeline that:
- 🌌 Extracts daily astronomy pictures from NASA's APOD API
- 🔄 Transforms the data for storage optimization
- 💾 Loads processed data into PostgreSQL database
- 📊 Enables analytics and reporting on astronomical content

## 🏗️ Project Structure

```
ETL_pipeline/
├── 📁 dags/              # Airflow DAG definitions
│   └── ETL.py           # Main ETL workflow
├── 📁 sql/              # Database schema scripts
├── 📁 config/           # Configuration files
├── 📁 scripts/          # Utility scripts
├── 📄 requirements.txt  # Python dependencies
├── 🐳 Dockerfile        # Container configuration
└── 🐳 docker-compose.yml # Multi-container setup
```

## 🛠️ Technology Stack

- **🌊 Apache Airflow**: Workflow orchestration
- **🚀 Astronomer CLI**: Pipeline deployment and management
- **☁️ AWS RDS PostgreSQL**: Cloud database storage
- **🐍 Python**: Data processing
- **🐳 Docker**: Containerization
- **🔗 NASA API**: Data source
- **👁️ DBeaver**: Database visualization and management

## ⚙️ Setup Instructions

### 1. 🚀 Start the Environment with Astronomer CLI
```bash
# Initialize Astronomer project
astro dev init

# Start local Airflow environment
astro dev start
```

### 2. ☁️ AWS RDS Setup
- Create PostgreSQL instance on AWS RDS
- Configure security groups for access
- Note down connection details (endpoint, port, database name)

### 3. 🌐 Access Services
- **Airflow UI**: http://localhost:8080
- **AWS RDS PostgreSQL**: Your RDS endpoint:5432
- **DBeaver**: Connect using RDS credentials

### 4. 🔧 Configure Database Connection
Create a new connection in Airflow UI:
- **Connection ID**: `postgres_connection`
- **Connection Type**: Postgres
- **Host**: Your AWS RDS endpoint
- **Schema**: Your database name
- **Port**: `5432`
- **Login**: Your RDS username
- **Password**: Your RDS password

## 🎯 Pipeline Features

### 📥 Data Extraction
- 🌟 NASA APOD API integration
- 🔄 Daily automated data retrieval
- 🛡️ Error handling and retry logic

### 🔄 Data Transformation
- 📝 Data cleaning and validation
- 🎯 Field selection and formatting
- 📊 Data quality checks

### 📤 Data Loading
- ⚡ Efficient bulk loading
- 🔒 Transaction safety
- 📈 Performance optimization

### 📊 Monitoring & Logging
- 📋 Pipeline status tracking
- 🚨 Error alerting
- 📝 Comprehensive logging

## 🚀 Deployment

### 🌟 Local Development
```bash
# Start local development environment
astro dev start

# View logs
astro dev logs

# Stop environment
astro dev stop
```

### ☁️ Production Deployment with Astronomer
```bash
# Deploy to Astronomer Cloud
astro deploy

# Check deployment status
astro deployment list
```

### 👁️ Data Visualization with DBeaver
1. **Install DBeaver**: Download from https://dbeaver.io/
2. **Connect to AWS RDS**:
   - Host: Your RDS endpoint
   - Port: 5432
   - Database: Your database name
   - Username/Password: Your RDS credentials
3. **View Data**: Browse `nasa_apod` table and run queries

## 🚀 Usage

1. **📂 Setup Data Sources**: Configure NASA API access
2. **⚙️ Configure Connections**: Set up database connections in Airflow
3. **▶️ Run Pipeline**: Execute the `nasa_apod_postgres` DAG
4. **📊 Monitor Results**: Check Airflow UI and PostgreSQL for data

## 📊 Database Schema

The pipeline creates a `nasa_apod` table with:
- 🆔 `id`: Primary key
- 📝 `title`: Picture title
- 📖 `explanation`: Detailed description
- 🔗 `url`: Image URL
- 📅 `date`: Publication date
- 🎬 `media_type`: Content type (image/video)

## 🔧 Troubleshooting

### Common Issues:
- 🐘 **AWS RDS Connection**: Ensure security groups allow inbound connections
- 🚀 **Astronomer CLI**: Verify CLI installation and authentication
- 🔑 **API Access**: Verify NASA API key configuration
- 📁 **File Permissions**: Check Docker volume permissions
- 🌐 **Network**: Confirm VPC and subnet configurations
- 👁️ **DBeaver Connection**: Verify RDS endpoint and credentials

### 📝 Logs Location:
- Airflow logs: Available in Airflow UI or `astro dev logs`
- Astronomer deployment logs: `astro deployment logs`
- Container logs: `docker-compose logs`

## 🤝 Contributing

1. 🍴 Fork the repository
2. 🌿 Create a feature branch
3. 💻 Make your changes
4. 🧪 Test thoroughly
5. 📤 Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

---

**🌟 Happy Data Engineering! 🌟**