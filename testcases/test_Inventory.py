import pytest

from configfiles.FrameworkConstants import FrameworkConstants
from pages.Inventory import Inventory
from utilities import FullScreenshot


class Test_Inventory:
    @pytest.mark.regression
    @pytest.mark.mytests
    def test_ProductCatalogdefaultOrder(self, setup):
        actualproductnames = []
        self.driver = setup
        self.inventory = Inventory(self.driver)
        self.inventory.dologin()
        # catalogorder = self.driver.find_element(Inventory.TEXT_ACTIVE_SORT_PRODUCT_OPTION).text
        # print(catalogorder)
        print(FrameworkConstants.SORT_ORDER_NAME_ATOZ_TEXT.value)
        print(self.inventory.get_element_text(Inventory.TEXT_ACTIVE_SORT_PRODUCT_OPTION))
        # print(len(self.inventory.get_elements_list(Inventory.ELEMENTS_INVENTORY_NAME)))
        # print(type(FrameworkConstants.SORT_ORDER_NAME_ATOZ_TEXT.value))
        if self.inventory.get_element_text(Inventory.TEXT_ACTIVE_SORT_PRODUCT_OPTION).__eq__(FrameworkConstants.SORT_ORDER_NAME_ATOZ_TEXT.value):
            print("hello")
            products = self.inventory.get_elements_list(Inventory.ELEMENTS_INVENTORY_NAME)
            print(len(products))
            for i in products:
                actualproductnames.append(i.text)
            print("Expected Product Order: ", end="")
            print(FrameworkConstants.ITEMS_NAMES_LIST_ATOZ_ORDER.value)
            print("Actual Product Order: ", end="")
            print(actualproductnames)
            FullScreenshot.take_full_page_screenshot(self.driver, "productdefaultorder")
            self.driver.close()
            assert actualproductnames.__eq__(FrameworkConstants.ITEMS_NAMES_LIST_ATOZ_ORDER.value), "Products default order not matches"

    @pytest.mark.mytests
    def test_productcatalogbypricelowtohigh(self, setup):
        self.driver = setup
        self.inventory = Inventory(self.driver)
        self.inventory.dologin()
        print(Inventory.SORT_NAME_LOHI_VALUE)
        self.inventory.selectDropDownByValue(Inventory.DROPDOWN_PRODUCT_SORT, Inventory.SORT_NAME_LOHI_VALUE)
        FullScreenshot.take_full_page_screenshot(self.driver, "productcatalogbypricelowtohigh")
        actualproductnames = []
        products = self.inventory.get_elements_list(Inventory.ELEMENTS_INVENTORY_NAME)
        print(len(products))
        for i in products:
            actualproductnames.append(i.text)
        print("Expected Product Order: ", end="")
        print(FrameworkConstants.ITEMS_NAMES_LIST_LOWTOHIGH_ORDER.value)
        print("Actual Product Order: ", end="")
        print(actualproductnames)
        self.driver.close()
        assert actualproductnames.__eq__(
            FrameworkConstants.ITEMS_NAMES_LIST_LOWTOHIGH_ORDER.value), "Products default order not matches"






