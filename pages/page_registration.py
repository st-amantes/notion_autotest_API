from dataclasses import dataclass

from attr import dataclass
from selene import browser, have
from locators.locator import User_Locators

locator = User_Locators()
@dataclass()
class Registration_page:

    locator = User_Locators()

    def browser_open(self):
        browser.open("")

    def account(self):
        browser.element(self.locator.ICONBUTTON).click()

    def create_account(self):
        browser.all(self.locator.CREATEACCOUNT).element_by(have.exact_text(self.locator.CREATETEXT)).click()

    def first_name(self):
        browser.element(self.locator.FIRSTNAME).send_keys()

    def last_name(self):
        browser.element(self.locator.LASTNAME).send_keys()

    def email(self):
        browser.element(self.locator.EMAIL).send_keys()

    def password(self):
        browser.element(self.locator.PASSWORD).send_keys()

    def button_pass(self):
        browser.open(self.locator.BUTTONPASS).click()
