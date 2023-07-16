import os
from dotenv import load_dotenv


class UserData:
    load_dotenv()

    URL = os.getenv("URL")
    FIRSTNAME = os.getenv("FIRSTNAME")

    print(URL)  # AQAAAAAz55vbAAdBSHeydEoSe0fclxSSABT
    print(FIRSTNAME)  # ramziv.com
