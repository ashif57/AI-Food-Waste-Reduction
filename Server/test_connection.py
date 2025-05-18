import os
from pathlib import Path
from dotenv import load_dotenv
from supabase import create_client

# 1. Get the absolute path to .env
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path, override=True)

