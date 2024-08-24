from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Specify the path to the chromedriver executable
chromedriver_path = "C:/chromedriver-win32"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to a webpage
driver.get("https://www.google.com")

# Find the search box using its name attribute value
search_box = driver.find_element(By.NAME, 'q')

# Enter text into the search box
search_box.send_keys('Selenium Python')


# Submit the search form
search_box.send_keys(Keys.RETURN)

# Close the browser
driver.quit()
