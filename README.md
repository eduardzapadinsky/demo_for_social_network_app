# Social Network Automation Script

This Python script is designed to automate interactions with a social networking application using its API. The script
creates users, generates random posts, and likes random posts for those users. It is intended for testing and
demonstration purposes only.

## Prerequisites

Before running this script, make sure you have the following:

1. Python installed on your system.
2. The requests library installed. You can install it using pip:

   ```bash
   pip install requests
   ```

3. A running instance of the social networking application's Django API. The API repository can be
   found [here](https://github.com/eduardzapadinsky/social_network_app). You can modify the `API_URL` variable in the
   script to point to the correct API endpoint.

## Configuration

The script reads its configuration from a JSON file named `config.json`. If the file is not found, it uses default
values. You can customize the following parameters in the `config.json` file:

- `number_of_users`: The number of users to create.
- `max_posts_per_user`: The maximum number of posts each user can create.
- `max_likes_per_user`: The maximum number of likes each user can give.

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/eduardzapadinsky/demo_for_social_network_app.git
   ```

2. Navigate to the directory where the script is located.

3. Create a `config.json` file if you want to customize the configuration (optional). Here's an example
   of `config.json`:

   ```json
   {
       "number_of_users": 5,
       "max_posts_per_user": 10,
       "max_likes_per_user": 15
   }
   ```

4. Run the script:

   ```bash
   python demo_for_social_network_app.py
   ```

