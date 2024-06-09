from src.components.repeat_func import click_button, assert_element_text, scroll_write_element
from src.helpers.date_helper import select_date
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def add_job (driver, SELECTORS, ASSERT_TEXT, work, current_year_int, previous_month_int, previous_month_string):
    # Verify that the radio buttons for how one looked for the job are visible
    assert_element_text(driver, By.XPATH, SELECTORS['XPATH']['search_how_text'], ASSERT_TEXT['how_searched'])

    # How did you look for the job?
    sleep(1)
    radio_buttons_container = driver.find_element(By.ID, SELECTORS['ID']['radio_buttons_container'])
    radio_buttons_container.is_displayed()
    ActionChains(driver)\
        .scroll_to_element(radio_buttons_container)\
        .perform()

    # Hur har du sokt jobbet radio buttons
    sleep(1)
    radio_value = work['searched']
    if radio_value == "soktjobb":
        click_button(driver, By.XPATH, SELECTORS['XPATH']['radio_Button_Sokt_Jobb'])
    elif radio_value == "intresseanmalan":
        click_button(driver, By.XPATH, SELECTORS['XPATH']['radio_Button_Spontanansokan'])

    # What type of work?
    sleep(1)
    if radio_value == "soktjobb":
        scroll_write_element(driver, By.ID, SELECTORS['ID']['soktjobb_soktTjanst'], work['job'])
    elif radio_value == "intresseanmalan":
        scroll_write_element(driver, By.ID, SELECTORS['ID']['intresseanmalan_soktTjanst'], work['job'])

    # Which employer?
    sleep(1)
    if radio_value == "soktjobb":
        scroll_write_element(driver, By.ID, SELECTORS['ID']['soktjobb_arbetsgivare'], work['employer'])
    elif radio_value == "intresseanmalan":
        scroll_write_element(driver, By.ID, SELECTORS['ID']['intresseanmalan_arbetsgivare'], work['employer'])

    # In which country does the job exist?
    sleep(1)
    radio_country_value = work['country']
    if radio_country_value == "sweden":
        click_button(driver, By.XPATH, SELECTORS['XPATH']['radio_Button_country_sweden'])
    elif radio_country_value == "unspecified":
        click_button(driver, By.XPATH, SELECTORS['XPATH']['radio_Button_country_unspecified'])
    elif radio_country_value == "abroad":
        click_button(driver, By.XPATH, SELECTORS['XPATH']['radio_Button_country_abroad'])
    else:
        print(f"Country value {radio_country_value} is not valid. Please use 'sweden', 'unspecified' or 'abroad'.")

    # Which locality?
    sleep(1)
    locality = None
    if radio_value == "soktjobb":
        scroll_write_element(driver, By.ID, SELECTORS['ID']['soktjobb_ort'], work['locality'])
    elif radio_value == "intresseanmalan":
        scroll_write_element(driver, By.ID, SELECTORS['ID']['intresseanmalan_ort'], work['locality'])
    else:
        print(f"Radio value {radio_value} is not valid. Please use 'soktjobb' or 'intresseanmalan'.")

    # Select which date the work was applied on.
    sleep(1)
    select_date(driver, SELECTORS, work['day'], current_year_int, previous_month_int, previous_month_string)

    # Click the add the activity button
    sleep(1)
    click_button(driver, By.XPATH, SELECTORS['XPATH']['save_button'])

    # Check that the activity was added
#     activity_finished_popup = driver.find_element(By.XPATH, '//*[@id="arw-container"]/ng-component/arw-full-page-block[1]/div/section/div/arw-popup/div/digi-ng-util-detect-click-outside/div/div/digi-ng-layout-segment/div/div[1]/strong')
#     activity_finished_popup.is_displayed()
#     assert activity_finished_popup.text == "Din aktivitet är sparad"
