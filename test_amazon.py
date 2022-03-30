import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
i = input("enter product name : ")
dr = webdriver.Chrome(ChromeDriverManager().install())
print("started")
dr.maximize_window()
dr.get("https://www.amazon.in/")
time.sleep(1)

dr.find_element_by_id("twotabsearchtextbox").send_keys(i)
#dr.find_element_by_name('password').send_keys()
time.sleep(1)
dr.find_element_by_id("nav-search-submit-button").click()
time.sleep(60)
dr.close()
print("test case completed")