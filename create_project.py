# Builtin imports
import logging
import time
import json
import uuid
import sys
import os

# Library imports
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import requests

# Local packages
import testutils


logging.basicConfig(level=logging.INFO)


def test_edge_build_versions(driver: selenium.webdriver):
    """
    Test that the requests edge build version matches the selenium edge build version.

    Args:
        driver
    """
    # get requests edge build version
    r = requests.get("http://localhost:10000/api/ping")
    if r.status_code != 200:
        logging.error("Gigantum is not found at localhost:10000")
        sys.exit(1)
    requests_edge_build_version = json.loads(r.text)
    # get selenium edge build version
    driver.get("http://localhost:10000/api/ping/")
    selenium_edge_build_version = json.loads(driver.find_element_by_css_selector("pre").text)
    # assert edge build versions match
    assert requests_edge_build_version == selenium_edge_build_version, "requests edge build version does not match selenium edge build version"


def test_py2_min_base(driver: selenium.webdriver):
    """
    Test the creation of a project with a python 2 minimal base.

    Args:
        driver
    """
    # project set up
    testutils.log_in(driver)
    time.sleep(2)
    testutils.remove_guide(driver)
    testutils.create_project_without_base(driver)
    time.sleep(2)
    # python 2 minimal base
    testutils.add_py2_min_base(driver)
    # wait until container status is stopped
    wait = selenium.webdriver.support.ui.WebDriverWait(driver, 200)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex>.Stopped")))
    # assert container status is stopped
    container_elts = testutils.ContainerStatus(driver)
    assert container_elts.container_status_stop.is_displayed(), "Expected stopped container"


def test_py3_min_base(driver: selenium.webdriver):
    """
    Test the creation a project with a python 3 minimal base.

    Args:
        driver
    """
    # project set up
    testutils.log_in(driver)
    time.sleep(2)
    testutils.remove_guide(driver)
    testutils.create_project_without_base(driver)
    time.sleep(2)
    # python 3 minimal base
    testutils.add_py3_min_base(driver)
    # wait until container status is stopped
    wait = selenium.webdriver.support.ui.WebDriverWait(driver, 200)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex>.Stopped")))
    # assert container status is stopped
    container_elts = testutils.ContainerStatus(driver)
    assert container_elts.container_status_stop.is_displayed(), "Expected stopped container"


def test_py3_ds_base(driver: selenium.webdriver):
    """
    Test the creation of a project with a python 3 data science base.

    Args:
        driver
    """
    # project set up
    testutils.log_in(driver)
    time.sleep(2)
    testutils.remove_guide(driver)
    testutils.create_project_without_base(driver)
    time.sleep(2)
    # python 3 data science base
    testutils.add_py3_ds_base(driver)
    # wait until container status is stopped
    wait = selenium.webdriver.support.ui.WebDriverWait(driver, 200)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex>.Stopped")))
    # assert container status is stopped
    container_elts = testutils.ContainerStatus(driver)
    assert container_elts.container_status_stop.is_displayed(), "Expected stopped container"


def test_rtidy_base(driver: selenium.webdriver):
    """
    Test the creation of a project with a R Tidyverse base.

    Args:
        driver
    """
    # project set up
    testutils.log_in(driver)
    time.sleep(2)
    testutils.remove_guide(driver)
    testutils.create_project_without_base(driver)
    time.sleep(2)
    # R tidyverse base
    testutils.add_rtidy_base(driver)
    # wait until container status is stopped
    wait = selenium.webdriver.support.ui.WebDriverWait(driver, 200)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex>.Stopped")))
    # assert container status is stopped
    container_elts = testutils.ContainerStatus(driver)
    assert container_elts.container_status_stop.is_displayed(), "Expected stopped container"




    
if __name__ == '__main__':
    username, password = testutils.load_credentials()
    logging.info(f"Using username {username}")

    r = requests.get('http://localhost:10000/api/ping')
    if r.status_code != 200:
        logging.error('Gigantum is not found at localhost:10000')
        sys.exit(1)

    version_info = json.loads(r.text)
    logging.info(f'Gigantum version: {version_info["built_on"]} -- {version_info["revision"][:8]}')

    tests_collection = {}

    # You may edit this as need-be
    #methods_under_test = [test_edge_build_versions, test_py2_min_base, test_py3_min_base, test_py3_ds_base,
    #                      test_rtidy_base, test_valid_custom_docker]
    methods_under_test = [test_pip_packages]

    for test_method in methods_under_test:
        driver = testutils.load_chrome_driver()
        # Run the test in headless mode
        #driver = testutils.load_chrome_driver_headless()
        driver.set_window_size(1440, 1000)
        try:
            logging.info(f"Running test script: {test_method.__name__}")
            result = test_method(driver)
            tests_collection[test_method.__name__] = {'status': 'Pass', 'message': None}
            logging.info(f"Concluded test script: {test_method.__name__}")
        except AssertionError as fail_msg:
            tests_collection[test_method.__name__] = {'status': 'Fail', 'message': fail_msg}
        except Exception as e:
            tests_collection[test_method.__name__] = {'status': 'Error', 'message': e}
            logging.error(f"{test_method.__name__} failed: {e}")
        finally:
            driver.quit()
            time.sleep(2)

    print('-' * 80)
    print('\nTest Report\n')
    for test_name in tests_collection.keys():
        print(f' {tests_collection[test_name]["status"]:6s} :: {test_name} :: {tests_collection[test_name]["message"] or "n/a"}')
