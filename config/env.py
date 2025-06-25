from dotenv import load_dotenv
import os

load_dotenv()  # load variables from .env in root

GROK_API_KEY = os.getenv("GROK_API_KEY")

if GROK_API_KEY is None:
    raise ValueError("GROK_API_KEY not found in environment variables. Check your .env file.")

if __name__ == "__main__":
    print("GROK_API_KEY:", GROK_API_KEY)
