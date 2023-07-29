import pytest
import allure
from pages.page_registration import Registration_page



class Test_registration:
    @allure.tag("Steps")
    @allure.label("owner", "Vitalii Eremeev")
    @allure.feature("Tests for burgers")
    @allure.link("https://stellarburgers.nomoreparties.site")
    @allure.title("Полное заполнение и отправка формы")
    @allure.severity(severity_level='HIGH')
    @pytest.mark.parametrize('window_size', ['FullHD', '720p'], indirect=True)
    @allure.step("")

    def test_registration_desktop(self, setup_browser):
        registration_page = Registration_page()
        with allure.step('Открытие главной страницы'):
            registration_page.browser_open()
        with allure.step('Кнопка перехода на регистарцию'):
            registration_page.account()
        with allure.step('Кнопка регистарции'):
            registration_page.registration_button()
        with allure.step('Заполнение - имя'):
            registration_page.name()
        with allure.step('Заполнение - почта'):
            registration_page.email()
        with allure.step('Заполнение - пароль'):
            registration_page.password()
        with allure.step('Подтверждение'):
            registration_page.button_submit()
