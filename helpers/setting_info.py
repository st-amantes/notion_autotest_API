import os
import random

from dotenv import load_dotenv


class UserData:
    load_dotenv()

    URL = os.getenv("URL")
    FIRSTNAME = f"{os.getenv('FIRSTNAME')}+{random.randint(10, 100)}"
    EMAIL = f"{os.getenv('EMAIL')}+{random.randint(10, 100)}@gmail.com"
    PASSWORD = os.getenv("PASSWORD")

