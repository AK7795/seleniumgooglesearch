import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
i1 = "7795910241"
i2 = "AKsh@7795"
print("test case started")
driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(1)
driver.find_element_by_name("q").send_keys("linkedin")
time.sleep(1)
driver.find_element_by_name("btnK").click()
#driver.get("https://www.linkedin.com/login")
time.sleep(1)
driver.find_element_by_xpath("//h3").click()
driver.find_element_by_id("email-or-phone").send_keys(i1)
time.sleep(1)
driver.find_element_by_id("password").send_keys(i2)
time.sleep(1)
#driver.find_element_by_xpath("//button[@type='submit']").click()
driver.find_element_by_id("join-form-submit").click()
time.sleep(10)
driver.close()
print("test case completed")
