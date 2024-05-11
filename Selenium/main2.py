from selenium import webdriver
from selenium.webdriver.common.by import By

# keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
button = driver.find_element(By.ID, value="submit")
# print(button.size)
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# SELECT ELEMENT BY XPATH
# in the website html right-click wanted element -> copy XPATH
bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.get_attribute("href"))


# Selecting multiple elements
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
for time in event_times:
    print(time.text)
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
for name in event_names:
    print(name.text)

events = {}

events = {num: {'time': event_times[num].text, 'name': event_names[num].text} for num in range(0, len(event_times))}

# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text
#     }

print(events)


# driver.close()
driver.quit()