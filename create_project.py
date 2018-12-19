import logging
import uuid
import time

import testutils


def run_script():
    username, password = testutils.load_credentials()
    logging.info(f"Using username {username}")

    #set driver
    driver = testutils.load_chrome_driver()

    driver.get("localhost:10000/projects/local#")
    driver.implicitly_wait(30)

    #get past login
    driver.find_element_by_class_name("Login__button").click()

    #username
    driver.find_element_by_css_selector("input[name='username']").click()
    driver.find_element_by_css_selector("input[name='username']").send_keys(username)

    #password
    driver.find_element_by_css_selector("input[name='password']").click()
    driver.find_element_by_css_selector("input[name='password']").send_keys(password)

    #submit
    driver.find_element_by_css_selector("button[type='submit']").click()

    #turn off Got it!
    driver.find_element_by_css_selector("button[class='button--green']").click()

    #turn off guide
    driver.find_element_by_css_selector("span[class='Helper-guide-slider']").click()

    #create new project
    driver.find_element_by_css_selector("div[class='btn--import']").click()

    #create project title
    driver.find_element_by_css_selector("input[maxlength='36']").click()
    driver.find_element_by_css_selector("input[maxlength='36']").send_keys('selenium-project-' + str(uuid.uuid4())[:6])

    #create project description
    driver.find_element_by_css_selector("textarea[class='CreateLabbook__description-input']").click()
    driver.find_element_by_css_selector("textarea[class='CreateLabbook__description-input']").send_keys(''.join([str(uuid.uuid4())[:6] for i in range(20)]))

    #continue
    driver.find_element_by_xpath("//button[contains(text(), 'Continue')]").click()

    #select base
    #bases can be - Python2 Minimal, Python3 Data Science, Python3 Minimal, R Tidyverse
    base = input('Enter base: ')
    if base == 'Python2 Minimal':
        driver.find_element_by_xpath("//li[contains(text(), 'python2')]").click()
        driver.find_element_by_xpath("//p[contains(text(), 'A minimal Base containing Python 2.7 and JupyterLab with no additional packages')]").click()
    elif base == 'Python3 Data Science':
        driver.find_element_by_xpath("//h6[contains(text(), 'Python3 Data Science Quick-Start')]").click()
    elif base == 'Python3 Minimal':
        driver.find_element_by_xpath("//p[contains(text(), 'A minimal Base containing Python 3.6 and JupyterLab with no additional packages')]").click()
    elif base == 'R Tidyverse':
        driver.find_element_by_xpath("//li[contains(text(), 'R')]").click()
        driver.find_element_by_xpath("//p[contains(text(), 'A JupyterLab install for CRAN PPA R + tidyverse packages, etc.')]").click()

    #create project
    driver.find_element_by_xpath("//button[contains(text(), 'Create Project')]").click()

    #check if build is stopped
    stop = driver.find_element_by_css_selector("div[class='ContainerStatus__container-state Stopped")
    while stop.is_displayed() == False:
        time.sleep(20)

    #add packages
    driver.find_element_by_xpath("//a[contains(text(), 'Environment')]").click()
    #need to add option for conda3 and apt here

    #check if build is stopped
    while stop.is_displayed() == False:
        time.sleep(20)

    #add packages
    driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div[1]/div[1]/div[2]/div/div[4]/div/div[2]/button").click()

    #iterate to add packages for Python bases
    if base == [pack for pack in ['Python2 Minimal', 'Python3 Data Science', 'Python3 Minimal']]:
        packages = ['pandas', 'numpy', 'matplotlib']
        for pack in packages:
            driver.find_element_by_css_selector("input[class='PackageDependencies__input']").click()
            driver.find_element_by_css_selector("input[placeholder='Enter Dependency Name']").send_keys(pack)
            driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div[1]/div[1]/div[2]/div/div[4]/div/div[2]/div/div[1]/button").click()
    else:
        pass
    driver.find_element_by_xpath("//button[contains(text(), 'Install Selected Packages')]").click()

#file upload


if __name__ == '__main__':
    try:
        run_script()
    finally:
        logger.info("Closing driver")
        driver.close()

#next steps - invalid login, invalid packages, file upload, change in jupyter lab, activity
