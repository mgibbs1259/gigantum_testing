import argparse
import logging
import time
import sys
import os
import docker


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


def run_playbook(path, headless, firefox):
    test_methods = load_test_methods(path)
    test_collect = {t.__name__: None for t in test_methods}

    if headless and firefox:
        logging.error('Cannot run firefox in headless mode!')
        sys.exit(1)
   
    for t in test_methods:
        logging.info(f'Running {path}:{t.__name__} ...')
        if firefox:
            driver = testutils.load_firefox_driver()
        elif headless:
            driver = testutils.load_chrome_driver_headless()
        else:
            driver = testutils.load_chrome_driver()

        driver.implicitly_wait(5)
        driver.set_window_size(1440, 1000)
        try:
            t0 = time.time()
            t(driver)
            tfin = time.time()
            logging.info(f'PASS -- {path}:{t.__name__} after {tfin-t0:.2f}s')
            test_collect[t.__name__] = {
                'status': 'PASS',
                'failure_message': None,
                'duration': round(tfin-t0, 2),
                'exception': None
            }
        except Exception as e:
            fail_type = 'ERROR' if type(e) != AssertionError else 'FAIL'
            tfin = time.time()
            logging.error(f'{fail_type} -- {path}:{t.__name__} after {tfin-t0:.2f}s: {e}')
            test_collect[t.__name__] = {
                'status': fail_type,
                'failure_message': str(e),
                'duration': round(tfin-t0),
                'exception': str(type(e))
            }
        finally:
            driver.quit()
            time.sleep(1)

    return test_collect


def stop_project_containers(client):
    containers = client.containers.list()
    for c in containers:
        for t in [c.image.tags]:
            if 'gmlb-' in t:
                logging.info(f"Stopping container for image {t}")
                c.stop()
    logging.info("Pruning all Docker containers")
    logging.info(client.containers.prune())


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--headless', default=False, action='store_true',
                           help='Optional name of specific playbook')
    argparser.add_argument('--firefox', default=False, action='store_true',
                           help='Run using Firefox driver (Chrome default)')
    argparser.add_argument('test_path', nargs='?', type=str, default="",
                           help='Optional name of specific playbook')
    args = argparser.parse_args()


    # TODO - Remove this line shortly
    os.environ['GIGANTUM_HOME'] = os.path.expanduser('~/gigantum/')
    docker_client = docker.from_env()
    playbooks = get_playbooks(args.test_path)

    failed = False
    full_results = {}
    for pb in playbooks:
        r = run_playbook(pb, args.headless, args.firefox)
        if any([r[l]['status'].lower() != 'pass' for l in r]):
            failed = True
        full_results[pb] = r
        stop_project_containers(docker_client)
    
    logging.info("Cleaning up...")
    testutils.cleanup()

    print(f'\n\nTEST SUMMARY ({len(full_results)} tests)\n')
    for test_file in full_results.keys():
        for test_method in full_results[test_file].keys():
            d = full_results[test_file][test_method]
            print(f"{d['status'].upper():6s} :: {test_file}@{test_method} ({d['duration']:.2f} sec) : {d['failure_message'] or ''}")

    if failed:
        sys.exit(1)
    else:
        sys.exit(0)

