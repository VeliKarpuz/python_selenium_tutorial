from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


service = Service("../chromedriver.exe")
options = Options()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=service, options=options)

base_url = "https://the-internet.herokuapp.com/login"

def test(user_name, password):
    
    driver.get(base_url)
    driver.maximize_window()

    user_name_box = driver.find_element(By.ID, "username" )
    user_name_box.send_keys(user_name)
    password_box = driver.find_element(By.ID, "password" )
    password_box.send_keys(password)
    login_button = driver.find_element(By.CLASS_NAME, "radius")
    login_button.click()

    title = driver.find_element(By.ID, "flash")
    print(title.text)
    return title.text
    
test("tomsmith", "SuperSecretPassword!")
driver.save_screenshot("projects/login/logged_secreen.png")


driver.close()