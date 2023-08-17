import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#password twitter JrS88lmo7


driver = webdriver.Chrome()


#Launch Driver @ Google login page
try:
    driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S671228005%3A1685847726769549&continue=https%3A%2F%2Faccounts.google.com%2Fgsi%2Fselect%3Fclient_id%3D49625052041-kgt0hghf445lmcmhijv46b715m2mpbct.apps.googleusercontent.com%26ux_mode%3Dpopup%26ui_mode%3Dcard%26as%3DKzrbnED0kRrghKVijCl%2FLw%26channel_id%3Da98dda3c70eae960f3701aae9d322c9d9dafa5210755f6a80fd3f27e36632b14%26origin%3Dhttps%3A%2F%2Ftwitter.com&faa=1&ffgf=1&ifkv=Af_xneE65oSJC6AxL2qcAcH-9XIAJ3k5iezQB0dMefzIVH46-zaqSnnGGY-A7645iCo_9AKt0fpeYA&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    print("Driver at Google login")
except:
    print("Failed to instatiate driver")


#Find login button
try:
    email = driver.find_element(by=By.ID, value= "identifierId")
    print("Found Login email")
except:
    print("Falied to find login email button")


#click login button
try:
    email.click
    print("Clicked on email")
except:
    print("failed to click on email")


#Enter email  
try: 
    email.send_keys("benjamin.apelman@student.prescott.edu")
    print("Sucsesfully added email")
except:
    print("failed to add email")


#Return email
try: 
    time.sleep(2)
    email.send_keys(Keys.RETURN)
    print("Email entered")
except:
    print("Failed to enter email")

time.sleep(3)
#Enter password
try:
    password = driver.find_element(by=By.ID, value="password")
    print("Found password")
except:
    print("Failed to find password")



#Enter password
try:
    password.send_keys("Just420you")
    print("Entered password")
except:
    print("Failed to enter password")


while(True):
    pass


#twitter pass: JrS88lmo7
