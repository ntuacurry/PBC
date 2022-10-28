from selenium import webdriver
import time

Edgedriver_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe"
driver = webdriver.Edge(Edgedriver_path)
driver.get("https://www.facebook.com/MgkLifeFun/")
driver.close()
