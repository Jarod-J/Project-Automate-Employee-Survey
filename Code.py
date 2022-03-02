from selenium import webdriver
from getpass import getpass
from selenium.webdriver.support.ui import Select
import time 

def autologin():
     username = input("Input your Username: ")
     password = getpass("Input your Password: ")
     
     driver = webdriver.Chrome("C:\\ChromeDriver\\chromedriver.exe")
     driver.get("https://auth.csun.edu/cas/login?error=&url=&service=https://mynorthridge.csun.edu/psp/PANRPRD/?cmd=login&languageCd=ENG")
    
     username_textbox = driver.find_element_by_id("username")
     username_textbox.send_keys(username)
     time.sleep(1)
     password_textbox = driver.find_element_by_id("password")
     password_textbox.send_keys(password)
     time.sleep(1)
     login_button = driver.find_element_by_class_name("submitButton")
     login_button.click() 
  
     driver.get("https://shibboleth.csun.edu/idp/profile/cas/login?execution=e1s3")
     driver.switch_to.frame(0);
     time.sleep(5)
     push_button = driver.find_element_by_xpath("//button[@class='positive auth-button']")
     push_button.click()
     
     time.sleep(7)
     driver.get("https://mynorthridge.csun.edu/psp/PANRPRD/EMPLOYEE/EMPL/h/?tab=NRPA_STAFF_TAB")
     time.sleep(3)
     Survey_button = driver.find_element_by_xpath("//li[@class='RSS_LI_STYLE']//a[@href='https://mynorthridge.csun.edu/psp/PANRPRD_newwin/EMPLOYEE/EMPL/e/?url=https%3a%2f%2fcsun.sjc1.qualtrics.com%2fjfe%2fform%2fSV_1TG3XMjYF15dyq9%3fpslnkid%3dNRPA_SELF_SCREEN_EMPL_L&PORTALPARAM_PTCNAV=NRPA_SELF_SCREEN_EMPL_L&EOPP.SCNode=EMPL&EOPP.SCPortal=EMPLOYEE&EOPP.SCName=NRPA_CSUN_STAFF_POLICIES_AND_P&EOPP.SCLabel=CSUN%20Staff%20Policies%20and%20Proc&EOPP.SCPTcname=&FolderPath=PORTAL_ROOT_OBJECT.PORTAL_BASE_DATA.CO_NAVIGATION_COLLECTIONS.NRPA_CSUN_STAFF_POLICIES_AND_P.NRPA_F200703281052301828058717.NRPA_SELF_SCREEN_EMPL_L&IsFolder=false']")
     Survey_button.click()
     time.sleep(7)
     driver.get("https://csun.sjc1.qualtrics.com/jfe/form/SV_1TG3XMjYF15dyq9?pslnkid=NRPA_SELF_SCREEN_EMPL_L")
     time.sleep(3)
     no_button = driver.find_element_by_xpath("//input[@id='QR~QID6~1']")
     no_button.click()
     time.sleep(1)
     room_textbox = driver.find_element_by_id("QR~QID8")
     select = Select(room_textbox)
     select.select_by_visible_text('BOOKSTEIN HALL')
     time.sleep(20)
     driver.quit()
autologin()
