# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values

# loading variables from .env file
load_dotenv()


def my_youtube_key():
    return os.getenv("YOUTUBE_KEY_ID")


def my_github_token():
    return os.getenv("GITHUB_TOKEN")
