from selenium import webdriver
from selenium.webdriver.common.by import By

# keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/dp/B09Q923TLT/ref=sspa_dk_browse_0?ie=UTF8&sp_csd=d2lkZ2V0TmFtZT1zcF9icm93c2VfdGhlbWF0aWM&th=1")

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

print(f"The price is {price_dollar.text}.{price_cents.text}")

# driver.close()
driver.quit()