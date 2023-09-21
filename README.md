# Social Network Automation Script

This Python script is designed to automate interactions with a social networking application using its API. The script creates users, generates random posts, and likes random posts for those users. It is intended for testing and demonstration purposes only.

## Prerequisites

Before running this script, ensure you have the following prerequisites:

- A running instance of the social networking application's Django API. The API repository can be found [here](https://github.com/eduardzapadinsky/social_network_app). You can modify the `API_URL` variable in the script to point to the correct API endpoint.

## Setting Up the Environment

To set up the environment for running the script, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/eduardzapadinsky/demo_for_social_network_app.git
   ```

2. Navigate to the directory where the script is located.

3. Create and activate a virtual environment:

   ```bash
   # On macOS and Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

4. Install the required packages from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The script reads its configuration from a JSON file named `config.json`. If the file is not found, it uses default values. You can customize the following parameters in the `config.json` file:

- `number_of_users`: The number of users to create.
- `max_posts_per_user`: The maximum number of posts each user can create.
- `max_likes_per_user`: The maximum number of likes each user can give.

## Usage

1. Run the script:

   ```bash
   python demo_for_social_network_app.py
   ```
