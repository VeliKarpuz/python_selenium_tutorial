from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


service = Service("../chromedriver.exe")
options = Options()
options.add_experimental_option("detach",True)
toms_URL= "https://tomspizzeria.b4a.app/"

driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.get(toms_URL)

def siparis_mesaji_kontrol(beklenen_mesaj):
    driver.find_element(By.ID, "siparis").click()
    mesaj = driver.find_element(By.ID, "mesaj").text
    assert mesaj == beklenen_mesaj

#müşteri isim girme kontrolü
siparis_mesaji_kontrol("Müşteri ismi girmediniz")

#pizza boyu seçme kontrolü
isim = "veli"
driver.find_element(By.ID, "musteri-adi").send_keys(isim)
siparis_mesaji_kontrol("Pizza boyu seçmediniz")

#pizzanın üstüne ekleme
driver.find_element(By.CSS_SELECTOR, "input[value='Orta']").click()      #boy seçimi
zeytin = driver.find_element(By.CSS_SELECTOR, "input[value='zeytin']").click()
mantar = driver.find_element(By.CSS_SELECTOR, "input[value='mantar']").click()

#ödeme yöntemi seçme kontrolü
odeme = driver.find_element(By.ID, "odeme-tipi")
dropdown = Select(odeme)
dropdown.select_by_index(2)
siparis_mesaji_kontrol("Siparişiniz alındı")

musteri_ismi = driver.find_element(By.ID, "musteri").text
pizza_boyu = driver.find_element(By.ID, "pizzaboyu").text
pizza_ustu = driver.find_element(By.ID, "pizzaustu").text
odeme_tipi = driver.find_element(By.ID, "odeme").text
tutar = driver.find_element(By.ID, "tutar").text

assert musteri_ismi == "Müşteri ismi: {}".format(isim)
assert pizza_boyu == "Pizza boyu: Orta"
assert pizza_ustu == "Pizza üstü: zeytin, mantar"
assert odeme_tipi == "Ödeme tipi: Kredi Kartı"
assert tutar == "Tutar: 16 TL"

driver.save_screenshot("projects/toms_pizzeria/last_screen.png")

print("Sorun yok")

driver.quit()