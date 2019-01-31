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



def test_labbook_delete(driver: selenium.webdriver, *args, **kwargs):


    testutils.log_in(driver)
    time.sleep(2)
    testutils.remove_guide(driver)
    testutils.create_project_without_base(driver)
    time.sleep(2)
    # python 3 minimal base
    testutils.add_py3_min_base(driver)
