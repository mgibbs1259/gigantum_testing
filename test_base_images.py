# Builtin imports
import logging

# Library imports
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Local packages
import testutils


logging.basicConfig(level=logging.INFO)


def test_python2_minimal_base():
    """Test the creation of a project with a Python2 Minimal base, and assert that the container is 'Stopped'."""
    test_project = CreateProject(driver)
    test_project.log_in()
    test_project.remove_guide()
    test_project.create_project_no_base()
    test_project.py2_min_base()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex>.Stopped")))
    assert driver.find_element_by_css_selector(".flex>.Stopped").is_displayed(), "Container is not 'Stopped'"


def test_python3_minimal_base():
    """Test the creation of a project with a Python3 Minimal base, and assert that the container is 'Stopped'."""
    test_project = CreateProject(driver)
    test_project.log_in()
    test_project.remove_guide()
    test_project.create_project_no_base()
    test_project.py3_min_base()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex>.Stopped")))
    assert driver.find_element_by_css_selector(".flex>.Stopped").is_displayed(), "Container is not 'Stopped'"


def test_python3_data_science_base():
    """Test the creation of a project with a Python3 Data Science base, and assert that the container is 'Stopped'."""
    test_project = CreateProject(driver)
    test_project.log_in()
    test_project.remove_guide()
    test_project.create_project_no_base()
    test_project.py3_DS_base()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex>.Stopped")))
    assert driver.find_element_by_css_selector(".flex>.Stopped").is_displayed(), "Container is not 'Stopped'"


def test_