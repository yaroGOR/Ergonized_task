import sys
import requests
import random
import time
import string

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.safari.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def searchForm(item, keys=None):
	if item == 'email':
		elem = driver.find_element(By.NAME,item)
		elem.send_keys(keys)

	elif item == 'password':
		elem = driver.find_element(By.NAME,item)
		elem.send_keys(keys)

	elif item =='username':
		elem = driver.find_element(By.NAME,item)
		elem.send_keys(keys)

	elif item =='month':
		day = driver.find_element(By.CLASS_NAME,'month-1Z2bRu')
		day.click()
		day_input = wait.until(EC.element_to_be_clickable((By.ID, "react-select-3-option-6")))
		day_input.click()

	elif item =='day':
		month = driver.find_element(By.CSS_SELECTOR,".css-1hwfws3")
		month.click()
		month_input = wait.until(EC.element_to_be_clickable((By.ID, "react-select-2-option-6")))
		month_input.click()

	elif item =='year':
		year = driver.find_element(By.CLASS_NAME,'year-3_SRuv')
		year.click()
		year_input = wait.until(EC.element_to_be_clickable((By.ID, "react-select-4-option-24")))
		year_input.click()
	elif item == 'button':
		button = driver.find_element(By.CLASS_NAME,'button-1cRKG6').click()

	else:
		print('Smth gome wrong')
#program

email = sys.argv[1]
characters = list(string.ascii_letters + string.digits)
username= sys.argv[2]
#generate password
password = []
for i in range(10):
		password.append(random.choice(characters))
password ="".join(password)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://discord.com/register')
wait = WebDriverWait(driver, 10)

print('You entered email: '+email)
print('You entered username: '+username)
print('Generated password: '+password)

searchForm('email', email)
searchForm('username', username)
searchForm('password', password)
searchForm('day')
searchForm('month')
searchForm('year')
searchForm('button')

#month_input.send_keys(Keys.ENTER)
x=input('Waiting for passing recapcha.... Enter "YES" when you pass and redirect to chanels: ')
if x =='YES':
	time.sleep(10)
	print('thats all.')
	
	#script to get auth token here
else:
	time.sleep(5)

time.sleep(100)