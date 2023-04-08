from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service (r"C:\Users\BHAGYASHRI\Downloads\chromedriver_win32 (1)\chromedriver")
driver =webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME, "name").send_keys("Bhagyashri")
driver.find_element(By.NAME, "email").send_keys("india@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("india@123")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.ID, "inlineRadio1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Bhagya")
message = driver.find_element(By.CLASS_NAME, "alert-success ").text
print(message)
assert "Success" in message
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
driver.close()
