from dataclasses import dataclass

@dataclass
class User_Locators:
    ICONBUTTON = '#root > div > main > section.BurgerConstructor_basket__29Cd7.mt-25 > div > button'
    CREATETEXT = 'Create one'
    REG = '#root > div > main > div > div > p.undefined.text.text_type_main-default.text_color_inactive.mb-4 > a'
    NAME = '#root > div > main > div > form > fieldset:nth-child(1) > div > div > input'
    EMAIL = '#root > div > main > div > form > fieldset:nth-child(2) > div > div > input'
    PASSWORD = '#root > div > main > div > form > fieldset:nth-child(3) > div > div > input'
    SUBMIT = '#root > div > main > div > form > button'
