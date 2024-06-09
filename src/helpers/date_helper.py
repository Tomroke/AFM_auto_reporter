from src.helpers.day_helper import get_day_as_string
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def select_date(driver, SELECTORS, day, current_year_int, previous_month_int, previous_month_string):
    # Open datum selector
    sleep(1)
    date_Button = driver.find_element(By.XPATH, SELECTORS['XPATH']['date_button'])
    ActionChains(driver)\
        .scroll_to_element(date_Button)\
        .perform()
    date_Button.is_displayed()
    date_Button.click()
    sleep(2)

    # Select day
    sleep(1)
    day_string = get_day_as_string(current_year_int, previous_month_int, day)
    date_string = f"{day_string.capitalize()} {day} {previous_month_string.capitalize()} {str(current_year_int)}"
    day_element = driver.find_element(By.XPATH, f".//td[descendant::span[contains(text(), '{date_string}')]]")
    day_element.is_displayed()
    day_element.click()
