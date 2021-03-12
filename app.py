import os
from selenium import webdriver

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")

driver = webdriver.Chrome(executable_path = os.environ.get("CROMEDRIVER_PATH"), chrome_options=op)

driver.get("https://www.google.com")
driver.save_screenshot('screenie.png') 
print(driver.page_source) #Hello  world in app ok
 
