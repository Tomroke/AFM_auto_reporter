from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

def click_button(driver, by, selector, initial_duration=1, final_duration=0):
    # Wait a second to let the elements load or a custom duration.
    sleep(initial_duration)

    # Find element, verify that it is displayed and click it.
    button = driver.find_element(by, selector)
    button.is_displayed()
    button.click()

    # Wait another second to let the elements load or a custom duration
    # The custom duration can either be the first duration or a new one.
    if final_duration != 0:
        sleep(final_duration)
    else:
        sleep(initial_duration)

def assert_element_text(driver, by, selector, text, initial_duration=1, final_duration=0):
    # Wait a second to let the elements load or a custom duration.
    sleep(initial_duration)

    # Find element, verify that it is displayed and assert that it contains the right text.
    element = driver.find_element(by, selector)
    element.is_displayed()
    assert element.text == text

    # Wait another second to let the elements load or a custom duration
    # The custom duration can either be the first duration or a new one.
    if final_duration != None:
        sleep(final_duration)
    else:
        sleep(initial_duration)

def scroll_click_element(driver, by, selector, initial_duration=1, final_duration=0):
    # Wait a second to let the elements load or a custom duration.
    sleep(initial_duration)

    # Find element, scroll to it, verify that it is displayed and click it.
    button = driver.find_element(by, selector)
    ActionChains(driver)\
        .scroll_to_element(button)\
        .perform()
    button.is_displayed()
    button.click()

    # Wait another second to let the elements load or a custom duration
    # The custom duration can either be the first duration or a new one.
    if final_duration != None:
        sleep(final_duration)
    else:
        sleep(initial_duration)

def scroll_write_element(driver, by, selector, text, initial_duration=1, final_duration=0):
    # Wait a second to let the elements load or a custom duration.
    sleep(initial_duration)

    # Find element, scroll to it, verify that it is displayed and enter the required text.
    input = driver.find_element(by, selector)
    ActionChains(driver)\
        .scroll_to_element(input)\
        .perform()
    input.is_displayed()
    input.send_keys(text)

    # Wait another second to let the elements load or a custom duration
    # The custom duration can either be the first duration or a new one.
    if final_duration != None:
        sleep(final_duration)
    else:
        sleep(initial_duration)
