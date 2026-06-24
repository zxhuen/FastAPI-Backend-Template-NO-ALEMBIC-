# Import SQLAlchemy column types and helper functions.
#
# Column      -> Represents a column in a database table.
# Integer     -> Stores whole numbers.
# String      -> Stores text.
# DateTime    -> Stores date and time values.
# func        -> Gives access to SQL functions like NOW().
from sqlalchemy import Column, Integer, String, DateTime, func

# Import the Base class that all database models inherit from.
# Base keeps track of every model (table) in your project.
from app.core.database import Base


# Create a Post model.
# By inheriting from Base, SQLAlchemy knows this class represents
# a database table.
class Post(Base):

    # Name of the table in the database.
    #
    # If you run Base.metadata.create_all(),
    # SQLAlchemy will create a table called "posts".
    __tablename__ = "posts"


    # Primary key column.
    #
    # Integer -> Stores numbers.
    # primary_key=True -> Makes this the unique identifier.
    # index=True -> Creates a database index to speed up searches.
    #
    # Example:
    # id = 1
    # id = 2
    # id = 3
    id = Column(Integer, primary_key=True, index=True)


    # Title column.
    #
    # String -> Stores text.
    # nullable=False -> This field is required.
    # The database will reject rows without a title.
    title = Column(String, nullable=False)


    # Content column.
    #
    # Also required because nullable=False.
    content = Column(String, nullable=False)


    # Stores when the post was created.
    #
    # DateTime(timezone=True)
    # -> Stores both the date and time, including timezone information.
    #
    # server_default=func.now()
    # -> The DATABASE automatically inserts the current date/time
    #    when a new row is created.
    #
    # You don't need to provide this value yourself.
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )