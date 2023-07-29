from dataclasses import dataclass

from attr import dataclass
from selene import browser, have
from locators.locator import User_Locators
from helpers.setting_info import UserData
from selene.support.shared.jquery_style import s

locator = User_Locators()
@dataclass()
class Registration_page:

    locator = User_Locators()
    data = UserData

    def browser_open(self):
        browser.open("")

    def account(self):
        s(self.locator.ICONBUTTON).click()
    def registration_button(self):
        s(self.locator.REG).click()

    def name(self):
        s(self.locator.NAME).send_keys(self.data.FIRSTNAME)


    def email(self):
        s(self.locator.EMAIL).send_keys(self.data.EMAIL)

    def password(self):
        s(self.locator.PASSWORD).send_keys(self.data.PASSWORD)

    def button_submit(self):
        s(self.locator.SUBMIT).click()
