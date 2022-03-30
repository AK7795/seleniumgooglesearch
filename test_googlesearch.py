import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
print("test case started")
driver.maximize_window()
driver.get("https://github.com/AK7795/seleniumgooglesearch/blob/master/test_googlesearch.py")
time.sleep(6)
driver.close()
print("test case completed")
