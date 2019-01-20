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


def get_playbooks(path):
    sys.path.append(os.path.join(os.getcwd(), path))
    return [t for t in os.listdir(path)
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

    s = f'Running Playbook {path}'
    print(f'{s}\n{"="*len(s)}')
    for t in test_methods:
        try:
            print(f'Running test: {t.__name__}')
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
    return test_collect

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('test_path', nargs='?', type=str,
                           default='gigantum_tests')
    argparser.add_argument('--stop-early', '-x', action='store_true')
    args = argparser.parse_args()

    playbooks = get_playbooks(args.test_path)

    import pprint
    for pb in playbooks:
        r = run_playbook(pb)
        pprint.pprint(r)


sys.exit(0)

logging.basicConfig(level=logging.INFO)
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
        
    #methods_under_test = [test_all_bases, test_pip_packages, test_valid_custom_docker]
    methods_under_test = [test_pip_packages]

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
            driver.quit()
            time.sleep(2)

    print('-' * 80)
    print('\nTest Report\n')
    for test_name in tests_collection.keys():
        print(f' {tests_collection[test_name]["status"]:6s} :: {test_name} :: {tests_collection[test_name]["message"] or "n/a"}')

