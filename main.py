from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")
play = True
counting_time = time.time()
end_time = time.time()+60*5
def find_best_upgrade():
    try:
        new_upgrade = driver.find_element(By.CSS_SELECTOR, value="#upgrades .enabled")
        new_upgrade.click()
    except:
        pass
    
    cookie_count = int(driver.find_element(By.ID, value="cookies").text.split()[0].replace(",",""))
    upgrades = driver.find_elements(By.CSS_SELECTOR, value="#products .content")
    dict_upgrades = {i.text.split("\n")[0]:int(i.text.split("\n")[1].replace(',','')) for i in upgrades}
    best_upgrade = " "
    for  key, value in dict_upgrades.items():
        if cookie_count > value:
            best_upgrade = key
    
    for i in upgrades:
        if best_upgrade==i.text.split("\n")[0]:
            print("hi")
            i.click()
            break
            
cookie = driver.find_element(By.ID, value="bigCookie")
while play:
    cookie.click()
    now = time.time()
    if now > end_time:
        cps = driver.find_element(By.ID, value="cookies").text.split("\n")[1]
        print(cps)
        play=False
    if now - counting_time >= 10:
        find_best_upgrade()
        counting_time = now


