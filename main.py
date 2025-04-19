import pytest
import json
import datetime
from src.helpers.month_helper import get_string
from src.helpers.login_helper import bankid, freja, normal_id, foreign_id, password
from src.components.repeat_func import click_button, assert_element_text, scroll_click_element
from src.components.select_driver import select_driver
from src.components.interviews import add_interview
from src.components.jobs import add_job
from time import sleep
from rich.console import Console
from selenium.webdriver.common.by import By
from functools import partial

console = Console()
GO_BACK_BY = 1

# Handle command line arguments for the user selecting a driver
@pytest.fixture(scope="session")
def driver_fixture(pytestconfig):
    return pytestconfig.getoption("driver")

# Handle command line arguments for the user selecting a month
@pytest.fixture(scope="session")
def month_fixture(pytestconfig):
    return pytestconfig.getoption("month")

# Handle command line arguments for the user selecting a login option
@pytest.fixture(scope="session")
def login_fixture(pytestconfig):
    return pytestconfig.getoption("login")

def test_main(driver_fixture, login_fixture, month_fixture):
    # Select the driver
    sleep(1)
    driver = select_driver(driver_fixture)

    login_details_list = None
    try:
        with open('login_details.txt', 'r') as f:
            login_details = f.read()
            login_details_list = login_details.split(':')
    except:
        console.print("Could not find login details file. Please create a login_details.txt file and add your Username and Password to it.")
        driver.close()

    # Get the current year and month as numbers
    sleep(1)
    current_year_num = datetime.date.today().year
    current_month_num = datetime.date.today().month

    # Get the data for the current year
    data_year = None
    with open('jobbs.json', 'r') as f:
        full_file = json.load(f)
        data_year = full_file[str(current_year_num)]

    # Get the selectors
    SELECTORS = None
    with open('src/data/locators.json', 'r') as f:
        SELECTORS = json.load(f)


    # Get the assertion texts
    ASSERT_TEXT = None
    with open('src/data/text_assert.json', 'r') as f:
        ASSERT_TEXT = json.load(f)

    # Get searched works and interviews for previous month
    sleep(1)
    previous_month_num = current_month_num - GO_BACK_BY
    previous_month_string = get_string(previous_month_num)
    print(previous_month_string)
    searched_works = data_year[previous_month_string]["work"]
    searched_interviews = data_year[previous_month_string]["interviews"]

    # Navigate to the website and maximize the window
    sleep(1)
    driver.get('https://arbetsformedlingen.se/')
    driver.maximize_window()

    # Accept cookies
    click_button(driver, By.ID, SELECTORS['ID']['cookie_decline'])

    # Navigate to the login page
    click_button(driver, By.CLASS_NAME, SELECTORS['CLASS_NAME']['function_nav_item'])

    # Select which login todo
    if login_fixture == "bankid" or login_fixture == None:
        bankid(driver, SELECTORS)
    elif login_fixture == "freja":
        freja(driver, SELECTORS)
    elif login_fixture == "id":
        normal_id(driver, SELECTORS)
    elif login_fixture == "foreign-id":
        foreign_id(driver, SELECTORS)
    elif login_fixture == "password":
        password(driver, SELECTORS, login_details_list)

    # Navigate to the report page
    click_button(driver, By.XPATH, SELECTORS['XPATH']["aktivitets_rapport"], 3)

    # Handle the rapport pop up
    #assert_element_text(driver, By.XPATH, SELECTORS['XPATH']["tanka_pa_nar_du_aktivitetsrapporterar"], ASSERT_TEXT["to_think_about"])
    scroll_click_element(driver, By.XPATH, SELECTORS['XPATH']["pop_up_close_button"])

    # Verify that the min aktivitetsrapport page is displayed
    assert_element_text(driver, By.XPATH, SELECTORS['XPATH']["min_aktivitetsrapport"], ASSERT_TEXT["aktivitetsrapport"], 3, 0)

    # Start adding activities
    click_button(driver, By.XPATH, SELECTORS['XPATH']["lagg_till_aktiviteter_button"], 1, 2)

    # Verify that the add activity page is displayed
    assert_element_text(driver, By.XPATH, SELECTORS['XPATH']["lagg_till_aktiviteter_text"], ASSERT_TEXT["add_activity"], 3, 0)

    # Loop to add each job
    sleep(1)
    if len(searched_works) != 0:
        curried_driver_job_file = partial(add_job, driver)
        curried_selectors_job_file = partial(curried_driver_job_file, SELECTORS)
        curried_assert_text_job_file = partial(curried_selectors_job_file, ASSERT_TEXT)
        for work in searched_works:
            curried_assert_text_job_file(work, current_year_num, previous_month_num, previous_month_string)


    # Add interviews
    sleep(1)
    if len(searched_interviews) != 0:
        curried_driver_interview_file = partial(add_interview, driver)
        curried_selectors_interview_file = partial(curried_driver_interview_file, SELECTORS)
        curried_assert_text_interview_file = partial(curried_selectors_interview_file, ASSERT_TEXT)
        for interview in searched_interviews:
            curried_assert_text_interview_file(interview, current_year_num, previous_month_num, previous_month_string)

    driver.close()
