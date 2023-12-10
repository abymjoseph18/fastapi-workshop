from graphene import ObjectType, String, Schema, List, Field, Argument, Mutation, Int


class UserType(ObjectType):
    # fields from user_data (or from DB)
    first_name = String(description="User's first name")
    last_name = String(description="User's last name")
    age = Int(description="User's age")
    email = String(description="User's email address")
    address = String(description="User's address")

    # custom field to be resolved
    display_name = String(description="User's custom display name")

    def resolve_display_name(self, info):
        # Combine first_name and last_name for the display name
        return f"{self.first_name} {self.last_name}"


# Dummy user data for illustration
user_data = [
    {"first_name": "John", "last_name": "Doe", "age": 30, "email": "john@example.com", "address": "123 Main St"},
    {"first_name": "Alice", "last_name": "Smith", "age": 25, "email": "alice@example.com", "address": "456 Oak Ave"},
    {"first_name": "Bob", "last_name": "Johnson", "age": 35, "email": "bob@example.com", "address": "789 Pine Rd"},
    {"first_name": "Eve", "last_name": "Johnson", "age": 28, "email": "eve@example.com", "address": "101 Cedar Ln"},
    {"first_name": "Charlie", "last_name": "Brown", "age": 40, "email": "charlie@example.com",
     "address": "222 Elm St"},
]


class Query(ObjectType):
    # Query 1: List all users
    users_query = List(UserType, description="List of users")

    # Resolver for query users
    def resolve_users_query(self, info):
        # Convert the list of dictionaries to a list of User objects
        users = [UserType(**user) for user in user_data]
        return users

    # Query 1: List user with input email
    user_query = Field(UserType, email=Argument(String, description="User's email"))

    def resolve_user_query(self, info, email):
        # Find and return the user with the specified email
        for user in user_data:
            if user["email"] == email:
                return UserType(**user)
        return None


class AddUser(Mutation):
    # input arguments
    class Arguments:
        first_name = String(description="User's first name")
        last_name = String(description="User's last name")
        age = String(description="User's age")
        email = String(description="User's email address")
        address = String(description="User's address")

    # output arguments
    user = Field(UserType)

    def mutate(self, info, first_name, last_name, age, email, address):
        # Add the new user to the user_data
        new_user = {"first_name": first_name, "last_name": last_name, "age": age, "email": email, "address": address}
        user_data.append(new_user)

        # Return the new user
        return AddUser(user=UserType(**new_user))


class Mutation(ObjectType):
    add_user = AddUser.Field(description="Add a new user")


schema = Schema(query=Query, mutation=Mutation)
