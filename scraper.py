from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd

URL = 'https://miaminutrition.miamioh.edu/NetNutrition/MU'
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(r'C:\Users\RyanC\Desktop\myProjects\miamiMeals\chromedriver\chromedriver.exe', options=chrome_options)

driver.get(URL)

imageNums = [11, 27, 51, 62]

for num in imageNums:
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[@id='cbo_nn_unitImages_"+str(num)+"']/div[1]/a")))
    elem = driver.find_element_by_xpath("//*[@id='cbo_nn_unitImages_"+str(num)+"']/div[1]/a")
    print(elem.text)
    elem.click()
    
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[@id='cbo_nn_childUnitDataList']/div")))
    for i in range(10):
        i+=1
        card = driver.find_element_by_xpath(f"/html/body/div/main/form/div/div[2]/div/div[2]/section/section/div/div[{i}]/div/div[1]/div[1]/a")
        print(card.text)
        card.click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/main/form/div/div[2]/div/div[3]/section/nav/a[1]")))
        back = driver.find_element_by_xpath("/html/body/div/main/form/div/div[2]/div/div[3]/section/nav/a[1]")
        back.click()
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, f"/html/body/div/main/form/div/div[2]/div/div[2]/section/section/div/div[{i+1}]/div/div[1]/div[1]/a")))
            card = driver.find_element_by_xpath(f"/html/body/div/main/form/div/div[2]/div/div[2]/section/section/div/div[{i+1}]/div/div[1]/div[1]/a")
        except:
            break
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[@id='childUnitsPanel']/section/nav/a[1]")))
    elem = driver.find_element_by_xpath("//*[@id='childUnitsPanel']/section/nav/a[1]")
    elem.click()

driver.close()

# ON PAUSE UNTIL MIAMI UNIVERSITY MEALS ARE BACK ON #


