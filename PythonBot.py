# -*- coding: cp1251 -*-
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import random



try:
    driver = webdriver.Ie('C:\\Project\\PythonBot\\IEDriverServer.exe')
    driver.get("https://forms.krasnodar.ru/opros-naseleniya/?municipality=38")
    driver.refresh()
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/a').click()
    #driver.find_element(
    time.sleep(1)
    driver.find_element(By.ID , 'login').send_keys("+7(991)4199574")
    time.sleep(1)
    driver.find_element(By.ID , 'password').send_keys("9M9a9r9k-7805282!")
    time.sleep(1)
    driver.find_element(By.XPATH , '//button[@class="plain-button plain-button_wide"]').click()

    try:
        element = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, '//button[@class="plain-button plain-button_wide mb-24"]'))
        )
        element.click()
    except : time.sleep(5)

    r = random.uniform(0,2)
    if r:
        time.sleep(1)
        driver.find_element(By.XPATH , '//input[@value="47"]').click()
    else:
        time.sleep(1)
        driver.find_element(By.XPATH , '//input[@value="48"]').click()


    driver.delete_all_cookies()
    time.sleep(5)
    driver.quit()

except Exception as e:
    print(e)

