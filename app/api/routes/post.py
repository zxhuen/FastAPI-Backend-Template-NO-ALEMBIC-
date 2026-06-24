# Import APIRouter and Depends from FastAPI.
#
# APIRouter -> Used to group related API endpoints together.
# Depends   -> FastAPI's dependency injection system. It automatically
#              provides things like database sessions.
from fastapi import APIRouter, Depends

# Import the SQLAlchemy Session class.
# A Session is used to communicate with the database.
from sqlalchemy.orm import Session

# Import the database dependency.
#
# get_db() creates a database session for each request,
# then automatically closes it when the request finishes.
from app.core.database import get_db

# Import the Pydantic schemas.
#
# PostCreate   -> Validates incoming request data.
# PostResponse -> Validates and formats outgoing response data.
from app.schemas.post import PostCreate, PostResponse

# Import the service layer functions.
#
# add_post()  -> Business logic for creating a post.
# list_posts() -> Business logic for retrieving all posts.
from app.services.post_service import add_post, list_posts


# Create a router for all post-related endpoints.
#
# prefix="/posts"
# Means every endpoint in this file automatically starts with "/posts".
#
# Example:
# @router.post("/") becomes POST /posts
# @router.get("/")  becomes GET  /posts
#
# tags=["posts"]
# Groups these endpoints together in the Swagger documentation.
router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)


# POST /posts
#
# Creates a new post.
#
# response_model=PostResponse
#
# After this function returns, FastAPI validates the returned object
# against the PostResponse schema before sending it back to the client.
#
# This ensures only the fields defined in PostResponse are returned.
@router.post("/", response_model=PostResponse)
def create(

    # The request body.
    #
    # FastAPI automatically:
    # 1. Reads the JSON body.
    # 2. Validates it using PostCreate.
    # 3. Converts it into a PostCreate object.
    #
    # Example JSON:
    # {
    #     "title": "Hello",
    #     "content": "World"
    # }
    post: PostCreate,

    # Database dependency.
    #
    # FastAPI automatically calls get_db(),
    # creates a database session,
    # and passes it into this function.
    db: Session = Depends(get_db)
):

    # Pass the request to the service layer.
    # The service handles the business logic.
    return add_post(db, post)


# GET /posts
#
# Retrieves every post from the database.
#
# response_model=list[PostResponse]
#
# The response should be a list of PostResponse objects.
#
# Example:
# [
#     {
#         "id": 1,
#         "title": "Hello",
#         "content": "World"
#     },
#     {
#         "id": 2,
#         "title": "FastAPI",
#         "content": "Learning"
#     }
# ]
@router.get("/", response_model=list[PostResponse])
def get_all(

    # Create a database session for this request.
    db: Session = Depends(get_db)
):

    # Ask the service layer to retrieve every post.
    return list_posts(db)