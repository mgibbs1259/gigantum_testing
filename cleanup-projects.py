import subprocess
import logging
import shutil
import time
import uuid
import glob
import sys
import os

import testutils


if __name__ == '__main__':
    username = testutils.load_credentials()[0].strip()
    workdir = os.path.expanduser(f'~/gigantum/{username}')
    
    project_paths = glob.glob(f'{workdir}/*/labbooks/selenium-project-*')

    r = subprocess.run('docker images'.split(), stdout=subprocess.PIPE)
    docker_image_pairs = [(l.split()[0], l.split()[2]) for l in r.stdout.decode().split('\n') if l]
    docker_image_pairs = [p for p in docker_image_pairs
                          if f'gmlb-{username}' in p[0] and 'selenium-project-' in p[0]]

    print('Warning! Deleting the following Gigantum projects and images')
    for i, e in enumerate(project_paths):
        print(f'  {i+1:2d}: {e}')

    confirm_text = input('Confirm "Yes" to continue: ')

    if confirm_text.lower() != 'yes':
        print('Cancelled.')
        sys.exit(0)

    for docker_id in set([l[0] for l in docker_image_pairs]):
        cmd = f'docker rmi {docker_id}'
        try:
            p = subprocess.run(cmd.split(), stderr=subprocess.PIPE,
                               stdout=subprocess.PIPE, check=True)
            print(f'  Deleted docker image {docker_id}')
        except subprocess.CalledProcessError as e:
            print(f'Error in command: {cmd}', e)

    time.sleep(1)
    for project_path in project_paths:
        try:
            shutil.rmtree(project_path)
            print(f'  Deleted project path {project_path}')
        except Exception as e:
            print(f"Error deleting {project_path}: {e}")
