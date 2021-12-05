import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from configfiles.FrameworkConstants import FrameworkConstants


class BasePageActions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def dosendkeys(self, by, text):
        self.wait.until(EC.presence_of_element_located(by)).clear()
        self.wait.until(EC.presence_of_element_located(by)).send_keys(text)

    def doclick(self, by):
        self.wait.until(EC.element_to_be_clickable(by)).click()

    def get_element_text(self, by):
        element = self.wait.until(
            EC.visibility_of_element_located(by))
        return element.text

    def get_elements_list(self, by):
        elements = self.wait.until(
            EC.visibility_of_all_elements_located(by)
        )
        return elements

    def doLaunchURL(self):
        self.driver.get(FrameworkConstants.BASE_URL.value)

    def take_full_page_screenshot(self, title):
        S = lambda X: self.driver.execute_script("return document.body.parentNode.scroll" + X)
        self.driver.set_window_size(S("Width"), S("Height"))

        for ch in ['/', '*', '\\', '?', ':', '|', '"', '>', '<', '#']:
            if ch in title:
                title = title.replace(ch, ' ')

        print(title)

        ct = str(time.asctime()).replace(':', '-')
        # screenshot = self.get_title()
        self.driver.find_element(
            By.TAG_NAME, "body").screenshot(".\\Screenshots\\Screenshot - "+title+" "+ct+".png")

    def selectDropDownByValue(self, by, value):
        drpdwn = Select(self.wait.until(EC.visibility_of_element_located(by)))
        drpdwn.select_by_visible_text(value)

