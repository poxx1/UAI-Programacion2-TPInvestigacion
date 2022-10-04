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
import pymongo
import email
import imaplib
#endregion

CRED_TYPE_GENERIC = win32cred.CRED_TYPE_GENERIC

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
    
#endregion

#region Selenium Excecution
print("UAI - Programacion II - Grupo 4")
print("- Selenium Automation -")
print("Start time: ")
print(datetime_.now())

def uploadData():
    client = pymongo.MongoClient("mongodb+srv://julian:password@cluster0.s9jgwyg.mongodb.net/?retryWrites=true&w=majority")
    result = client["Prog2"]["Clients"].find()
    #https://www.mongodb.com/languages/python/pymongo-tutorial
    print("Client Uploaded")

def readEmails():
    #https://iq.opengenus.org/read-gmail-python/
    mail = imaplib.IMAP4_SSL(host)
    mail.login(user, gmail_pass)
    res, messages = mail.select('CLIENTS') #Selects the folder which u want 2 read
    messages = int(messages[0])
    for i in range(messages, messages - count, -1):
            # RFC822 protocol
            res, msg = mail.fetch(str(i), "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])

                    # Store the senders email
                    sender = msg["From"]

                    # Store subject of the email
                    subject = msg["Subject"]

                    # Store Body
                    body = ""
                    temp = msg
                    if temp.is_multipart():
                        for part in temp.walk():
                            ctype = part.get_content_type()
                            cdispo = str(part.get('Content-Disposition'))

                            # skip text/plain type
                            if ctype == 'text/plain' and 'attachment' not in cdispo:
                                body = part.get_payload(decode=True)  # decode
                                break
                    else:
                        body = temp.get_payload(decode=True)

                    # Print Sender, Subject, Body
                    print("-"*50)  # To divide the messages
                    print("From    : ", sender)
                    print("Subject : ", subject)
                    if(contain_body):
                        print("Body    : ", body.decode())

            mail.close()
            mail.logout()

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

#read_email_from_gmail(3, True)

#uploadData() 

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