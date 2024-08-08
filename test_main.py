import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import page

def test_search_mostbet():
    driver = webdriver.Chrome()
    driver.get("https://mostbet.com")
    driver.maximize_window()
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app_header"]/div[2]/nav/a[2]'))
        )
    finally:
        print("Загрузка страницы завершена")
        element.click()
    try:
        element1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div[2]/a/div'))
        )
    finally:
        print("Загрузка страницы завершена")
        element1.click()
