import pytest
from selene import browser
from helpers.setting_info import UserData

@pytest.fixture(scope='function', params=['desktop', 'tablet', 'mobile'])
def window_size(request):
    return request.param


@pytest.fixture(scope='function')
def setup_browser(window_size):

    browser.config.base_url = UserData.URL
    browser.config.timeout = 5

    if window_size == 'desktop':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    elif window_size == 'desktop1':
        browser.config.window_width = 1680
        browser.config.window_height = 1024

    # browser_name = get_option_browser_name
    # browser_name = browser_name if browser_name != '' else DEFAULT_BROWSER
    #
    # browser_version = get_option_browser_version
    # browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
