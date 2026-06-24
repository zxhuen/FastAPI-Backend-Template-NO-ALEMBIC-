# Import Session from SQLAlchemy.
# This is the active database connection that will be used
# throughout the request.
from sqlalchemy.orm import Session

# Import repository functions.
#
# The repository layer is responsible for talking directly
# to the database.
#
# create_post() -> Inserts a new post into the database.
# get_posts()   -> Retrieves all posts from the database.
from app.repository.post_repo import create_post, get_posts

# Import the Pydantic schema used to validate
# incoming request data.
from app.schemas.post import PostCreate


# Service function for creating a new post.
#
# Parameters:
# db   -> Active database session.
# post -> Validated request body (PostCreate schema).
#
# Right now, this simply calls the repository function.
# In larger applications, this is where business logic goes.
def add_post(db: Session, post: PostCreate):

    # Call the repository to insert the post into the database,
    # then return the newly created post.
    return create_post(db, post)


# Service function for retrieving all posts.
#
# Parameter:
# db -> Active database session.
def list_posts(db: Session):

    # Call the repository to fetch every post
    # from the database.
    return get_posts(db)