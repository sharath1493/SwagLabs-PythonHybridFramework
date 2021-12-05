from selenium.webdriver.common.by import By

from configfiles.FrameworkConstants import FrameworkConstants
from pages.BasePageActions import BasePageActions


class LoginPage(BasePageActions):
    TEXTBOX_USERNAME = (By.ID, "user-name")
    TEXTBOX_PASSWORD = (By.ID, "password")
    BUTTON_LOGIN = (By.ID, "login-button")

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    def dologin(self):
        self.doLaunchURL()
        self.dosendkeys(self.TEXTBOX_USERNAME, FrameworkConstants.STANDARD_USER.value)
        self.dosendkeys(self.TEXTBOX_PASSWORD, FrameworkConstants.PASSWORD.value)
        self.doclick(self.BUTTON_LOGIN)





