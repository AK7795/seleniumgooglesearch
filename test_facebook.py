import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
i1 = input("enter user email : ")
i2 =input("enter password : ")
dr = webdriver.Chrome(ChromeDriverManager().install())
print("started")
dr.maximize_window()
dr.get("https://www.facebook.com/")
time.sleep(1)

dr.find_element_by_name("email").send_keys(i1)
dr.find_element_by_name("pass").send_keys(i2)
time.sleep(1)
dr.find_element_by_name("login").click()
time.sleep(10)
dr.close()
print("test case completed")