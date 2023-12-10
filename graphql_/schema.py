from graphene import ObjectType, String, Schema, List


class User(ObjectType):
    first_name = String(description="User's first name")
    last_name = String(description="User's last name")
    age = String(description="User's age")
    email = String(description="User's email address")
    address = String(description="User's address")


# Dummy user data for illustration
user_data = [
    {"first_name": "John", "last_name": "Doe", "age": "30", "email": "john@example.com", "address": "123 Main St"},
    {"first_name": "Alice", "last_name": "Smith", "age": "25", "email": "alice@example.com", "address": "456 Oak Ave"},
    {"first_name": "Bob", "last_name": "Johnson", "age": "35", "email": "bob@example.com", "address": "789 Pine Rd"},
    {"first_name": "Eve", "last_name": "Johnson", "age": "28", "email": "eve@example.com", "address": "101 Cedar Ln"},
    {"first_name": "Charlie", "last_name": "Brown", "age": "40", "email": "charlie@example.com",
     "address": "222 Elm St"},
]


class Query(ObjectType):
    users = List(User, description="List of users")

    def resolve_users(self, info):
        # Convert the list of dictionaries to a list of User objects
        users = [User(**user) for user in user_data]
        return users


schema = Schema(query=Query)

