from selenium.webdriver.common.by import By

from pages.LoginPage import LoginPage


class Inventory(LoginPage):

    TEXT_ACTIVE_SORT_PRODUCT_OPTION = (By.XPATH, "//span[@class='active_option']")

    ELEMENTS_INVENTORY_NAME = (By.XPATH, "//div[@class='inventory_item_name']")
    ELEMENTS_INVENTORY_PRICE = (By.XPATH, "//div[@class='inventory_item_price']")

    # SORT Order values
    DROPDOWN_PRODUCT_SORT = (By.XPATH, "//select[@class='product_sort_container']")
    SORT_NAME_AZ_VALUE = "Name (A to Z)"
    SORT_NAME_ZA_VALUE = "Name (Z to A)"
    SORT_NAME_LOHI_VALUE = "Price (low to high)"
    SORT_NAME_HILO_VALUE = "Price (high to low)"

    def __init__(self, driver):
        super(Inventory, self).__init__(driver)










