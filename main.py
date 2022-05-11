import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from functions import *

PATH = "/Users/josepachecosanchez/Documents/chromedriver"
driver = webdriver.Chrome(PATH)

f = open("log-"+str(get_date())+".txt", "a")
f.write("******* LOG " + str(get_date()) + " - " + str(get_time()) + " *******\n")

f.write("Waiting for the page to load...\n")
f.close()
print("Waiting for the page to load...")
driver.get('https://cotps.com/#/pages/transaction/transaction')
try:
    print("Login initialization...")
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
    id_box.send_keys("phone")

    id_box = driver.find_element(By.XPATH, "//input[@type='password']")
    id_box.click()
    id_box.send_keys("password")
    time.sleep(2)
    id_box = driver.find_element(By.CLASS_NAME, "login")
    id_box.click()
    print("Starting transactions...")
    time.sleep(10)

    while True:
        try:
            driver.get('https://cotps.com/#/pages/transaction/transaction')
            print("Trying to sell...")
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
                get_time()
                time.sleep(15)
            else:
                f = open("log-"+str(get_date())+".txt", "a")
                processing = driver.find_element(By.XPATH, "(//uni-view[@class='division-num'])[1]").text
                get_time()
                f.write("You don't have enough money to sell, we will try again in 15 mins: \n")
                f.write("TIME: " + str(get_time()) + "\nCurrent PROCESSING: " + processing + "\n")
                f.close()
                print("You don't have enough money to sell, we will try again in 15 mins , in process:", processing)
                time.sleep(900)

        except NoSuchElementException:
            time = get_time()
            f.write("There was an error TIME: " + str(get_time()) + " DATE: " + str(get_date()) + "\n")
            f.close()
            print("There was an error, trying again...")
            get_time()
            restart()
            time.sleep(2)

except:
    restart()
