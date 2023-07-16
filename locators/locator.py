from dataclasses import dataclass

@dataclass
class User_Locators:
    ICONBUTTON = '#section-header > div > div:nth-child(4) > nav > ul > li:nth-child(1) > a'
    CREATEACCOUNT = '[class="Link Link--secondary"]'
    CREATETEXT = 'Create one'
    FIRSTNAME = '[aria-label="First name"]'
    LASTNAME = '[aria-label="Last name"]'
    EMAIL = '[aria-label="Email"]'
    PASSWORD = '[aria-label="Password"]'
    BUTTONPASS = '[class="Form__Submit Button Button--primary Button--full"]'
