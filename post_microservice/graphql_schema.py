# Graphene is the library that we'll be using in this demo
from graphene import ObjectType, String, List
from graphene_federation import key, build_schema, external


class PostType(ObjectType):
    post_name = String(description="Post name")
    description = String(description="Post description")
    email = String(description="Author's email")


posts_data = [
    {"post_name": "Post 1", "description": "Description 1", "email": "john@example.com"},
    {"post_name": "Post 2", "description": "Description 2", "email": "john@example.com"},
    {"post_name": "Post 3", "description": "Description 3", "email": "alice@example.com"},
    {"post_name": "Post 4", "description": "Description 4", "email": "alice@example.com"},
    {"post_name": "Post 5", "description": "Description 5", "email": "john@example.com"},
    # Add more posts as needed
]


# Here we first define the GraphQL Types required
@key("email")
class UserType(ObjectType):
    email = external(String(required=True))
    posts_by_user = List(PostType)

    def resolve_posts_by_user(self, info):
        # Filter posts by user email
        user_posts = [PostType(**post)
                      for post in posts_data if post["email"] == self.email]
        return user_posts


schema = build_schema(types=[UserType], enable_federation_2=True)
