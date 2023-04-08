from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service (r"C:\Users\BHAGYASHRI\Downloads\chromedriver_win32 (1)\chromedriver")
driver =webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client/")
driver.maximize_window()
#driver.find_element(By.CLASS_NAME, "forgot-password-link").click()
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
#Xpath - parent to child
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("abc@gmail.com")
#CSS_SELECTOR - parent to child
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input ").send_keys("abc@123")
driver.find_element(By.ID, "confirmPassword").send_keys("abc@123")
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
driver.close()