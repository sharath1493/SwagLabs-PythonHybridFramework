import enum


class FrameworkConstants(enum.Enum):

    # URLs, Usernames and Passwords

    STANDARD_USER = "standard_user"
    LOCKED_OUT_USER = "locked_out_user"
    PROBLEM_USER = "problem_user"
    PERFORMANCE_GLITCH_USER = "performance_glitch_user"
    PASSWORD = "secret_sauce"
    BASE_URL = "https://www.saucedemo.com/"

    # Inventory Page data
    SORT_ORDER_NAME_ATOZ_TEXT = "NAME (A TO Z)"
    SORT_ORDER_NAME_ZTOA_TEXT = "NAME (Z To A)"
    SORT_ORDER_PRICE_LOWTOHIGH_TEXT = "PRICE (LOW TO HIGH)"
    SORT_ORDER_PRICE_HIGHTOLOW_TEXT = "PRICE (HIGH TO LOW)"

    ITEMS_NAMES_LIST_ATOZ_ORDER = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt",
                        "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]
    ITEMS_NAMES_LIST_LOWTOHIGH_ORDER = ["Sauce Labs Onesie", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt",
                        "Test.allTheThings() T-Shirt (Red)", "Sauce Labs Backpack", "Sauce Labs Fleece Jacket"]









