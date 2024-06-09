from selenium import webdriver

def select_driver(driver_string):
    driver = None
    if driver_string != None:
        driver_string_decapitalized = driver_string.lower()
        if driver_string_decapitalized == "chrome":
            driver = webdriver.Chrome()
        elif driver_string_decapitalized == "edge":
            driver = webdriver.Edge()
        elif driver_string_decapitalized == "firefox":
            driver = webdriver.Firefox()
        elif driver_string_decapitalized == "safari":
            driver = webdriver.Safari()
    else:
        driver = webdriver.Chrome()

    return driver
