import os
from dotenv import load_dotenv


class UserData:
    load_dotenv()

    URL = os.getenv("URL")
    FIRSTNAME = os.getenv("FIRSTNAME")
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")
    LASTNAME = os.getenv("LASTNAME")

    print(URL)  # AQAAAAAz55vbAAdBSHeydEoSe0fclxSSABT
    print(FIRSTNAME)  # ramziv.com
