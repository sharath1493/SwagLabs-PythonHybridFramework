import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from configfiles.FrameworkConstants import FrameworkConstants
from pages.LoginPage import LoginPage
from utilities import FullScreenshot
from utilities.ExcelUtils import ExcelUtils


class Test_LoginDDT:
    @pytest.mark.regression
    @pytest.mark.mytests
    def test_loginDDT(self, setup):
        r = ExcelUtils.getrowcount("Billing")
        c = ExcelUtils.getcolumncount("Billing")

        es = []
        ast = []

        for r in range(2, r+1):
            # self.driver = webdriver.Chrome(ChromeDriverManager().install())
            self.driver = setup
            self.driver.get("https://www.saucedemo.com/")
            self.driver.find_element(By.ID, "user-name").send_keys(ExcelUtils.readdata("Billing", r, 1))
            self.driver.find_element(By.ID, "password").send_keys(ExcelUtils.readdata("Billing", r, 2))
            es.append(ExcelUtils.readdata("Billing", r, 3))
            self.driver.find_element(By.ID, "login-button").click()
            url = self.driver.current_url
            if url.__eq__("https://www.saucedemo.com/inventory.html"):
                FullScreenshot.take_full_page_screenshot(self.driver, "DDT-testlogin {0}".format(r-1))
                self.driver.find_element(By.ID, "react-burger-menu-btn").click()
                # self.driver.find_element_by_link_text("Logout").click()
                ele = self.driver.find_element(By.ID, "logout_sidebar_link")
                self.driver.execute_script("arguments[0].click();", ele)
                ast.append("Pass")
                print(f"Test {r-1} is Pass")
            else:
                ast.append("Fail")
                FullScreenshot.take_full_page_screenshot(self.driver, "DDT-testlogin {0}".format(r-1))
                print(f"Test {r-1} is Fail")

        self.driver.close()
        print(es)
        print(ast)
        assert es.__eq__(ast), "Login Data Driven Test is a Fail"



