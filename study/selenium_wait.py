from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

service = Service("./chromedriver.exe")
options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window()
driver.implicitly_wait(20)   # 20 saniyeye kadar bekleme (bir kere ayarlanır her yerde çalışır)

driver.get("https://pynishant.github.io/Selenium-python-waits.html")

try_it =  driver.find_element(By.XPATH, "//button[text()='Try it']")

try_it.click()

WebDriverWait(driver,30).until(expected_conditions.presence_of_element_located((By.ID, "waitCreate")))  # ... olana kadar şu kadar saniye bekle

click_me = driver.find_element(By.ID, "waitCreate")

click_me.click()

print("Okey")


driver.quit()



