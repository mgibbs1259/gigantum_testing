import logging
import time
import uuid

import selenium
import testutils

logging.basicConfig(level=logging.INFO)

class Elements:

    # log in
    logIn = ".Login__button"
    gotIt = ".button--green"

    # remove guide
    guide = ".Helper-guide-slider"
    helper = ".Helper__button--side-view"

    # create project
    project = ".btn--import"
    projectTitle = ".CreateLabbook input"
    projectDescription = ".CreateLabbook__description-input"
    projectContinue = "//button[contains(text(), 'Continue')]"

    # all bases
    sideArrow = ".slick-arrow slick-next"
    createProject = ".ButtonLoader "
    projectsPage = ".SideBar__icon"

    # py2 min base
    py2 = "//li[contains(text(), 'python2')]"
    py2Min = "//h6[contains(text(), 'Python2 Minimal')]"

    # py3 min base
    py3 = "//li[contains(text(), 'python3')]"
    py3Min = "//h6[contains(text(), 'Python3 Minimal')]"

    # py3 DS base
    py3DS = "//h6[contains(text(), 'Python3 Data Science Quick-Start')]"

    # RTidy base
    R = "//li[contains(text(), 'R')]"
    RTidy = "//h6[contains(text(), 'R Tidyverse (+ Python3) in Jupyter Quickstart')]"

    # project tabs
    environment = "#environment"

    # all environment
    addPackages = ".PackageDependencies__addPackage"
    packageName = ".PackageDependencies__input"
    versionName = ".PackageDependencies__input--version"
    addButton = ".PackageDependencies__btn--add"
    installPackages = ".PackageDependencies__btn--absolute"

    # pip
    pip = "//li[contains(text(), 'pip (0)')]"
    # conda3
    conda3 = "//li[contains(text(), 'conda3 (0)')]"
    # apt_
    apt = "//li[contains(text(), 'apt (0)')]"

    # custom Docker
    customDockerEdit = ".CustomDockerfile__btn--edit"
    customDockerText = ".CustomDockerfile__textarea"
    customDockerSave = ".CustomDockerfile__content-save-button"

class CreateProject(Elements):

    def __init__(self, driver):
        self.driver = driver

    def log_in(self):
        """ Log into Gigantum """
        logging.info("Logging in")
        # set up browser
        self.driver.get("localhost:10000/projects/local#")
        self.driver.implicitly_wait(15)
        # log in button
        self.driver.find_element_by_css_selector(Elements.logIn).click()
        # username and password
        logging.info("Putting in username and password")
        auth0_elts = testutils.Auth0LoginElements(driver)
        auth0_elts.username_input.click()
        auth0_elts.username_input.send_keys(username)
        auth0_elts.password_input.click()
        auth0_elts.password_input.send_keys(password)
        return self.driver

    def remove_guide(self):
        """ Remove "Got it!", guide, and helper """
        logging.info("Getting rid of 'Got it!'")
        # get rid of Got it!
        self.driver.find_element_by_css_selector(Elements.gotIt).click()
        logging.info("Turning off guide and helper")
        # turn off guide and helper
        self.driver.find_element_by_css_selector(Elements.guide).click()
        self.driver.find_element_by_css_selector(Elements.helper).click()
        return self.driver

    def create_project_no_base(self):
        """ Create a project without a base """
        logging.info("Creating new project")
        # create new project
        self.driver.find_element_by_css_selector(Elements.project).click()
        # create project title
        self.driver.find_element_by_css_selector(Elements.projectTitle).click()
        self.driver.find_element_by_css_selector(Elements.projectTitle).send_keys(testutils.unique_project_name())
        # create project description
        self.driver.find_element_by_css_selector(Elements.projectDescription).click()
        self.driver.find_element_by_css_selector(Elements.projectDescription).send_keys(testutils.unique_project_description())
        # continue creating project
        self.driver.find_element_by_xpath(Elements.projectContinue).click()
        return self.driver

    def py2_min_base(self):
        """ Add a Python2 Minimal base """
        logging.info("Creating new project with Python2 Minimal base")
        # find python2 tab
        self.driver.find_element_by_xpath(Elements.py2).click()
        # select python2 minimal base
        while not self.driver.find_element_by_xpath(Elements.py2Min).is_displayed():
            logging.info("Searching for Python2 Minimal base...")
            self.driver.find_element_by_css_selector(Elements.sideArrow).click()
        self.driver.find_element_by_xpath(Elements.py2Min).click()
        self.driver.find_element_by_css_selector(Elements.createProject).click()
        return self.driver

    def py3_min_base(self):
        """ Add a Python3 Minimal base """
        logging.info("Creating new project with Python3 Minimal base")
        # find python3 tab
        self.driver.find_element_by_xpath(Elements.py3).click()
        # select python3 minimal base
        while not self.driver.find_element_by_xpath(Elements.py3Min).is_displayed():
            logging.info("Searching for Python3 Minimal base...")
            self.driver.find_element_by_css_selector(Elements.sideArrow).click()
        self.driver.find_element_by_xpath(Elements.py3Min).click()
        self.driver.find_element_by_css_selector(Elements.createProject).click()
        return self.driver

    def py3_DS_base(self):
        """ Add a Python3 Data Science Quick-start base """
        logging.info("Creating new project with Python3 Data Science Quick-start base")
        # find python3 tab
        self.driver.find_element_by_xpath(Elements.py3).click()
        # select python3 data science base
        while not self.driver.find_element_by_xpath(Elements.py3DS).is_displayed():
            logging.info("Searching for Python3 Data Science Quick-start base...")
            self.driver.find_element_by_css_selector(Elements.sideArrow).click()
        self.driver.find_element_by_xpath(Elements.py3DS).click()
        self.driver.find_element_by_css_selector(Elements.createProject).click()
        return self.driver

    def RTidy_base(self):
        """ Add a R Tidyverse base """
        logging.info("Creating new project with R Tidyverse base")
        # find R tab
        self.driver.find_element_by_xpath(Elements.R).click()
        # select R Tidyverse base
        while not self.driver.find_element_by_xpath(Elements.RTidy).is_displayed():
            logging.info("Searching for R Tidyverse base...")
            self.driver.find_element_by_css_selector(Elements.sideArrow).click()
        self.driver.find_element_by_xpath(Elements.RTidy).click()
        self.driver.find_element_by_css_selector(Elements.createProject).click()
        return self.driver

    def container_status(self):
        """ Check whether container is building, running, or stopped """
        #implement


    def pip_packages(self):
        """ Add pip packages """
        logging.info("Adding pip packages")
        # find environment tab
        self.driver.find_element_by_css_selector(Elements.environment).click()
        # add pip packages
        self.driver.find_element_by_css_selector(Elements.addPackages).click()
        for pip_pack in ['pandas', 'numpy', 'matplotlib']:
            self.driver.find_element_by_css_selector(Elements.packageName).send_keys(pip_pack)
            time.sleep(3)
            self.driver.find_element_by_css_selector(Elements.addButton).click()
            time.sleep(3)
        self.driver.find_element_by_css_selector(Elements.installPackages).click()
        return self.driver

    def conda3_packages(self):
        """ Add conda3 packages """
        logging.info("Adding conda3 packages")
        # find environment tab
        self.driver.find_element_by_css_selector(Elements.environment).click()
        # find conda3 tab
        self.driver.find_element_by_css_selector(Elements.conda3).click()
        # add conda3 packages
        self.driver.find_element_by_css_selector(Elements.addPackages).click()
        for conda_pack in ['pyflakes', 'odo']:
            self.driver.find_element_by_css_selector(Elements.packageName).send_keys(conda_pack)
            time.sleep(3)
            self.driver.find_element_by_css_selector(Elements.addButton).click()
            time.sleep(3)
        self.driver.find_element_by_css_selector(Elements.installPackages).click()
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
    driver.find_element_by_css_selector(Elements.projectsPage).click()
    # python 3 minimal base
    test_project.create_project_no_base()
    test_project.py3_min_base()
    time.sleep(15)
    driver.find_element_by_css_selector(Elements.projectsPage).click()
    # python 3 data science base
    test_project.create_project_no_base()
    test_project.py3_DS_base()
    time.sleep(15)
    driver.find_element_by_css_selector(Elements.projectsPage).click()
    # R Tidyverse base
    test_project.create_project_no_base()
    test_project.RTidy_base()
    time.sleep(15)
    driver.find_element_by_css_selector(Elements.projectsPage).click()

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
    test_project.pip_packages()
    time.sleep(10)
    # conda3 packages
    test_project.conda3_packages()
    time.sleep(30)

if __name__ == '__main__':
    try:
        # set driver
        driver = testutils.load_chrome_driver()
        # username and password
        username, password = testutils.load_credentials()
        logging.info(f"Using username {username}")
        #all_bases(driver)
        all_packages(driver)
    finally:
        # cleanly close driver
        logging.info("Closing driver")
        driver.close()

