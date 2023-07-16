import pytest

from pages.page_registration import Registration_page


class Test_autorization:

    @pytest.mark.parametrize('window_size', ['desktop', 'desktop1'], indirect=True)
    def test_registration_desktop(self, setup_browser):
        registration_page = Registration_page()
        registration_page.browser_open()
        registration_page.account()
        # registration_page.create_account()
        # registration_page.first_name()
        # registration_page.last_name()
        # registration_page.email()
        # registration_page.password()
        # registration_page.button_pass()
