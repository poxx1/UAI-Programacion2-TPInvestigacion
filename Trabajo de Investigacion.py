# UAI - Programacion II - Grupo 4
# Robot de automatizacion con Selenium 

#region Short version control
# v0.0 ---> Forms testing
# v0.1 ---> MongoDB connection
# v0.2 ---> lalala
#endregion

#region Imports
#Selenium imports
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

#Other imports
import datetime
from datetime import datetime as datetime_
from datetime import timedelta
import json
import requests
import sys
import time
import os, uuid
#endregion

#region Selenium configuration
options = webdriver.ChromeOptions()
options.add_argument("--incongnito")
driver = webdriver.Chrome(options=options) #, executable_path="\\chromedriver.exe"
wait = WebDriverWait(driver,15) 
#endregion

#region Variables setup - Oriented Object Paradigm
class Person:
    def __init__(self, name, surname, email, address, telephone):
        self.name = name
        self.surname =  surname
        self.email = email
        self.address = address
        self.telephone = telephone

def buildFormEntry(Person) : 
    json_data = {
        "Name" : Person.name,
        "Surename" : Person.surename,
        "Email" : Person.email,
        "Address" : Person.address,
        "Telephone" : Person.telephone
    }

#endregion

#region Selenium Excecution
print("UAI - Programacion II - Grupo 4")
print("- Selenium Automation -")
print("Start time: ")
print(datetime_.now())

try :
    driver.get("https://forms.gle/yfK3JA4jmy4wXb74A")

    #Wait for page to load
    wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")))

    #1. Name and Surename
    wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input"))).send_keys("Julian, Lastra")
    time.sleep(0.1)

    #2. Email
    wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input"))).send_keys("julianlastra.kz@gmail.com")
    time.sleep(0.1)

    #3. Address >> No anda el cornudo
    wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input"))).send_keys("Posadas 289")
    time.sleep(0.1)

    #4. Telephone number >> No anda el cornudo
    wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input"))).send_keys("1159363830")
    time.sleep(0.1)

    #5. Espero para mostrar el screen
    time.sleep(5)

    #Enviar button
    wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span"))).click

    driver.close()
    driver.quit()

except Exception as e :
    driver.close()
    driver.quit()
    print("Exception found" + e)

#endregion