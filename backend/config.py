from dotenv import load_dotenv
import os
import redis
# Load environment variables from the .env file
load_dotenv()

class ApplicationConfig:
    # Retrieve the secret key from the environment, with a fallback for safety
    SECRET_KEY = os.environ.get("SECRET_KEY", "default_secret_key")
    
    # Disable track modifications to save resources
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Enable SQLAlchemy's echo mode for debugging SQL queries
    SQLALCHEMY_ECHO = True  # Corrected typo (was SQLALCHEMY_EHO)
    
    # Define the SQLite database URI
    SQLALCHEMY_DATABASE_URI = r"sqlite:///./db.sqlite"
    SESSION_TYPE ="redis"
    SESSION_PERMANENT= False
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.from_url("redis://127.0.0.1:6379")
