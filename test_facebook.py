import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

dr = webdriver.Chrome(ChromeDriverManager().install())
print("started")
dr.maximize_window()
dr.get("https://www.facebook.com/")
time.sleep(1)
dr.find_element_by_name("email").send_keys("ABC")
dr.find_element_by_name("pass").send_keys("XYZ")
time.sleep(1)
dr.find_element_by_name("login").click()
time.sleep(6)
dr.close()
print("test case completed")