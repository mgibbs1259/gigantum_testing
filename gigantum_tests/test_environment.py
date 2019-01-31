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


def test_pip_packages(driver: selenium.webdriver):
    """
    Test that pip packages install successfully.

    Args:
        driver
    """
    # project set up
    testutils.log_in(driver)
    time.sleep(2)
    testutils.remove_guide(driver)
    time.sleep(2)
    testutils.create_project_without_base(driver)
    time.sleep(2)
    # python 3 minimal base
    testutils.add_py3_min_base(driver)
    # wait
    wait = WebDriverWait(driver, 200)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex>.Stopped")))
    # pip packages
    testutils.add_pip_package(driver)
    # wait until container status is stopped
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex>.Stopped")))
    assert testutils.is_container_stopped(driver), "Expected stopped container"


    # check package version from environment
    package_info = driver.find_element_by_css_selector(".PackageDependencies__table-container").text
    # parse the string to a list and extract information of package names and versions
    package_list = package_info.split("\n")[1::2]
    package_parse = [x.split(" ") for x in package_list]
    # convert to dictionary with package names as key and versions as values
    package_environment = {x[0]: x[1] for x in package_parse}
    logging.info("Getting package versions from environment")

    # check pip packages version from jupyterlab
    driver.find_element_by_css_selector(".ContainerStatus__selected-tool").click()
    time.sleep(10)
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[1])
    time.sleep(5)
    driver.find_element_by_css_selector("[data-category = Notebook]").click()
    time.sleep(5)
    el = driver.find_element_by_css_selector(".CodeMirror-line")
    actions = ActionChains(driver)
    # implement script the import packages and print the versions.
    package_script = "import pandas\nimport numpy\nimport matplotlib\n" \
                     "print('pandas', pandas.__version__," \
                     " 'numpy',numpy.__version__," \
                     " 'matplotlib', matplotlib.__version__)"
    actions.move_to_element(el).click(el).send_keys(package_script).perform()
    driver.find_element_by_css_selector(".jp-RunIcon").click()
    time.sleep(5)
    # extract the output of package versions as string and parse to a list.
    time.sleep(2)
    package_output = driver.find_element_by_css_selector(".jp-OutputArea-output>pre").text.split(" ")
    # convert to dictionary with package names as key and versions as values.
    package_jupyter = dict(zip(package_output[::2], package_output[1::2]))
    logging.info("Getting package versions from jupyterlab")
    # check if package versions from environment and from jupyter notebook are same.
    assert package_environment == package_jupyter, "Package versions match"
    time.sleep(10)
    # stop the container after the test is finished
    driver.switch_to.window(window_handles[0])
    time.sleep(5)
    testutils.stop_container(driver)
    time.sleep(5)
    assert testutils.is_container_stopped(driver), "Expected stopped container"



    '''
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


def test_valid_custom_docker(driver: selenium.webdriver):
    """
    Test valid custom Docker instructions.

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
    testutils.add_py3_min_base(driver)
    # wait until container status is stopped
    wait = selenium.webdriver.support.ui.WebDriverWait(driver, 200)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex>.Stopped")))
    # add custom docker instructions
    testutils.add_valid_custom_docker(driver)
    # wait until container status is stopped
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex>.Stopped")))
    # assert container status is stopped and 'Successfully tagged' is in footer
    assert driver.find_element_by_css_selector(".flex>.Stopped").is_displayed(), "Expected stopped container"
    assert "Successfully tagged" in driver.find_element_by_css_selector(".Footer__message-title").text, "Expected 'Successfully tagged' in footer"

