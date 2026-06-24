# Import create_engine.
# This creates the connection between SQLAlchemy and your database.
from sqlalchemy import create_engine

# Import sessionmaker and declarative_base.
# sessionmaker -> creates database sessions.
# declarative_base -> creates the base class that all database models inherit from.
from sqlalchemy.orm import sessionmaker, declarative_base

# Import our settings object that contains DATABASE_URL from the .env file.
from app.core.config import settings


# Create the database engine.
# The engine is SQLAlchemy's connection manager.
# It knows HOW to connect to your PostgreSQL (Supabase) database.
#
# settings.DATABASE_URL comes from:
# DATABASE_URL=postgresql://...
#
# echo=True prints every SQL query to the terminal.
# This is useful while learning and debugging.
# In production, this is usually set to False.
engine = create_engine(settings.DATABASE_URL, echo=True)


# Create a Session factory.
#
# Think of SessionLocal as a "database session creator."
# Every time you call SessionLocal(), it creates a new session.
#
# autocommit=False
# -> You must manually call db.commit() to save changes.
#
# autoflush=False
# -> SQLAlchemy won't automatically send changes to the database
#    before every query.
#
# bind=engine
# -> Tells this session to use the engine (database connection)
#    we created above.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Create a Base class.
#
# Every SQLAlchemy model (table) will inherit from Base.
#
# Example:
#
# class User(Base):
#     __tablename__ = "users"
#
# Base keeps track of every model you create.
# Later, SQLAlchemy uses Base.metadata.create_all()
# to automatically create those tables.
Base = declarative_base()


# Dependency function for FastAPI.
#
# This creates a database session for every incoming request.
# FastAPI will automatically call this whenever a route needs
# database access.
def get_db():

    # Create a new database session.
    db = SessionLocal()

    try:

        # Give the session to the route.
        #
        # Example:
        #
        # def get_users(db: Session = Depends(get_db)):
        #     ...
        #
        # "yield" temporarily hands the session to the route.
        yield db

    finally:

        # After the request is finished (even if an error occurs),
        # always close the session.
        #
        # This prevents memory leaks and frees the database connection.
        db.close()