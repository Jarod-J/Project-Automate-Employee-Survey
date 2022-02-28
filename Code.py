from selenium import webdriver
from getpass import getpass
def autologin():
     username = input("Input your Username: ")
     password = getpass("Input your Password: ")
     
     driver = webdriver.Chrome("C:\\ChromeDriver\\chromedriver.exe")
     driver.get("https://csun.sjc1.qualtrics.com/jfe/form/SV_1TG3XMjYF15dyq9")
    
     username_textbox = driver.find_element_by_id("username")
     username_textbox.send_keys(username)
     
     password_textbox = driver.find_element_by_id("password")
     password_textbox.send_keys(password)
 
     login_button = driver.find_element_by_id("_shib_idp_revokeConsent")
     login_button.submit()   
autologin()