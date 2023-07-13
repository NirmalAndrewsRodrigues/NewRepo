
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the w3schools homepage
driver.get("https://www.w3schools.com")
time.sleep(3)


# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","search2") old syntax
search_bar = driver.find_element("id","search2")
search_bar.send_keys("python tutorial")
time.sleep(5)
# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
# assert "python tutorial" in driver.title

# Selecting a "Start learning Python now " from the search results
PythonT_link = driver.find_element("xpath","/html/body/div[5]/div[1]/div[1]/div[3]/a")

PythonT_link.click()

time.sleep(5)
# Waiting for the laptop details page to load
time.sleep(5)
# selecting the "try it yourself option "

tryurself_Link = driver.find_element("xpath","/html/body/div[5]/div[1]/div[1]/div[3]/a")
tryurself_Link.click()
time.sleep(5)

time.sleep(5)
# Closing the webdriver
driver.close()
