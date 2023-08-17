import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

#navigate to ChatGPT
try:
    driver.get("https://chat.openai.com/")
except:
    print("Failed to reach AI")


#login
time.sleep(1)
try:
  loginButton = driver.find_element(By.XPATH, "//button")
  loginButton.click()
except:
    print("loggin button not found")

time.sleep(5)


#verify you are human ;)
try:
    verifyButton = driver.find_element(By.XPATH, "//input")
    verifyButton.click
    print("clicked veryify")
except:
    print("not verified")





while(True):
    pass

#//*[@id="__next"]/div[1]/div[1]/div[4]/button[1]