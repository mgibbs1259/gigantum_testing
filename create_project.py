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
            time.sleep(3)
            environment.add_button.click()
            time.sleep(3)
        environment.install_packages_button.click()
        return self.driver

    def conda3_package(self):
        """ Add conda3 package """
        logging.info("Adding conda3 package")
        environment = testutils.EnvironmentElements(driver)
        # find environment tab
        environment.environment_tab_button.click()
        time.sleep(3)
        # find conda3 tab
        environment.conda3_tab_button.click()
        # add conda3 packages
        self.driver.execute_script("window.scrollBy(0, -400);")
        self.driver.execute_script("window.scrollBy(0, 400);")
        environment.add_packages_button.click()
        environment.package_name_input.send_keys('pyflakes')
        time.sleep(3)
        environment.add_button.click()
        time.sleep(3)
        environment.install_packages_button.click()
        return self.driver

    def apt_package(self):
        """ Add apt package """
        logging.info("Adding apt packages")
        environment = testutils.EnvironmentElements(driver)
        # find environment tab
        environment.environment_tab_button.click()
        time.sleep(3)
        # find apt tab
        environment.apt_tab_button.click()
        # add apt packages
        self.driver.execute_script("window.scrollBy(0, -400);")
        self.driver.execute_script("window.scrollBy(0, 400);")
        environment.add_packages_button.click()
        environment.package_name_input.send_keys('apache2')
        time.sleep(3)
        environment.add_button.click()
        time.sleep(3)
        environment.install_packages_button.click()
        return self.driver

    def custom_docker_instructions(self):
        """ Add custom Docker instructions """
        logging.info("Adding custom Docker instructions")
        environment = testutils.EnvironmentElements(driver)
        # find environment tab
        environment.environment_tab_button.click()
        # add custom docker instructions
        self.driver.execute_script("window.scrollBy(0, 600);")
        environment.custom_docker_edit_button.click()
        time.sleep(2)
        environment.custom_docker_text_input.send_keys(testutils.custom_docker_instructions())
        self.driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(2)
        environment.custom_docker_save_button.click()
        return self.driver


# test scripts


def test_all_bases(driver):
    """ Create a project for each base """
    # set up
    test_project = CreateProject(driver)
    test_project.log_in()
    test_project.remove_guide()
    test_project.create_project_no_base()
    # python 2 minimal base
    test_project.py2_min_base()
    # wait
    wait = WebDriverWait(driver, 200)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex>.Stopped")))
    assert driver.find_element_by_css_selector(".flex>.Stopped").is_displayed(), "Expected stopped container"
    # projects page
    environment = testutils.AddProjectBaseElements(driver)
    environment.projects_page_button.click()
    # python 3 minimal base
    test_project.create_project_no_base()
    test_project.py3_min_base()
    # wait
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex>.Stopped")))
    assert driver.find_element_by_css_selector(".flex>.Stopped").is_displayed(), "Expected stopped container"
    # projects page
    environment.projects_page_button.click()
    # python 3 data science base
    test_project.create_project_no_base()
    test_project.py3_DS_base()
    # wait
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex>.Stopped")))
    assert driver.find_element_by_css_selector(".flex>.Stopped").is_displayed(), "Expected stopped container"
    # projects page
    environment.projects_page_button.click()
    # R Tidyverse base
    test_project.create_project_no_base()
    test_project.RTidy_base()
    # wait
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex>.Stopped")))
    assert driver.find_element_by_css_selector(".flex>.Stopped").is_displayed(), "Expected stopped container"


def test_pip_packages(driver):
    """ Install packages with pip """
    # set up
    test_project = CreateProject(driver)
    test_project.log_in()
    test_project.remove_guide()
    test_project.create_project_no_base()
    # python 3 minimal base
    test_project.py3_min_base()
    # wait
    wait = WebDriverWait(driver, 200)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex>.Stopped")))
    # pip packages
    test_project.pip_package()
    # wait
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex>.Stopped")))
    assert driver.find_element_by_css_selector(".flex>.Stopped").is_displayed(), "Expected stopped container"


    '''#check pip packages version
    time.sleep(5)
    driver.find_element_by_css_selector(".ContainerStatus__selected-tool").click()
    time.sleep(30)
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[1])
    print("switch success")
    time.sleep(10)
    driver.find_element_by_css_selector("[data-category = Notebook]").click()
    time.sleep(10)
    driver.find_element_by_css_selector(".CodeMirror-line").click().send_keys("import pandas")
    time.sleep(20)

    # conda3 package
    test_project.conda3_package()
    # wait 
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex>.Stopped")))
    assert driver.find_element_by_css_selector(".flex>.Stopped").is_displayed(), "Expected stopped container"

    # apt package
    test_project.apt_package()
    # wait 
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex>.Stopped")))
    assert driver.find_element_by_css_selector(".flex>.Stopped").is_displayed(), "Expected stopped container"'''


def test_valid_custom_docker(driver):
    # set up
    test_project = CreateProject(driver)
    test_project.log_in()
    test_project.remove_guide()
    test_project.create_project_no_base()
    # python 3 minimal base
    test_project.py3_min_base()
    # wait
    wait = WebDriverWait(driver, 200)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex>.Stopped")))
    # custom docker instructions
    test_project.custom_docker_instructions()
    # wait
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex>.Stopped")))
    assert driver.find_element_by_css_selector(".flex>.Stopped").is_displayed(), "Expected stopped container"
    assert "Successfully tagged" in driver.find_element_by_css_selector(".Footer__message-title").text, "Expected 'Successfully tagged' in footer"


def validate_edge_build_version(driver):
    """ Compare selenium and requests edge build version """
    # set up
    CreateProject(driver)
    # switch to api/ping
    driver.get("http://localhost:10000/api/ping/")
    selenium_edge_build_version = json.loads(driver.find_element_by_css_selector("pre").text)
    assert selenium_edge_build_version == version_info, "selenium does not match requests edge build version"


def test_drag_drop_file_local_to_browser(driver):
    # set up
    test_project = CreateProject(driver)
    test_project.log_in()
    test_project.remove_guide()
    test_project.create_project_no_base()
    # python 3 minimal base
    test_project.py3_min_base()
    # wait
    wait = WebDriverWait(driver, 200)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex>.Stopped")))
    # switch to input data tab
    driver.find_element_by_css_selector("#inputData").click()
    time.sleep(3)
    # drag and drop from local to browser
    js_script = """for (var b = arguments[0], k = arguments[1], l = arguments[2], c = b.ownerDocument, m = 0;;) {
        var e = b.getBoundingClientRect(),
            g = e.left + (k || e.width / 2),
            h = e.top + (l || e.height / 2),
            f = c.elementFromPoint(g, h);
        if (f && b.contains(f)) break;
        if (1 < ++m) throw b = Error('Element not interractable'), b.code = 15, b;
        b.scrollIntoView({
            behavior: 'instant',
            block: 'center',
            inline: 'center'
        })
        }
    var a = c.createElement('INPUT');
    a.setAttribute('type', 'file');
    a.setAttribute('style', 'position:fixed;z-index:2147483647;left:0;top:0;');
    a.onchange = function() {
        var b = {
            effectAllowed: 'all',
            dropEffect: 'none',
            types: ['Files'],
            files: this.files,
            setData: function() {},
            getData: function() {},
            clearData: function() {},
            setDragImage: function() {}
        };
        window.DataTransferItemList && (b.items = Object.setPrototypeOf([Object.setPrototypeOf({
            kind: 'file',
            type: this.files[0].type,
            file: this.files[0],
            getAsFile: function() {
                return this.file
            },
            getAsEntry: function() {
                console.log(this, this.file, b)
                return this.file; // {"file": this.file, "entry": { "fullpath": file.name, "file": file, "name": file.name }}
            },
            getAsString: function(b) {
                var a = new FileReader;
                a.onload = function(a) {
                    b(a.target.result)
                };
                a.readAsText(this.file)
            }
        }, DataTransferItem.prototype)], DataTransferItemList.prototype));
        Object.setPrototypeOf(b, DataTransfer.prototype);
        ['dragenter', 'dragover', 'drop'].forEach(function(a) {
            var d = c.createEvent('DragEvent');
            d.initMouseEvent(a, !0, !0, c.defaultView, 0, 0, 0, g, h, !1, !1, !1, !1, 0, null);
            Object.setPrototypeOf(d, null);
            d.dataTransfer = b;
            Object.setPrototypeOf(d, DragEvent.prototype);
            f.dispatchEvent(d)
        });
        a.parentElement.removeChild(a)
    };
    c.documentElement.appendChild(a);
    a.getBoundingClientRect();
    return a;"""
    drop_target = driver.find_element_by_css_selector(".FileBrowser")
    file_path = os.path.join(os.getcwd(), 'testmaterial/file-3000000b.rando')
    drag_and_drop_file(drop_target, file_path, js_script)
    time.sleep(3)
    flat_dir_path = os.path.join(os.getcwd(), 'testmaterial/flatdir')
    drag_and_drop_file(drop_target, flat_dir_path, js_script)
    time.sleep(60)


def drag_and_drop_file(drop_target, path, js_script):
    #driver = drop_target.parent
    file_input = driver.execute_script(js_script, drop_target, 0, 0)
    file_input.send_keys(path)

#drag_and_drop_file(drop_target, path)

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
    methods_under_test = [drag_drop_file_local_to_browser]

    for test_method in methods_under_test:
        driver = testutils.load_chrome_driver()
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
            #driver.close()
            time.sleep(2)

    print('-' * 80)
    print('\nTest Report\n')
    for test_name in tests_collection.keys():
        print(f' {tests_collection[test_name]["status"]:6s} :: {test_name} :: {tests_collection[test_name]["message"] or "n/a"}')

