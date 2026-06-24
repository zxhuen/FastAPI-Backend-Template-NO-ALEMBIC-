# Import BaseModel from Pydantic.
#
# BaseModel is used to create data validation models.
# These models define what data your API expects and returns.
#
# Think of it as a "template" for JSON data.
from pydantic import BaseModel


# Schema used when creating a new post.
#
# This describes what data the client must send.
#
# Example request:
# {
#     "title": "Hello World",
#     "content": "My first FastAPI post."
# }
class PostCreate(BaseModel):

    # Title of the post.
    # Must be a string.
    title: str

    # Content/body of the post.
    # Must also be a string.
    content: str


# Schema used when sending a post back to the client.
#
# This describes what the API response should look like.
#
# Example response:
# {
#     "id": 1,
#     "title": "Hello World",
#     "content": "My first FastAPI post."
# }
class PostResponse(BaseModel):

    # Database ID of the post.
    id: int

    # Title of the post.
    title: str

    # Content of the post.
    content: str


    # Configuration for this schema.
    class Config:

        # Allows Pydantic to read data directly from SQLAlchemy model objects.
        #
        # Without this, Pydantic expects a dictionary.
        #
        # With this enabled, you can return a SQLAlchemy object like:
        #
        # return post
        #
        # instead of:
        #
        # return {
        #     "id": post.id,
        #     "title": post.title,
        #     "content": post.content
        # }
        from_attributes = True