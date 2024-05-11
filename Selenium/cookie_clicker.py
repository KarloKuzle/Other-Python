from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")


consent = driver.find_element(By.CSS_SELECTOR, ".fc-footer-buttons button")
consent.click()

time.sleep(1)

language = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
language.click()

time.sleep(1)

cookie = driver.find_element(By.ID, "bigCookie")



def click():
    timeout = time.time() + 10  # 10 sec
    while True:
        if time.time() > timeout:
            break
        cookie.click()

click()

time.sleep(1)
score = int(driver.find_element(By.XPATH, '//*[@id="cookies"]').text.split(" ")[0])
print(f"Your score is {score} cookies!")

