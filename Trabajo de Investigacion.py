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
from datetime import datetime as datetime_
import json
import io
import pywintypes
import win32cred
#endregion

CRED_TYPE_GENERIC = win32cred.CRED_TYPE_GENERIC

url = "file:C:\\Pagina.html"
path = "C:\\jason.json"

#region Selenium configuration
options = webdriver.ChromeOptions()
options.add_argument("--incongnito")
driver = webdriver.Chrome(options=options) #, executable_path="\\chromedriver.exe"
wait = WebDriverWait(driver,15) 
#endregion

#region Variables setup - Oriented Object Paradigm
class Person:
    Name = ""
    Surename = ""
    Email = ""
    Address = ""
    Telephone = ""
    Query = ""

    def __init__(self, Name, Surename, Email, Address, Telephone,Query):
        self.Name = Name
        self.Surename =  Surename
        self.Email = Email
        self.Address = Address
        self.Telephone = Telephone
        self.Query = Query

def readFile(path):
    print("Reading file")
    f = open(path, "r")
    listaPreliminar = f.read()
    print(listaPreliminar)
    return listaPreliminar

def jsonDeserialize(jason):
    print("Processing JSON file")
    listaJsonElements = json.loads(jason)
    for persona in listaJsonElements:
        auxPersona = Person(**persona) #Mapeo 
        ListaDeClientes.append(auxPersona)
    print("JSON file processed")

#endregion

#region Selenium Excecution
print("UAI - Programacion II - Grupo 4")
print("- Selenium Automation -")
print("Start time: ")
print(datetime_.now())

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
jsonDeserialize(readFile(path),ListaDeClientes)

try :
    for cliente in ListaDeClientes:

        driver.get(url)

        #Wait for page to load
        wait.until(EC.presence_of_element_located((By.NAME,"nombre")))

        #1. Name 
        wait.until(EC.element_to_be_clickable((By.ID,"nombre"))).send_keys(cliente.Name)
        #time.sleep(0.1)

    #2. Surename
        wait.until(EC.presence_of_element_located((By.ID,"apellido"))).send_keys(cliente.Surename)
        #time.sleep(0.1)

        #2. Email
        wait.until(EC.presence_of_element_located((By.NAME,"correo"))).send_keys(cliente.Email)
        #time.sleep(0.1)

        #3. Address >> No anda el cornudo
        wait.until(EC.presence_of_element_located((By.NAME,"direccion"))).send_keys(cliente.Address)
        #time.sleep(0.1)

        #4. Telephone number >> No anda el cornudo
        wait.until(EC.presence_of_element_located((By.NAME,"telefono"))).send_keys(cliente.Telephone)
        #time.sleep(0.1)

        #5. Tipo de consulta
        wait.until(EC.presence_of_element_located((By.TAG_NAME,"select"))).send_keys(cliente.Query)
        #time.sleep(0.1)

        #6. Espero para mostrar el screen
        #time.sleep(5)

        #7. Enviar button
        boton = True
        boton = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/form/ul/li[8]/button"))).click
        if(boton):
            print("No se encontro el boton")
            print("Intentando con JS...")
            #javas = "document.getElementById('button1')[0].click();" #Clickeo el primer elemento que encuentro
            #driver.execute_script(javas)

except Exception as e :
    print("Exception found" + e.msg)
    driver.close()
    driver.quit()

finally:
    driver.close()
    driver.quit()   

    #endregion