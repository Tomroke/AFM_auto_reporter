from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

def interact_with_login_select_button(driver, selector):
    # Select which way to login
    sleep(1)
    login_button_element = driver.find_element(By.ID, selector)
    login_button_element.is_displayed()
    login_button_element.click()
    sleep(3)

def bankid(driver, SELECTORS):
    # Select bankID as login option
    interact_with_login_select_button(driver, SELECTORS['ID']['bankID'])

    # Log in with bankID
    sleep(1)
    main_content = driver.find_element(By.XPATH, SELECTORS['XPATH']["logga_in_med_bank_id"])
    main_content.is_displayed()
    assert main_content.text == "Logga in med bank-id"

    bankID_button = driver.find_element(By.ID, SELECTORS['ID']["login_button_2"])
    bankID_button.is_displayed()
    assert bankID_button.text == "Mobilt bank-id"
    bankID_button.click()
    WebDriverWait(driver, 15).until(lambda x: x.find_element(By.ID, SELECTORS['ID']["asms_h1_heading"])).is_displayed()

def freja(driver, SELECTORS):
    interact_with_login_select_button(driver, SELECTORS['ID']['freja'])

    # Log in with Freja
    sleep(1)
    main_content = driver.find_element(By.ID, SELECTORS['ID']["freja_header"])
    main_content.is_displayed()
    assert main_content.text == "Freja e-id"

def normal_id(driver, SELECTORS):
    interact_with_login_select_button(driver, SELECTORS['ID']['normal_id'])
    print("Normal ID NOT DONE")
    # Log in with normal ID
#     sleep(1)
#     id_header_popup = driver.find_element(By.Id, SELECTORS['ID']['skatteverk_popup_header'])
#
#     pop_up_accept_button = driver.find_element(By.ID, SELECTORS['XPATH']['skatteverk_popup_accept'])
#     pop_up_accept_button.is_displayed()
#     pop_up_accept_button.click()


def foreign_id(driver, SELECTORS):
    interact_with_login_select_button(driver, SELECTORS['ID']['foreign_id'])


def password(driver, SELECTORS, login_details_list):
    interact_with_login_select_button(driver, SELECTORS['ID']['password'])

    # Log in with username and password
    sleep(1)
    username_input = driver.find_element(By.ID, SELECTORS['ID']['username_input'])
    username_input.is_displayed()
    username_input.send_keys(login_details_list[0])

    password_input = driver.find_element(By.ID, SELECTORS['ID']['password_input'])
    password_input.is_displayed()
    password_input.send_keys(login_details_list[1])

    sleep(2)
    login_button = driver.find_element(By.XPATH, SELECTORS['XPATH']['login_button_pass_user'])
    login_button.is_displayed()
    login_button.click()
