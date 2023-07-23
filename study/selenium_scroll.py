from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


service = Service("./chromedriver.exe")
options = Options()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

driver.get("https://stackoverflow.com/")
time.sleep(2)
driver.execute_script("window.scrollBy(0,300)","")      #Scroll 
time.sleep(3)
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")     #Sayfanın en altına gitme
time.sleep(3)
text = driver.find_element(By.XPATH, "//p[text()='Thousands of organizations around the globe use Stack Overflow for Teams']")
driver.execute_script("arguments[0].scrollIntoView()", text)
time.sleep(3)       #selenium çok hızlı yetişemeyebilir.
driver.save_screenshot("./scroll_ekran.png")

driver.quit()

