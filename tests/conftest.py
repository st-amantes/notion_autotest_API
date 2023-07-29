import allure
import pytest
from selene import browser
from helpers.setting_info import UserData

@pytest.fixture(scope='function', params=['FullHD', '720p'])
def window_size(request):
    return request.param


@pytest.fixture(scope='function')
def setup_browser(window_size):

    browser.config.base_url = UserData.URL
    browser.config.timeout = 5

    if window_size == 'FullHD':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    elif window_size == '720p':
        browser.config.window_width = 1680
        browser.config.window_height = 1024
