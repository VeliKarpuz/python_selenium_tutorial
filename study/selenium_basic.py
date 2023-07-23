from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

service = Service("../chromedriver.exe")
options = Options()
options.add_experimental_option("detach",True) 
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://tr.linkedin.com/")
link = driver.current_url                               #current_url 
print(link)

title = driver.title                                    #title
print(title)

driver.maximize_window()                                #maximize_window

driver.get("https://stackoverflow.com/")   

driver.back()                                           #back

driver.forward()                                        #forward

driver.refresh()                                        #refresh

driver.save_screenshot("./screenshot.png")              #screenshot

driver.close()                                          #Son pencereyi kapatır.

driver.quit()                                           #Bütün pencereleri kapatır.