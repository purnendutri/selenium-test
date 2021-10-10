from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time, os

driver = webdriver.Chrome(r"chromedriver.exe")

#Open login page
driver.get("https://github.com/login")

#setup Credentials
my_username = os.getenv('userid',"purnendutri")
my_password= os.getenv('password',"Jinu9876")

#Print Element value
webElement = driver.find_element_by_link_text("Create an account")
print(webElement.text)
print(webElement.location)

try:
    username_input_box = driver.find_element_by_name("login")
    password_input_box = driver.find_element_by_name("password")
    login_button = driver.find_element_by_xpath("(//input[starts-with(@name, 'commit')])")

    #clear the placeholders data
    username_input_box.clear()
    password_input_box.clear()

    #fill login credentials
    username_input_box.send_keys(my_username)
    time.sleep(2) 
    password_input_box.send_keys(my_password)
    time.sleep(2)
    login_button.click()

except NoSuchElementException as exception:
    print ("Element not found and test failed")

time.sleep(15)
driver.close()
