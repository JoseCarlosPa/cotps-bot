import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from twilio.rest import Client
from selenium.common.exceptions import NoSuchElementException

client = Client('TWILIOSDI', 'TWILIOTOKEN')


PATH = "/Users/josepachecosanchez/Documents/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get('https://cotps.com/#/pages/transaction/transaction')

id_box = driver.find_element(By.XPATH, "//*[contains(text(), 'United States +1')]")
id_box.click()
time.sleep(2)
id_box = driver.find_element(By.XPATH, "//input[@type='number']")
id_box.click()
id_box.send_keys("52")
time.sleep(2)
id_box = driver.find_element(By.XPATH, "//*[contains(text(), 'Confirmar')]")
id_box.click()
time.sleep(2)

id_box = driver.find_element(By.XPATH, "//input[@type='number']")
id_box.click()
id_box.send_keys("phone_number")

id_box = driver.find_element(By.XPATH, "//input[@type='password']")
id_box.click()
id_box.send_keys("password")
time.sleep(2)
id_box = driver.find_element(By.CLASS_NAME, "login")
id_box.click()

time.sleep(10)


while True:
    try:
        driver.get('https://cotps.com/#/pages/transaction/transaction')
        time.sleep(10)
        classNames = driver.find_element(By.XPATH, "(//uni-view[@class='division-num'])[2]").text
        value = float(classNames)
        if value >= 5:
            time.sleep(2)
            id_box = driver.find_element(By.CLASS_NAME, "orderBtn")
            id_box.click()
            time.sleep(15)
            id_box = driver.find_element(By.XPATH, "//*[contains(text(), 'Vendido')]")
            id_box.click()

            time.sleep(15)
        else:

            print("El valor es menos a 5 en este momento")
            time.sleep(900)

    except NoSuchElementException:
        time.sleep(2)




