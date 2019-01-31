# Builtin imports
import logging
import requests
import sys
import json

# Library imports
import selenium
from selenium.webdriver.common.by import By


logging.basicConfig(level=logging.INFO)


def test_edge_build_versions(driver: selenium.webdriver, *args, **kwargs):
    """
    Test that the requests edge build version matches the selenium edge build version.

    Args:
        driver
    """
    # get requests edge build version
    r = requests.get("http://localhost:10000/api/ping")
    if r.status_code != 200:
        logging.error("Gigantum is not found at localhost:10000")
        sys.exit(1)
    requests_edge_build_version = json.loads(r.text)
    # get selenium edge build version
    driver.get("http://localhost:10000/api/ping/")
    selenium_edge_build_version = json.loads(driver.find_element_by_css_selector("pre").text)
    # assert edge build versions match
    assert requests_edge_build_version == selenium_edge_build_version, "requests edge build version does not match selenium edge build version"