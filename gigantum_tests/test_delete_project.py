# Builtin imports
import logging
import time

# Library imports
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Local packages
import testutils


def test_delete_project(driver: selenium.webdriver, *args, **kwargs):
    testutils.log_in(driver)
    time.sleep(2)
    testutils.remove_guide(driver)
    time.sleep(2)
    testutils.create_project_without_base(driver)
    testutils.add_py3_min_base(driver)
    wait = WebDriverWait(driver, 200)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex>.Stopped")))
    #grab project title
    project_title = driver.find_element_by_css_selector(".LabbookHeader__section--title").text
    symbol_index = project_title.index("/") + 1
    project_title = project_title[symbol_index:]
    print(project_title)
    driver.find_element_by_css_selector(".BranchMenu__btn").click()
    time.sleep(1)
    driver.find_element_by_css_selector(".BranchMenu__item--delete").click()
    time.sleep(1)
    driver.find_element_by_css_selector("#deleteInput").send_keys(project_title)
    driver.find_element_by_css_selector(".DeleteLabbook > .ButtonLoader").click()




