import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_CLIENT_ID = os.environ["GOOGLE_CLIENT_ID"] or None
GOOGLE_CLIENT_SECRET = os.environ["GOOGLE_CLIENT_SECRET"] or None
SECRET_KEY = os.environ["SECRET_KEY"] or None