# Builtin imports
import logging
import time

# Library imports
import selenium

# Local packages
from testutils import elements
from testutils import testutils


# create project
def log_in(driver: selenium.webdriver):
    """
    Log in to Gigantum.

    Args:
        driver
    """
    driver.get("http://localhost:10000/projects/local#")
    logging.info("Logging in")
    auth0_elts = elements.Auth0LoginElements(driver)
    auth0_elts.login_green_button.click()
    time.sleep(2)
    username,password = testutils.load_credentials()
    auth0_elts.username_input.click()
    auth0_elts.username_input.send_keys(username)
    auth0_elts.password_input.click()
    auth0_elts.password_input.send_keys(password)
    try:
        auth0_elts.login_grey_button.click()
    except:
        pass


def remove_guide(driver: selenium.webdriver):
    """
    Remove'Got it!', guide, and helper.

    Args:
        driver
    """
    logging.info("Getting rid of 'Gotit!'")
    guide_elts = elements.GuideElements(driver)
    guide_elts.got_it_button.click()
    logging.info("Turning off guide and helper")
    guide_elts.guide_button.click()
    guide_elts.helper_button.click()


def create_project_without_base(driver: selenium.webdriver):
    """
    Create a project without a base.

    Args:
        driver
    """
    logging.info("Creating a project without a base")
    project_elts = elements.AddProjectElements(driver)
    project_elts.create_new_button.click()
    project_elts.project_title_input.click()
    project_elts.project_title_input.send_keys(testutils.unique_project_name())
    project_elts.project_description_input.click()
    project_elts.project_description_input.send_keys(testutils.unique_project_description())
    project_elts.project_continue_button.click()


# bases
def add_py2_min_base(driver: selenium.webdriver):
    """
    Add a Python2 Minimal base.

    Args:
        driver
    """
    logging.info("Creating new project with Python2 Minimal base")
    py2_base_elts = elements.AddProjectBaseElements(driver)
    try:
        py2_base_elts.py2_tab_button.click()
    except:
        pass
    while not py2_base_elts.py2_minimal_base_button.is_displayed():
        logging.info("Searching for Python2 Minimal base...")
        py2_base_elts.arrow_button.click()
    py2_base_elts.py2_minimal_base_button.click()
    py2_base_elts.create_project_button.click()


def add_py3_min_base(driver: selenium.webdriver):
    """
    Add a Python3 Minimal base.

    Args:
        driver
    """
    logging.info("Creating new project with Python3 Minimal base")
    py3_base_elts = elements.AddProjectBaseElements(driver)
    try:
        py3_base_elts.py3_tab_button.click()
    except:
        pass
    while not py3_base_elts.py3_minimal_base_button.is_displayed():
        logging.info("Searching for Python3 Minimal base...")
        py3_base_elts.arrow_button.click()
    py3_base_elts.py3_minimal_base_button.click()
    py3_base_elts.create_project_button.click()


def add_py3_ds_base(driver: selenium.webdriver):
    """
    Add a Python3 Data Science Quick-start base.

    Args:
        driver
    """
    logging.info("Creating new project with Python3 Data Science Quick-start base")
    py3_base_elts = elements.AddProjectBaseElements(driver)
    try:
        py3_base_elts.py3_tab_button.click()
    except:
        pass
    while not py3_base_elts.py3_minimal_base_button.is_displayed():
        logging.info("Searching for Python3 Data Science Quick-start base...")
        py3_base_elts.arrow_button.click()
    py3_base_elts.py3_data_science_base_button.click()
    py3_base_elts.create_project_button.click()


def add_rtidy_base(driver: selenium.webdriver):
    """
    Add a R Tidyverse base.

    Args:
        driver
    """
    logging.info("Creating new project with R Tidyverse base")
    r_base_elts = elements.AddProjectBaseElements(driver)
    try:
        r_base_elts.r_tab_button.click()
    except:
        pass
    while not r_base_elts.r_tidyverse_base_button.is_displayed():
        logging.info("Searching for R Tidyverse base...")
        r_base_elts.arrow_button.click()
    r_base_elts.r_tidyverse_base_button.click()
    r_base_elts.create_project_button.click()


# environment
def add_pip_package(driver: selenium.webdriver):
    """
    Add pip packages.

    Args:
        driver
    """
    logging.info("Adding pip packages")
    environment = elements.EnvironmentElements(driver)
    environment.environment_tab_button.click()
    time.sleep(3)
    driver.execute_script("window.scrollBy(0, -400);")
    driver.execute_script("window.scrollBy(0, 400);")
    environment.add_packages_button.click()
    pip_list = ["pandas", "numpy", "matplotlib"]
    for pip_pack in pip_list:
        environment.package_name_input.send_keys(pip_pack)
        time.sleep(3)
        environment.add_button.click()
        time.sleep(3)
    environment.install_packages_button.click()


def add_conda3_package(driver: selenium.webdriver):
    """
    Add conda3 packages.

    Args:
        driver
    """
    logging.info("Adding conda3 package")
    environment = elements.EnvironmentElements(driver)
    environment.environment_tab_button.click()
    time.sleep(3)
    environment.conda3_tab_button.click()
    driver.execute_script("window.scrollBy(0, -400);")
    driver.execute_script("window.scrollBy(0, 400);")
    environment.add_packages_button.click()
    environment.package_name_input.send_keys("pyflakes")
    time.sleep(3)
    environment.add_button.click()
    time.sleep(3)
    environment.install_packages_button.click()


def add_apt_package(driver: selenium.webdriver):
    """
    Add apt packages.

    Args:
        driver
    """
    logging.info("Adding apt packages")
    environment = elements.EnvironmentElements(driver)
    environment.environment_tab_button.click()
    time.sleep(3)
    environment.apt_tab_button.click()
    driver.execute_script("window.scrollBy(0, -400);")
    driver.execute_script("window.scrollBy(0, 400);")
    environment.add_packages_button.click()
    environment.package_name_input.send_keys("apache2")
    time.sleep(3)
    environment.add_button.click()
    time.sleep(3)
    environment.install_packages_button.click()


def add_valid_custom_docker(driver: selenium.webdriver):
    """
    Add valid custom Docker.

    Args:
        driver
    """
    logging.info("Adding valid custom Docker")
    environment = elements.EnvironmentElements(driver)
    environment.environment_tab_button.click()
    driver.execute_script("window.scrollBy(0, 600);")
    environment.custom_docker_edit_button.click()
    environment.custom_docker_text_input.send_keys(testutils.custom_docker_instructions())
    driver.execute_script("window.scrollBy(0, 300);")
    environment.custom_docker_save_button.click()
