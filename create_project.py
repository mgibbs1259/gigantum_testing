from selenium import webdriver

#set driver
#can also set to Firefox
driver = webdriver.Chrome()
driver.get("localhost:10000/projects/local#")

#get past login
driver.find_element_by_class_name("Login__button").click()

#load page
driver.implicitly_wait(3)

#username
driver.find_element_by_css_selector("input[name='username']").click()
driver.find_element_by_css_selector("input[name='username']").send_keys(input('Enter your username: '))

#password
driver.find_element_by_css_selector("input[name='password']").click()
driver.find_element_by_css_selector("input[name='password']").send_keys(input('Enter your password: '))

#submit
driver.find_element_by_css_selector("button[type='submit']").click()

#load page
driver.implicitly_wait(5)

#turn off Got it!
driver.find_element_by_css_selector("button[class='button--green']").click()

#turn off guide
driver.find_element_by_css_selector("span[class='Helper-guide-slider']").click()

#create new project
driver.find_element_by_css_selector("div[class='btn--import']").click()

