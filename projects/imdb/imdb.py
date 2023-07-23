from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


service = Service("../chromedriver.exe")
options = Options()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.get("https://www.imdb.com/")

driver.find_element(By.ID, "imdbHeader-navDrawerOpen").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[text()='Top 250 Movies']").click()
time.sleep(1)


driver.quit()
