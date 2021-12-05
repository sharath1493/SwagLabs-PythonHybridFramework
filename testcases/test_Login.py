import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from configfiles.FrameworkConstants import FrameworkConstants
from pages.LoginPage import LoginPage
from utilities import FullScreenshot


class Test_Login:

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.mytests
    def test_login(self, setup):
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lp.doLaunchURL()
        self.lp.dologin()
        if self.driver.current_url.__eq__("https://www.saucedemo.com/inventory.html"):
            self.driver.close()
            assert True
        else:
            time.sleep(3)
            FullScreenshot.take_full_page_screenshot(self.driver, "testlogin")
            self.driver.close()
            assert False

    @pytest.mark.smoke
    @pytest.mark.mytests
    def test_login2(self, setup):
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lp.doLaunchURL()
        assert self.driver.current_url.__eq__(FrameworkConstants.BASE_URL.value)
        self.driver.close()

