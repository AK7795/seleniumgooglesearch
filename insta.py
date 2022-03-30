import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

dr = webdriver.Chrome(ChromeDriverManager().install())
print("started")
dr.maximize_window()
dr.get("https://www.instagram.com/")
time.sleep(1)
i1 = input("enter user email : ")
i2 = input("enter password : ")
dr.find_element_by_name('username').send_keys(i1)
dr.find_element_by_name('password').send_keys(i2)
time.sleep(1)

time.sleep(10)
dr.close()
print("test case completed")