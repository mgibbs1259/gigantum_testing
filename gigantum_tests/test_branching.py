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

def test_create_local_branch(driver: selenium.webdriver, *args, **kwargs):
    """
    Test the creation of a branch.

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
    time.sleep(2)
    # wait until container status is stopped
    wait = selenium.webdriver.support.ui.WebDriverWait(driver, 200)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex > .Stopped")))
    # select create branch
    driver.find_element_by_css_selector(".BranchMenu__btn--create").click()
    driver.find_element_by_css_selector("#CreateBranchName").send_keys("branch")
    driver.find_element_by_css_selector(".CreateBranch_navItem > .ButtonLoader").click()
    time.sleep(3)
    # assert that current branch is new branch and local only in upper left
    assert "branch" == driver.find_element_by_css_selector(".BranchMenu__dropdown-text").text, "Expected to be on newly created branch, upper left"
    assert True == True if driver.find_element_by_css_selector(".BranchMenu__status--local") else False, "Expected newly created branch to be local only, upper left"
    # open branch manager
    time.sleep(5)
    driver.find_element_by_css_selector(".BranchMenu__buttons > .BranchMenu__btn--manage").click()
    time.sleep(2)
    # assert that current branch is new branch and local only in branch manager
    assert "branch" == driver.find_element_by_css_selector(".Branches__branchname").text, "Expected to be on newly created branch, branch manager"
    assert True == True if driver.find_element_by_css_selector(".Branches__status--local") else False, "Expected newly created branch to be local only, branch manager"
