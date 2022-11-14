# UAI - Programacion II - Grupo 4
# Robot de automatizacion con Selenium 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime as datetime_
import data_loader
import os

URL = os.getcwd() + "/" + "frontend/index.html"
DATA_PATH = "data/data.json"

def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incongnito")
    return webdriver.Chrome(options=options)

def start_automation(driver, data):
    wait = WebDriverWait(driver, 5);
    try:
        for client in data:
            driver.get(URL)

            wait.until(EC.element_to_be_clickable((By.ID, "nombre"))).send_keys(client.name)
            wait.until(EC.presence_of_element_located((By.ID, "apellido"))).send_keys(client.surname)
            wait.until(EC.presence_of_element_located((By.NAME, "correo"))).send_keys(client.email)
            wait.until(EC.presence_of_element_located((By.NAME, "direccion"))).send_keys(client.address)
            wait.until(EC.presence_of_element_located((By.NAME, "telefono"))).send_keys(client.telephone)
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "select"))).send_keys(client.query)
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "form__button"))).click
    except Exception as e:
        print(f"Exception found: {e.msg}")
    finally:
        driver.close()
        driver.quit()

def main():
    print("UAI - Programacion II - Grupo 4")
    print("- Selenium Automation -")
    excecution_start_time = datetime_.now()
    print(f"Start time: {excecution_start_time}")

    clients = data_loader.get_clients_from_file(DATA_PATH)
    start_automation(create_driver(), clients)

    print("End of excecution")
    excecution_end_time = datetime_.now()
    print("End time: {excecution_end_time}")
    time_taken = excecution_end_time - excecution_start_time
    print(f"Opration took: {time_taken.seconds} seconds")

if __name__ == "__main__":
    main()