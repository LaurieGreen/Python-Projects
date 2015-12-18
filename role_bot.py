from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import time

def getUserID(url):	
	urlList = url.split("http://87.237.38.24:50001/gm/users.py?Submit=1&userID=")
	print 
	return urlList[1]

target = "//87.237.38.24:50001/"
target_account = raw_input("Please enter account name: ")

driver = webdriver.Firefox()
driver.get("http://87.237.38.24:50001/gm/users.py")
user_name_input = driver.find_element_by_id('userID_ac')
user_name_input.send_keys(target_account)
time.sleep(0.5)
user_name_input.send_keys(Keys.ARROW_DOWN)
time.sleep(0.5)
user_name_input.send_keys(Keys.RETURN)
time.sleep(0.5)
confirm_link = driver.find_element_by_xpath("//input[@value='GO']")
confirm_link.click()

info = driver.find_element_by_link_text("INFO")
info.click()

driver.get("http:%sgm/users.py?action=UserRoles&userID=%s" % (target, getUserID(driver.current_url))) 

role_input = driver.find_element_by_xpath("//input[@value='36028797018963968'])")
role_input.click()
role_input = driver.find_element_by_xpath("//input[@value='9007199254740992']")
role_input.click()
role_input = driver.find_element_by_xpath("//input[@value='18014398509481984']")
role_input.click()
role_input = driver.find_element_by_xpath("//input[@value='8388608']")
role_input.click()
role_input = driver.find_element_by_xpath("//input[@value='4194304']")
role_input.click()
role_input = driver.find_element_by_xpath("//input[@value='4503599627370496']")
role_input.click()
role_input = driver.find_element_by_xpath("//input[@value='8589934592']")
role_input.click()
role_input = driver.find_element_by_xpath("//input[@value='137438953472']")
role_input.click()
role_input = driver.find_element_by_xpath("//input[@value='144115188075855872']")
role_input.click()
role_input = driver.find_element_by_xpath("//input[@value='4096']")
role_input.click()
role_link = driver.find_element_by_xpath("//input[@value='Assign roles']")
role_link.click()