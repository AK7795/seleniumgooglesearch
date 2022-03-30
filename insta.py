import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

dr = webdriver.Chrome(ChromeDriverManager().install())
print("started")
dr.maximize_window()
dr.get("https://www.instagram.com/")
time.sleep(1)
username = input("enter user email : ")
password = input("enter password : ")
dr.find_element_by_name(username).send_keys("7795910241")
dr.find_element_by_name(password).send_keys("")
time.sleep(1)

time.sleep(6)
dr.close()
print("test case completed")