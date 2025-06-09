from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models import Base, User
import os
import urllib.parse

class DatabaseManager:
    def __init__(self):
        # SQL Server connection string for Windows Authentication
        server = os.getenv('SQL_SERVER', 'localhost')  # Default to localhost
        database = os.getenv('SQL_DATABASE', 'intercalmdev')  # Updated database name
        
        # Create connection string for Windows Authentication
        connection_string = f"mssql+pyodbc://{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
        
        # Create engine
        self.engine = create_engine(
            connection_string,
            echo=True,  # Set to False in production
            pool_pre_ping=True,
            pool_recycle=300
        )
        
        # Create session factory
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        
        # # Create tables
        # self.create_tables()
    
    # def create_tables(self):
    #     """Create all tables"""
    #     try:
    #         Base.metadata.create_all(bind=self.engine)
    #         print("✅ Database tables created successfully")
    #     except Exception as e:
    # #         print(f"❌ Error creating tables: {e}")
    
    def get_db_session(self):
        """Get database session"""
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()
    
    def test_connection(self):
        """Test database connection"""
        try:
            with self.engine.connect() as connection:
                result = connection.execute(text("SELECT 1"))
                return True
        except Exception as e:
            print(f"Database connection failed: {e}")
            return False
    
    def get_or_create_user(self, google_id: str, email: str, name: str, picture: str = None):
        """Get existing user or create new one"""
        db = next(self.get_db_session())
        try:
            # Try to find existing user
            user = db.query(User).filter(User.google_id == google_id).first()
            
            if user:
                # Update user info in case it changed
                user.email = email
                user.name = name
                user.picture = picture
                db.commit()
                return user
            else:
                # Create new user
                user = User(
                    google_id=google_id,
                    email=email,
                    name=name,
                    picture=picture
                )
                db.add(user)
                db.commit()
                db.refresh(user)
                return user
        except Exception as e:
            db.rollback()
            print(f"Error managing user: {e}")
            return None
        finally:
            db.close()

# Create global database manager instance
db_manager = DatabaseManager()

# Dependency to get database session
def get_db():
    """FastAPI dependency to get database session"""
    return next(db_manager.get_db_session())
