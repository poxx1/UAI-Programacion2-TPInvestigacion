# UAI - Programacion II - Grupo 4
# Robot de automatizacion con Selenium 

#region Short version control
# v0.0 ---> Forms testing
# v0.1 ---> MongoDB connection
# v0.2 ---> lalala
# v0.3 ---> Form changed to html page
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
from urllib.parse import quote_plus
#from email_config import gmail_pass, user, host

#Other imports
import datetime
from datetime import datetime as datetime_
from datetime import timedelta
import json
import requests
import io
import sys
import time
import os, uuid
import pywintypes
import win32cred
import email
import imaplib
#endregion

CRED_TYPE_GENERIC = win32cred.CRED_TYPE_GENERIC

url = "file:C:\\Pagina.html"

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
        "Telephone" : Person.telephone,
        "Query" : Person.query
    }
    
def readFile(path):
    print("Reading file")

def jsonDeserialize(json,lista):
    print("Processing JSON file")

#endregion

#region Selenium Excecution
print("UAI - Programacion II - Grupo 4")
print("- Selenium Automation -")
print("Start time: ")
print(datetime_.now())

#def uploadData():
#    client = pymongo.MongoClient("mongodb+srv://julian:password@cluster0.s9jgwyg.mongodb.net/?retryWrites=true&w=majority")
#    result = client["Prog2"]["Clients"].find()
#    #https://www.mongodb.com/languages/python/pymongo-tutorial
#    print("Client Uploaded")

def getCredentials():
    CredEnumerate = win32cred.CredEnumerate
    CredRead = win32cred.CredRead

    try:
        creds = CredEnumerate(None, 0)  # Enumerate credentials
    except Exception:              		# Avoid crashing on any exception
        pass
        
    credentials = []

    for package in creds:
        try:
            target = package['TargetName']
            creds = CredRead(target, CRED_TYPE_GENERIC)
            credentials.append(creds)
        except pywintypes.error:
            pass     

        credman_creds = io.StringIO() # In-memory text stream

        for cred in credentials:
            try:
                service = cred['TargetName']
                username = cred['UserName']
                password = cred['CredentialBlob'].decode()

                credman_creds.write('Service: ' + str(service) + '\n')
                credman_creds.write('Username: ' + str(username) + '\n')
                credman_creds.write('Password: ' + str(password) + '\n')
                credman_creds.write('\n')
            except Exception as credentialsError:
                print(credentialsError)

        return credman_creds.getvalue()   
print(getCredentials())

ListaDeClientes = []
jsonDeserialize(readFile(),ListaDeClientes)

for cliente in ListaDeClientes:
    try :
        driver.get(url)

        #Wait for page to load
        wait.until(EC.presence_of_element_located((By.NAME,"nombre")))

        #1. Name 
        wait.until(EC.element_to_be_clickable((By.ID,"nombre"))).send_keys(cliente.name)
        #time.sleep(0.1)

    #2. Surename
        wait.until(EC.presence_of_element_located((By.ID,"apellido"))).send_keys(cliente.surname)
        #time.sleep(0.1)

        #2. Email
        wait.until(EC.presence_of_element_located((By.NAME,"correo"))).send_keys(cliente.email)
        #time.sleep(0.1)

        #3. Address >> No anda el cornudo
        wait.until(EC.presence_of_element_located((By.NAME,"direccion"))).send_keys(cliente.address)
        #time.sleep(0.1)

        #4. Telephone number >> No anda el cornudo
        wait.until(EC.presence_of_element_located((By.NAME,"telefono"))).send_keys(cliente.telephone)
        #time.sleep(0.1)

        #5. Tipo de consulta
        wait.until(EC.presence_of_element_located((By.TAG_NAME,"select"))).send_keys(cliente.query)
        #time.sleep(0.1)

        #6. Espero para mostrar el screen
        #time.sleep(5)

        #7. Enviar button
        boton = True
        boton = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/form/ul/li[8]/button"))).click
        if(boton):
            print("No se encontro el boton")
            print("Intentando con JS...")
            javas = "document.getElementById('button1')[0].click();" #Clickeo el primer elemento que encuentro
            driver.execute_script(javas)

        driver.close()
        driver.quit()

    except Exception as e :
        print("Exception found" + e.msg)
        driver.close()
        driver.quit()

    #endregion