from selenium import webdriver
from getpass import getpass
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time 

def autologin():
     username = input("Input your Username: ")
     password = getpass("Input your Password: ")
     # Mac user 
     driver = webdriver.Chrome()
     # Windows user
     # driver = webdriver.Chrome("C:\\ChromeDriver\\chromedriver.exe")
     
     # CSUN login
     driver.get("https://csun.sjc1.qualtrics.com/jfe/form/SV_1TG3XMjYF15dyq9")
     username_textbox = driver.find_element_by_id("username").send_keys(username)
     time.sleep(1)
     password_textbox = driver.find_element_by_id("password").send_keys(password)
     time.sleep(1)
     login_button = driver.find_element_by_class_name("submitButton").click()
     
     # Duo site
     driver.get("https://shibboleth.csun.edu/idp/profile/cas/login?execution=e1s3")
     time.sleep(3)
     driver.switch_to.frame(0)
     time.sleep(3)
     push_button = driver.find_element_by_xpath("//button[@class='positive auth-button']").click()
     time.sleep(3)
     
     # survey site
     driver.get("https://csun.sjc1.qualtrics.com/jfe/form/SV_1TG3XMjYF15dyq9?pslnkid=NRPA_SELF_SCREEN_EMPL_L")
     time.sleep(7)
     no_button = driver.find_element_by_xpath("//label[@id = 'QID6-1-label']").click()
     time.sleep(3)
     room_textbox = driver.find_element_by_id("QR~QID8")
     select = Select(room_textbox)
     select.select_by_visible_text('BOOKSTEIN HALL')
     submit_button = driver.find_element_by_xpath("//input[@id = 'NextButton']").click()
     time.sleep(20)
     driver.quit()
autologin()
