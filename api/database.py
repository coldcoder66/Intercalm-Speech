from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User
import os

class DatabaseManager:
    def __init__(self):
        # SQL Server connection string for Windows Authentication
        server = os.getenv('SQL_SERVER', 'localhost')  # Default to localhost
        database = os.getenv('SQL_DATABASE', 'intercalmdev')  # Updated database name
        connection_string_params = os.getenv('SQL_CONNECTION_STRING_PARAMS', 'driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes') # Additional connection string parameters
        
        # Create connection string for Windows Authentication
        connection_string = f"mssql+pyodbc://{server}/{database}?{connection_string_params}"
        
        # Create engine
        self.engine = create_engine(
            connection_string,
            echo=True,  # Set to False in production
            pool_pre_ping=True,
            pool_recycle=300
        )
        
# Create global database manager instance
db_manager = DatabaseManager()

# Factory to construct new database sessions
Session = sessionmaker(autocommit=False, autoflush=False, bind=db_manager.engine)