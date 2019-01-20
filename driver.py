# Builtin imports
import argparse
import logging
import time
import json
import uuid
import sys
import os

# Library imports
import selenium
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

# Local packages
import testutils

TEST_ROOT = os.path.join(os.getcwd(), 'gigantum_tests')
sys.path.append(TEST_ROOT)


def get_playbooks(path):
    # If given a specific path
    if path and 'test_' in path:
        return [path]
    # Else, get all test playbooks
    return [t for t in os.listdir(os.path.join(TEST_ROOT, path))
            if '.py' in t and 'test_' in t]


def load_test_methods(path):
    playbook = __import__(path.replace('.py', ''))
    test_methods = [getattr(playbook, field) for field in dir(playbook)
                    if callable(getattr(playbook, field))
                    and 'test_' in field]
    return test_methods


def run_playbook(path):
    test_methods = load_test_methods(path)
    test_collect = {t.__name__: None for t in test_methods}
   
    for t in test_methods:
        logging.info(f'Running {path}:{t.__name__} ...')
        driver = testutils.load_chrome_driver()
        driver.set_window_size(1440, 1000)
        try:
            t0 = time.time()
            result = t()
            tfin = time.time()
            test_collect[t.__name__] = {
                'status': 'PASS',
                'failure_message': None,
                'duration': round(tfin-t0, 2),
                'exception': None
            }
        except Exception as e:
            tfin = time.time()
            test_collect[t.__name__] = {
                'status': 'ERROR' if type(e) != AssertionError else 'FAIL',
                'failure_message': str(e),
                'duration': round(tfin-t0),
                'exception': str(type(e))
            }
        finally:
            driver.quit()
            time.sleep(2)

    return test_collect



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    argparser = argparse.ArgumentParser()
    argparser.add_argument('test_path', nargs='?', type=str, default="",
                           help='Optional name of specific playbook')
    args = argparser.parse_args()

    playbooks = get_playbooks(args.test_path)

    failed = False
    full_results = {}
    for pb in playbooks:
        r = run_playbook(pb)
        if any([r[l]['status'].lower() != 'pass' for l in r]):
            failed = True
        full_results[pb] = r

    import pprint
    pprint.pprint(full_results)

    if failed:
        sys.exit(1)
    else:
        sys.exit(0)

