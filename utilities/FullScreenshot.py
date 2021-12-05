import time
from selenium.webdriver.common.by import By


def take_full_page_screenshot(driver, text):
    S = lambda X: driver.execute_script("return document.body.parentNode.scroll" + X)

    driver.set_window_size(S("Width"), S("Height"))

    """
    ----------Below is more readable way --------------------- -------------------------------------
    w = driver.execute_script('return document.body.parentNode.scrollWidth')
    h = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(w, h)
    driver.find_element_by_tag_name('body').screenshot(".\\Screenshots\\"+"tutorialspoint.png")
    ------------------------------------------------------------------------------------------------
    
    for ch in ['/', '*', '\\', '?', ':', '|', '"', '>', '<', '#']:
        if ch in text:
            text = text.replace(ch, ' ')
    """

    ct = str(time.asctime()).replace(':', '-')

    driver.find_element(By.TAG_NAME, "body").screenshot(".\\Screenshots\\" + text + " - " + ct + ".png")
