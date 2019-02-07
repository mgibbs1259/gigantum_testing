# Builtin imports
import subprocess
import logging
import shutil
import time
import uuid
import glob
import uuid
import sys
import os

# Library imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def load_chrome_driver():
    """ Return Chrome webdriver """
    return webdriver.Chrome()

def load_chrome_driver_headless():
    """ Return headless Chrome webdriver """
    options = Options()
    options.add_argument("--headless")
    return webdriver.Chrome(options=options)

def load_firefox_driver():
    """ Return Firefox webdriver """
    return webdriver.Firefox()

def unique_project_name(prefix: str = "selenium-project"):
    """ Return a universally-unique project name """
    return f'{prefix}-{uuid.uuid4().hex[:8]}'

def unique_project_description():
    """ Return a universally-unique project description """
    return ''.join([str(uuid.uuid4())[:6] for num in range(30)])

def load_credentials(path: str = 'credentials.txt'):
    """ Return tuple of username and password """
    assert os.path.exists(path), f"Specificy login credentials in {path}"
    with open(path) as cfile:
        lines = cfile.readlines()
        assert len(lines) >= 2, f"Must have line for username and password in {path}"
    # return username (first line) and password (second line)
    return lines[0], lines[1]

def custom_docker_instructions():
    """ Return a custom Docker instruction"""
    return "RUN cd /tmp && git clone https://github.com/gigantum/confhttpproxy && cd /tmp/confhttpproxy && pip install -e."

def is_container_stopped(driver):
    """ Check if the container is stopped """
    return driver.find_element_by_css_selector(".flex>.Stopped").is_displayed()


def stop_container(driver):
    """ Stop container after test is finished """
    return driver.find_element_by_css_selector(".flex>.Running").click()


def cleanup():
    """ Cleanup all Docker containers and Gigantum projects made by
    this Selenium test harness. It infers projects and images by
    by the test harness according to a given pattern: "selenium-project-"
    exists as a substring of the project name """

    username = load_credentials()[0].strip()
    workdir = os.path.join(os.environ['GIGANTUM_HOME'], username)
    project_paths = glob.glob(f'{workdir}/*/labbooks/selenium-project-*')

    # TODO - Use actual docker client
    r = subprocess.run('docker images'.split(), stdout=subprocess.PIPE)
    docker_image_pairs = [(l.split()[0], l.split()[2]) for l in r.stdout.decode().split('\n') if l]
    docker_image_pairs = [p for p in docker_image_pairs
                          if f'gmlb-{username}' in p[0] and 'selenium-project-' in p[0]]

    logging.info('Warning! Deleting the following Gigantum projects and images')
    for i, e in enumerate(project_paths):
        logging.info(f'  {i+1:2d}: {e}')

    for docker_id in set([l[0] for l in docker_image_pairs]):
        cmd = f'docker rmi {docker_id}'
        try:
            p = subprocess.run(cmd.split(), stderr=subprocess.PIPE,
                               stdout=subprocess.PIPE, check=True)
            logging.info(f'  Deleted docker image {docker_id}')
        except subprocess.CalledProcessError as e:
            logging.info(f'Error in command: {cmd}', e)

    time.sleep(1)
    for project_path in project_paths:
        try:
            shutil.rmtree(project_path)
            logging.info(f'  Deleted project path {project_path}')
        except Exception as e:
            logging.info(f"Error deleting {project_path}: {e}")

