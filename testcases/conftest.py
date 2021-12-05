import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriver


@pytest.fixture()
def setup():
    """
    if browser == "chrome":
        coptions = webdriver.ChromeOptions()
        coptions.headless = False
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=coptions)
        driver.maximize_window()
    elif browser == "firefox":
        foptions = webdriver.FirefoxOptions()
        foptions.headless = False
        driver = webdriver.Firefox(GeckoDriverManager.install(), options=foptions)
        driver.maximize_window()

    elif browser == "edge":

        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        driver.maximize_window()

    else:
    """

    coptions = webdriver.ChromeOptions()
    coptions.headless = False
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=coptions)
    driver.maximize_window()

    return driver


def teardown():
    pass

"""
def pytest_addoption(parser):    # this will get the value from CLI / hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

"""


# PyTest HTML Report # -- customizing the HTML Report

def pytest_configure(config):
    config._metadata["Project Name"] = "SWAG LABS"
    config._metadata["Module Name"] = "SauceDemo"
    config._metadata["Tester"] = "SG"


def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
