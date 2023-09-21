"""
This Python script is designed to automate interactions with a social networking application using its API.
The script creates users, generates random posts, and likes random posts for those users.
It is intended for testing and demonstration purposes only.
"""

import requests
import random
import string
import json

# Define the URL of your Django API
API_URL = "http://localhost:8000/api/"

posts_number = 0

config_file_path = "config.json"

try:
    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)
except FileNotFoundError:
    # Handle the case when the JSON file is not found
    config = {
        "number_of_users": 5,
        "max_posts_per_user": 10,
        "max_likes_per_user": 15
    }


# Function to generate a random string for post content
def random_string(length):
    """
    Generate a random string for post content.
    Args:
        length (int): The length of the random string.
    Returns:
        str: A random string of the specified length.
    """

    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


# Function to create a new user
def create_user(user_name):
    """
    Create a new user using the API.
    Args:
        user_name (str): The username for the new user.
    Returns:
        int or None: The user ID if user creation is successful, or None if it fails.
    """

    response = requests.post(
        f"{API_URL}signup/",
        data={"username": user_name, "password": "password"},
    )
    if response.status_code == 201:
        print(f"User {user_name} created successfully")
        return json.loads(response.text)["id"]
    else:
        print(f"Failed to create user {user_name}")
        return None


# Function to get an authentication token for a user
def get_token(user_name):
    """
    Get an authentication token for a user.
    Args:
        user_name (str): The username of the user.
    Returns:
        str or None: The authentication token if successful, or None if it fails.
    """

    response = requests.post(
        f"{API_URL}auth/",
        data={"username": f"{user_name}", "password": "password"},
    )
    if response.status_code == 200:
        return json.loads(response.text)["access"]
    else:
        return None


# Function to create random posts for a user
def create_posts(user_name, max_posts):
    """
    Create random posts for a user.
    Args:
        user_name (str): The username of the user creating posts.
        max_posts (int): The maximum number of posts the user can create.
    """

    global posts_number

    num_posts = random.randint(1, max_posts)
    for _ in range(num_posts):
        content = random_string(random.randint(10, 20))
        data = {
            "content": content
        }
        response = requests.post(
            f"{API_URL}post/create/",
            data=data,
            headers={"Authorization": f"Bearer {get_token(user_name)}"},
        )
        if response.status_code == 201:
            # Parse the response JSON to get the post ID
            post_data = response.json()
            post_id = post_data.get("id")

            print(f"User {user_name} created a post {post_id}")
            posts_number += 1
        else:
            print(f"Failed to create a post for user {user_name}")


# Function to like random posts
def like_posts(user_name, max_likes):
    """
    Like random posts for a user.
    Args:
        user_name (str): The username of the user liking posts.
        max_likes (int): The maximum number of likes the user can give.
    """

    unique_post_ids = list(range(1, posts_number + 1))
    random.shuffle(unique_post_ids)

    num_likes = random.randint(1, max_likes)
    for _ in range(num_likes):

        if not unique_post_ids:
            print(f"All available posts have been liked by user {user_name}")
            break

        post_id = unique_post_ids.pop()
        response = requests.put(
            f"{API_URL}post/{post_id}/like/",
            headers={"Authorization": f"Bearer {get_token(user_name)}"},
        )
        if response.status_code == 200:
            print(f"User {user_name} liked post {post_id}")
        else:
            print(f"Failed to like the {post_id} by user {user_name}")


if __name__ == "__main__":
    # Create users

    for i in range(config["number_of_users"]):
        username = f"urNui{i + 1}"
        user_id = create_user(username)
        if user_id:
            # Create posts for each user
            create_posts(username, config["max_posts_per_user"])

            # Like posts for each user
            like_posts(username, config["max_likes_per_user"])
