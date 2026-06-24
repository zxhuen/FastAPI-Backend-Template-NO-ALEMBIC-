# Import BaseSettings from Pydantic.
# BaseSettings automatically reads values from environment variables (.env file).
from pydantic_settings import BaseSettings


# Create a Settings class that will hold all of our application configuration.
# It inherits from BaseSettings so it knows how to load environment variables.
class Settings(BaseSettings):

    # Expected environment variable:
    # SUPABASE_URL=https://your-project.supabase.co
    # This will be stored as a string.
    SUPABASE_URL: str

    # Expected environment variable:
    # SUPABASE_KEY=your-secret-key
    # This is your Supabase API key.
    SUPABASE_KEY: str

    # Expected environment variable:
    # DATABASE_URL=postgresql://...
    # SQLAlchemy will use this to connect to the PostgreSQL database.
    DATABASE_URL: str


    # Configuration for the BaseSettings class.
    class Config:

        # Tell Pydantic to look for environment variables inside a file
        # named ".env" located in the project root.
        env_file = ".env"


# Create one instance of the Settings class.
# As soon as this line runs:
# 1. It opens the .env file.
# 2. Reads SUPABASE_URL, SUPABASE_KEY, and DATABASE_URL.
# 3. Stores them inside this object.
#
# Now you can access them anywhere like:
# settings.SUPABASE_URL
# settings.SUPABASE_KEY
# settings.DATABASE_URL
settings = Settings()