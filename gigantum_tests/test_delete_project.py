# Builtin imports
import logging
import time
import os
from pathlib import Path

# Library imports
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Local packages
import testutils


def test_delete_project(driver: selenium.webdriver, *args, **kwargs):
    """
        Test that deleting a project in Gigantum deletes it from the file system.

        Args:
            driver
    """
    # project set up
    testutils.log_in(driver)
    time.sleep(2)
    testutils.remove_guide(driver)
    time.sleep(2)
    testutils.create_project_without_base(driver)
    # python 3 minimal base
    testutils.add_py3_min_base(driver)
    wait = WebDriverWait(driver, 200)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex>.Stopped")))
    # obtain project title
    full_project_title = driver.find_element_by_css_selector(".LabbookHeader__section--title").text
    project_title = full_project_title[full_project_title.index("/") + 1:]
    # check that project path exists on file system
    username, password = testutils.load_credentials()
    username = username.strip()
    project_path = os.path.join(str(Path.home()), f"gigantum/{username}/{username}/labbooks", project_title)
    before_delete = os.path.exists(project_path)
    assert before_delete == True, "Project not found in file system"
    # delete project
    driver.find_element_by_css_selector(".BranchMenu__btn").click()
    time.sleep(1)
    driver.find_element_by_css_selector(".BranchMenu__item--delete").click()
    time.sleep(1)
    driver.find_element_by_css_selector("#deleteInput").send_keys(project_title)
    driver.find_element_by_css_selector(".DeleteLabbook > .ButtonLoader").click()
    # check that project path does not exist on file system
    time.sleep(5)
    after_delete = os.path.exists(project_path)
    assert before_delete != after_delete, "Project not deleted from file system"


