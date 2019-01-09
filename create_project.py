# Builtin imports
import logging
import time
import json
import uuid
import sys

# Library imports
import selenium
import requests

# Local packages
import testutils

logging.basicConfig(level=logging.INFO)


class CreateProject():

    def __init__(self, driver):
        self.driver = driver

    def log_in(self):
        """ Log into Gigantum """
        logging.info("Logging in")
        # set up browserq
        self.driver.get("http://localhost:10000/projects/local#")
        self.driver.implicitly_wait(15)
        # log in button
        auth0_elts = testutils.Auth0LoginElements(driver)
        auth0_elts.login_green_button.click()
        # username and password
        time.sleep(2)
        logging.info("Putting in username and password")
        auth0_elts.username_input.click()
        auth0_elts.username_input.send_keys(username)
        auth0_elts.password_input.click()
        auth0_elts.password_input.send_keys(password)
        # log in with credentials
        try:
            auth0_elts.login_grey_button.click()
        except:
            pass
        return self.driver

    def remove_guide(self):
        """ Remove "Got it!", guide, and helper """
        logging.info("Getting rid of 'Got it!'")
        guide_elts = testutils.GuideElements(driver)
        # get rid of Got it!
        time.sleep(2)
        guide_elts.got_it_button.click()
        logging.info("Turning off guide and helper")
        # turn off guide and helper
        guide_elts.guide_button.click()
        guide_elts.helper_button.click()
        return self.driver

    def create_project_no_base(self):
        """ Create a project without a base """
        logging.info("Creating new project")
        proj_elts = testutils.AddProjectElements(driver)
        # create new project
        proj_elts.create_new_button.click()
        # create project title
        proj_elts.project_title_input.click()
        proj_elts.project_title_input.send_keys(testutils.unique_project_name())
        # create project description
        proj_elts.project_description_input.click()
        proj_elts.project_description_input.send_keys(testutils.unique_project_description())
        # continue creating project
        proj_elts.project_continue_button.click()
        return self.driver

    def py2_min_base(self):
        """ Add a Python2 Minimal base """
        logging.info("Creating new project with Python2 Minimal base")
        py2_base_elts = testutils.AddProjectBaseElements(driver)
        # find python2 tab
        try:
            py2_base_elts.py2_tab_button.click()
        except:
            pass
        # select python2 minimal base
        while not py2_base_elts.py2_minimal_base_button.is_displayed():
            logging.info("Searching for Python2 Minimal base...")
            py2_base_elts.arrow_button.click()
        py2_base_elts.py2_minimal_base_button.click()
        py2_base_elts.create_project_button.click()
        return self.driver

    def py3_min_base(self):
        """ Add a Python3 Minimal base """
        logging.info("Creating new project with Python3 Minimal base")
        py3_base_elts = testutils.AddProjectBaseElements(driver)
        # find python3 tab
        try:
            py3_base_elts.py3_tab_button.click()
        except:
            pass
        # select python3 minimal base
        while not py3_base_elts.py3_minimal_base_button.is_displayed():
            logging.info("Searching for Python3 Minimal base...")
            py3_base_elts.arrow_button.click()
        py3_base_elts.py3_minimal_base_button.click()
        py3_base_elts.create_project_button.click()
        return self.driver

    def py3_DS_base(self):
        """ Add a Python3 Data Science Quick-start base """
        logging.info("Creating new project with Python3 Data Science Quick-start base")
        py3_base_elts = testutils.AddProjectBaseElements(driver)
        # find python3 tab
        try:
            py3_base_elts.py3_tab_button.click()
        except:
            pass
        # select python3 data science base
        while not py3_base_elts.py3_minimal_base_button.is_displayed():
            logging.info("Searching for Python3 Data Science Quick-start base...")
            py3_base_elts.arrow_button.click()
        py3_base_elts.py3_data_science_base_button.click()
        py3_base_elts.create_project_button.click()
        return self.driver

    def RTidy_base(self):
        """ Add a R Tidyverse base """
        logging.info("Creating new project with R Tidyverse base")
        R_base_elts = testutils.AddProjectBaseElements(driver)
        # find R tab
        try:
            R_base_elts.R_tab_button.click()
        except:
            pass
        # select R Tidyverse base
        while not R_base_elts.R_tidyverse_base_button.is_displayed():
            logging.info("Searching for R Tidyverse base...")
            R_base_elts.arrow_button.click()
        R_base_elts.R_tidyverse_base_button.click()
        R_base_elts.create_project_button.click()
        return self.driver

    def container_status(self):
        """ Check whether container is building, running, or stopped """
        #implement


    def pip_package(self):
        """ Add pip packages """
        logging.info("Adding pip packages")
        environment = testutils.EnvironmentElements(driver)
        # find environment tab
        environment.environment_tab_button.click()
        time.sleep(3)
        # add pip packages
        self.driver.execute_script("window.scrollBy(0, -400);")
        self.driver.execute_script("window.scrollBy(0, 400);")
        environment.add_packages_button.click()
        for pip_pack in ['pandas', 'numpy', 'matplotlib']:
            environment.package_name_input.send_keys(pip_pack)
            time.sleep(4)
            environment.add_button.click()
            time.sleep(4)
        environment.install_packages_button.click()
        return self.driver

    def conda3_package(self):
        """ Add conda3 package """
        logging.info("Adding conda3 package")
        environment = testutils.EnvironmentElements(driver)
        # find environment tab
        environment.environment_tab_button.click()
        # find conda3 tab
        environment.conda3_tab_button.click()
        # add conda3 packages
        environment.add_packages_button.click()
        self.driver.execute_script("window.scrollBy(0, -400);")
        self.driver.execute_script("window.scrollBy(0, 400);")
        environment.package_name_input.send_keys('pyflakes')
        time.sleep(4)
        environment.add_button.click()
        time.sleep(4)
        environment.install_packages_button.click()
        return self.driver

    def apt_package(self):
        """ Add apt package """
        logging.info("Adding apt packages")
        environment = testutils.EnvironmentElements(driver)
        # find environment tab
        environment.environment_tab_button.click()
        # find apt tab
        environment.apt_tab_button.click()
        # add apt packages
        environment.add_packages_button.click()
        self.driver.execute_script("window.scrollBy(0, -400);")
        self.driver.execute_script("window.scrollBy(0, 400);")
        environment.package_name_input.send_keys('apache2')
        time.sleep(4)
        environment.add_button.click()
        time.sleep(4)
        environment.install_packages_button.click()
        return self.driver

    def custom_docker_instructions(self):
        """ Add custom Docker instructions """
        logging.info("Adding custom Docker instructions")
        environment = testutils.EnvironmentElements(driver)
        # find environment tab
        environment.environment_tab_button.click()
        # add custom docker instructions
        self.driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(2)
        environment.custom_docker_edit_button.click()
        environment.custom_docker_text_input.send_keys(testutils.custom_docker_instructions())
        self.driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(2)
        environment.custom_docker_save_button.click()
        return self.driver

#test scripts


def all_bases(driver):
    """ Create a project for each base """
    # set up
    test_project = CreateProject(driver)
    test_project.log_in()
    test_project.remove_guide()
    test_project.create_project_no_base()
    # python 2 minimal base
    test_project.py2_min_base()
    time.sleep(15)
    environment = testutils.AddProjectBaseElements(driver)
    environment.projects_page_button.click()
    time.sleep(15)
    # python 3 minimal base
    test_project.create_project_no_base()
    test_project.py3_min_base()
    time.sleep(15)
    environment.projects_page_button.click()
    time.sleep(15)
    # python 3 data science base
    test_project.create_project_no_base()
    test_project.py3_DS_base()
    time.sleep(15)
    environment.projects_page_button.click()
    time.sleep(30)
    # R Tidyverse base
    test_project.create_project_no_base()
    test_project.RTidy_base()
    time.sleep(15)
    environment.projects_page_button.click()
    time.sleep(5)


def all_packages(driver):
    """ Install packages with apt, pip, conda3 """
    # set up
    test_project = CreateProject(driver)
    test_project.log_in()
    test_project.remove_guide()
    test_project.create_project_no_base()
    # python 3 minimal base
    test_project.py3_min_base()
    time.sleep(15)
    # pip packages
    test_project.pip_package()
    time.sleep(30)
    assert driver.find_element_by_css_selector(".Stopped").text == "Stopped", "Expected container status stopped"

    # conda3 package
    test_project.conda3_package()
    time.sleep(120)
    assert driver.find_element_by_css_selector(".Stopped").text == "Stopped", "Expected container status stopped"

    # apt package
    test_project.apt_package()
    time.sleep(60)
    assert driver.find_element_by_css_selector(".Stopped").text == "Stopped", "Expected container status stopped"


def custom_docker(driver):
    # set up
    test_project = CreateProject(driver)
    test_project.log_in()
    test_project.remove_guide()
    test_project.create_project_no_base()
    # python 3 minimal base
    test_project.py3_min_base()
    time.sleep(15)
    # custom docker instructions
    test_project.custom_docker_instructions()
    time.sleep(10)


def test_example_success(driver):
    my_sum = 1 + 1
    assert my_sum == 2, "Expected sum to be 2"
    my_product = 3 * 4


def test_example_failure(driver):
    my_sum = 1 + 1
    assert my_sum == 3, "Expected sum to be 3"


def test_example_error(driver):
    my_sum = 1 + 1
    
    # The following line will cause an exception
    my_quotient = 3 / 0

    # The following lines will never be reached
    my_product = 4 + 5
    

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
    methods_under_test = [test_example_success, test_example_failure, test_example_error, all_bases, all_packages, custom_docker]

    for test_method in methods_under_test:
        driver = testutils.load_chrome_driver()
        driver.set_window_size(1200, 1000)
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
            driver.close()
            time.sleep(2)

    print('-' * 80)
    print('\nTest Report\n')
    for test_name in tests_collection.keys():
        print(f' {tests_collection[test_name]["status"]:6s} :: {test_name} :: {tests_collection[test_name]["message"] or "n/a"}')

