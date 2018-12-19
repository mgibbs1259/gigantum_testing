from selenium import webdriver
import uuid
import time

#set driver
#can also set to Firefox
driver = webdriver.Chrome()
driver.get("localhost:10000/projects/local#")
driver.implicitly_wait(30)

#get past login
driver.find_element_by_class_name("Login__button").click()

#username
driver.find_element_by_css_selector("input[name='username']").click()
driver.find_element_by_css_selector("input[name='username']").send_keys(input('Enter your username: '))

#password
driver.find_element_by_css_selector("input[name='password']").click()
driver.find_element_by_css_selector("input[name='password']").send_keys(input('Enter your password: '))

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
driver.find_element_by_xpath("//p[contains(text(), 'A minimal Base containing Python 3.6 and JupyterLab with no additional packages')]").click()

#create project
driver.find_element_by_xpath("//button[contains(text(), 'Create Project')]").click()

#add packages
driver.find_element_by_xpath("//a[contains(text(), 'Environment')]").click()
#need to add option for conda3 and apt here
#check with selenium if stopped
time.sleep(15)
driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div[1]/div[1]/div[2]/div/div[4]/div/div[2]/button").click()

#iterate to add packages
packages = ['pandas', 'numpy', 'matplotlib']
for pack in packages:
    driver.find_element_by_css_selector("input[class='PackageDependencies__input']").click()
    driver.find_element_by_css_selector("input[placeholder='Enter Dependency Name']").send_keys(pack)
    driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div[1]/div[1]/div[2]/div/div[4]/div/div[2]/div/div[1]/button").click()
driver.find_element_by_xpath("//button[contains(text(), 'Install Selected Packages')]").click()

#driver.close()

#next steps - invalid login, invalid packages, file upload, change in jupyter lab, activity