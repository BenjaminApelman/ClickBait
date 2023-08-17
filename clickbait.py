import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#password JrS88lmo7
    #     JrS88lmo7



s= Service('/usr/local/bin/chromedriver') # establish path to driver


driver = webdriver.Chrome()


#Open Twitter:
try:
    driver.get("https://twitter.com/i/flow/login")
    print("At Twitter loign")
except:
    print("Failed to reach Twitter login")

time.sleep(2)

try:  
    driver.find_element(By.XPATH, "//input").send_keys("beap9735@colorado.edu")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input").send_keys(Keys.RETURN)
except:
    print("Email not entered")

time.sleep(2)



#Unusual activity check
try:
    driver.find_element(By.XPATH, "//input").send_keys("MarcoGari42")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input").send_keys(Keys.RETURN)
except:
    print("Pass")
    
time.sleep(3)

#Ender PassWord
try:
    driver.find_element(By.NAME, "password").send_keys("JrS88lmo7")
    time.sleep(1)
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
except:
    print("Pass")








while(True):
    pass 
