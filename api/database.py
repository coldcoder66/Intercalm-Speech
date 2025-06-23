from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.config import Config

# Load config from environment variables or .env file
config = Config('.env')

# SQL Server connection string for Windows Authentication
server = config('SQL_SERVER', default='localhost')  # Default to localhost
database = config('SQL_DATABASE', default='intercalmdev')  # Updated database name
connection_string_params = config('SQL_CONNECTION_STRING_PARAMS', default='driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes') # Additional connection string parameters
echo = config('SQL_ECHO', default='False', cast=bool) #Echos SQL statements in console if set to True

# Create connection string for Windows Authentication
connection_string = f"mssql+pyodbc://{server}/{database}?{connection_string_params}"

# Create engine
engine = create_engine(
    connection_string,
    echo=echo,
    pool_pre_ping=True,
    pool_recycle=300
)

# Factory to construct new database sessions
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)