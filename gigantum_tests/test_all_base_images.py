# Builtin imports
import logging
import time

# Library imports
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Local packages
import testutils

logging.basicConfig(level=logging.INFO)

def test_py2_min_base(driver):
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