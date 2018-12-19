import uuid
import os

from selenium import webdriver


def load_chrome_driver():
    return webdriver.Chrome('/Users/bill/Desktop/chromedriver')

def load_firefox_driver():
    return webdriver.Firefox()

def unique_project_name(prefix: str = "selenium-project"):
    """ Return a universally-unique project name """
    return f'{prefix}-{uuid.uuid4().hex[:8]}'

def load_credentials(path: str = 'credentials.txt'):
    """ Return tuple of username and password """
    assert os.path.exists(path), f"Specificy login credentials in {path}"
    with open(path) as cfile:
        lines = cfile.readlines()
        assert len(lines) >= 2, f"Must have line for username and password in {path}"
    # Return username (first line) and pasword (second line)
    return lines[0], lines[1]


