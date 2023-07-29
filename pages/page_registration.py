from dataclasses import dataclass

from attr import dataclass
from selene import browser, have
from locators.locator import User_Locators
from helpers.setting_info import UserData

locator = User_Locators()
@dataclass()
class Registration_page:

    locator = User_Locators()
    data = UserData

    def browser_open(self):
        browser.open("")

    def account(self):
        browser.element(self.locator.ICONBUTTON).click()
    def registration_button(self):
        browser.element(self.locator.REG).click()

    def name(self):
        browser.element(self.locator.NAME).send_keys(self.data.FIRSTNAME)


    def email(self):
        browser.element(self.locator.EMAIL).send_keys(self.data.EMAIL)

    def password(self):
        browser.element(self.locator.PASSWORD).send_keys(self.data.PASSWORD)

    def button_submit(self):
        browser.open(self.locator.SUBMIT).click()
