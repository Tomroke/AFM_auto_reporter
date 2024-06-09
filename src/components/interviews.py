from src.helpers.date_helper import select_date
from src.components.repeat_func import click_button, assert_element_text, scroll_click_element, scroll_write_element
from time import sleep
from selenium.webdriver.common.by import By

def add_interview(driver, SELECTORS, ASSERT_TEXT, interview, current_year_int, previous_month_int, previous_month_string):
    # Verify that the add activity page is displayed
    assert_element_text(driver, By.XPATH, SELECTORS['XPATH']['add_activity_header'], ASSERT_TEXT["add_activity"])

    # Find, verify and click interview button
    scroll_click_element(driver, By.XPATH, SELECTORS['XPATH']['interview_button'])

    # Verify that the interview form has appeared
    assert_element_text(driver, By.XPATH, SELECTORS['XPATH']['interview_form_header'], ASSERT_TEXT["interview"])

    # Fill out employer
    scroll_write_element(driver, By.ID, SELECTORS['ID']['interview_form_employer'], interview['employer'])

    # Fill out which job the interview was about (optional)
    scroll_write_element(driver, By.XPATH, SELECTORS['XPATH']['interview_form_job'], interview['job'])

    # In which country?
    sleep(1)
    radio_country_value = interview['country']
    if radio_country_value == "sweden":
        click_button(driver, By.XPATH, SELECTORS['XPATH']['radio_Button_country_sweden'])
    elif radio_country_value == "unspecified":
        click_button(driver, By.XPATH, SELECTORS['XPATH']['radio_Button_country_unspecified'])
    elif radio_country_value == "abroad":
        click_button(driver, By.XPATH, SELECTORS['XPATH']['radio_Button_country_abroad'])
    else:
        print(f"Country value {radio_country_value} is not valid. Please use 'sweden', 'unspecified' or 'abroad'.")

    # Fill out locality
    scroll_write_element(driver, By.ID, SELECTORS['ID']['interview_form_locality'], interview['locality'])

    # Fill out date
    select_date(driver, SELECTORS, interview['day'], current_year_int, previous_month_int, previous_month_string)

    # Click the save the activity button
    scroll_click_element(driver, By.XPATH, SELECTORS['XPATH']['save_button'])



