
from time import time
from requests import options
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
# import threading

screen = int(input("How Many Extra Screen you want:"))
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome()

driver.get("https://www.youtube.com/watch?v=83ugsNZcpeo")
for i in range(screen):
    driver.switch_to.new_window('window')
    driver.get("https://www.youtube.com/watch?v=83ugsNZcpeo")

numberofwindows = driver.window_handles
while True:
    
    for i in range(len(numberofwindows)):
        driver.switch_to.window(driver.window_handles[i])
        time.sleep(random.randint(15,30))
        driver.refresh()