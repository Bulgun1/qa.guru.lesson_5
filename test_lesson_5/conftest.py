from sys import modules

import pytest
from selene import browser

@pytest.fixture(scope='module', autouse=True)
def browser_management():
    browser.config.base_url="https://demoqa.com"
    browser.config.window_height=1800
    browser.config.window_width=1200


    yield
    browser.quit()