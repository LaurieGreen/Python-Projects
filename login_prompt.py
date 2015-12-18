from selenium import webdriver
import getpass
import time

target = ""
account_amount = 2
first_account = 107
name = "Laurie Green"
email = "laurie.green@poletowininternational.com"
password = "e4e!t3stSRVR"
clear = "\n" * 100

print clear
print "============================INPUT================================"
while target == "":
	target_server = raw_input("Please enter server (e.g. Chaos, Multi, Sisi): ")
	if target_server == 'Sisi' or target_server == 'sisi' or target_server == 'singularity' or target_server == 'Singularity':
		target = "//87.237.38.24:50001/"
		print "You chose %s" % target
	if target_server == 'Chaos' or target_server == 'chaos' or target_server == 'chacha' or target_server == 'Chacha':
		target = "//87.237.38.71:50001/"
		print "You chose %s" % target
	if target_server == 'Multi' or target_server == 'multi' or target_server == 'multiplicity' or target_server == 'Multiplicity':
		target = "//87.237.38.71:50001/"
		print "You chose %s" % target
	if target == "":
		print "DIDN'T UNDERSTAND"

#account_amount = raw_input("How many accounts: ")	
#first_account = raw_input("First account: ")
#name = raw_input("Full Name: ")
#email = raw_input("Email Address: ")
#password = getpass.getpass("Password: ")
print "============================OUTPUT==============================="
print ""
print "Server: %s" % target
print ""
print "Amount of Accounts: %s" % account_amount
print ""
print "First Account: %s" % first_account
print ""
print "Name: %s" % name
print ""
print "Email Address: %s" % email
print ""
print "Password: %s" % password
print ""
print "Launching Firefox... Please wait..."
print ""
print "================================================================"
driver = webdriver.Firefox()
driver.get("http:%s/gm/users.py" % (target)) 

current_account = first_account

while current_account < (account_amount + first_account):
	#new_user = driver.find_element_by_link_text("Add User")
	#new_user.click()
	driver.get("http:%s/gm/users.py?action=AddUserForm&" % (target)) 
	user_name_input = driver.find_element_by_id('userName')
	user_name_input.send_keys("e4e_test%s" % (current_account))
	password_input = driver.find_element_by_name("password")
	password_input.send_keys(password)
	name_input = driver.find_element_by_id("fullName")
	name_input.send_keys(name)
	email_input = driver.find_element_by_id("eMail")
	email_input.send_keys("%s@poletowininternational.com" % (email))
	client_input = driver.find_element_by_id("client")
	client_input.send_keys("EVE Client")
	confirmation_input = driver.find_element_by_id("Post")
	confirmation_input.click()
	print ""
	print driver.current_url
	print ""
	getUserID(driver.current_url)
	role_link = driver.find_element_by_link_text("Roles")
	role_link.click()
	role_input = driver.find_element_by_xpath("//input[@names'ass'][16]")
	role_input.click()
	role_input = driver.find_element_by_xpath("//input[@names'ass'])[17]")
	role_input.click()
	role_input = driver.find_element_by_xpath("//input[@names'ass'])[19]")
	role_input.click()
	role_input = driver.find_element_by_xpath("//input[@names'ass'])[20]")
	role_input.click()
	role_input = driver.find_element_by_xpath("//input[@names'ass'])[11]")
	role_input.click()
	role_input = driver.find_element_by_xpath("//input[@names'ass'])[29]")
	role_input.click()
	role_input = driver.find_element_by_xpath("//input[@names'ass'])[30]")
	role_input.click()
	role_input = driver.find_element_by_xpath("//input[@names'ass'])[31]")
	role_input.click()
	role_input = driver.find_element_by_xpath("//input[@names'ass'])[38]")
	role_input.click()
	role_input = driver.find_element_by_xpath("//input[@names'ass'])[40]")
	role_input.click()
	role_link = driver.find_element_link_text("Assign Roles")
	role_link.click()
	print "e4e_test%s is now complete" % (current_account)

def getUserID(url):	
	urlList = url.split("&")
	
	
driver.quit()