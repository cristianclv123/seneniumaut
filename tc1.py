from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)


driver.get("https://www.saucedemo.com/")
print("ok- sitio web abierto")
driver.find_element(By.ID,"user-name").send_keys("standard_user")
print("ok- nombre de usuario enviado")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
login=driver.find_element(By.ID,"login-button")
assert login.is_displayed(),"El boton no esta visible"
print("ok boton si existe")

driver.find_element(By.ID,"login-button").click()
print("click ok al boton login")
titulo=driver.find_element(By.CLASS_NAME,"title").text
assert titulo =="Products","el titulo products no se encuentra en ese objeto"
print("titulo Products encontrado")
imagen=driver.find_element(By.CSS_SELECTOR,'[data-test="inventory-item-sauce-labs-backpack-img"]')
assert imagen.is_displayed(),"imagen no existe"
print("imagen visible")


driver.quit()

