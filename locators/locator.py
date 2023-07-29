from dataclasses import dataclass

@dataclass
class User_Locators:
    ICONBUTTON = '[id="signup"]'
    CREATETEXT = 'Create one'
    FIRSTNAME = '[id="firstName"]'
    LASTNAME = '[id="lastName"]'
    EMAIL = '[id="email"]'
    PASSWORD = '[id="password"]'
    SUBMIT = '[id="submit"]'
