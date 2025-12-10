# test_dotenv.py
from dotenv import load_dotenv
import os

# Adjust path if your .env is inside 'backend' folder
load_dotenv('backend/.env')  

# Read BEARER_TOKEN from .env
bearer_token = os.getenv('BEARER_TOKEN')

if bearer_token:
    print("✅ BEARER_TOKEN loaded successfully!")
    print("Your token starts with:", bearer_token[:10], "...")  # just for checking
else:
    print("❌ BEARER_TOKEN not found. Check .env file and variable name.")
