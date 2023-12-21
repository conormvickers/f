import time
import logging
# logging.basicConfig(level=0)
import json
import pickle

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webdriver import By
import selenium.webdriver.support.expected_conditions as EC  # noqa
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.109/win64/chromedriver-win64.zip

import undetected_chromedriver as uc


#    //*[text()[contains(.,'ABC')]]
commands = [
    ["get", "https://home.personalcapital.com/page/login/goHome"],
    # ["keys", "//input[@name='username']", "conormvickers@gmail.com" + Keys.ENTER],
    # ["click", "//*[text()[contains(.,'Text')]]"],
    # ["sms", "//input[@type='text']"]
]




def main(args=None):
    # capabilities = DesiredCapabilities.CHROME
    # capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
    options = uc.ChromeOptions()
    options.user_data_dir = "selenium"
    driver = uc.Chrome(options = options )



    # driver = webdriver.Chrome(service=service)
    
    def execute(command):
        driver.save_screenshot("before.jpeg")
        if command[0] == "get":
            driver.get(command[1])
        elif command[0] == "keys":
            xpath = command[1]
            time.sleep(3)
            currentElement = WebDriverWait(driver, 50).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            driver.implicitly_wait(2)

            el = driver.find_element(By.XPATH, xpath)
            el.send_keys(command[2])
        elif command[0] == "click":
            print(command)
            xpath = command[1]
            currentElement = WebDriverWait(driver, 50).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            driver.implicitly_wait(2)

            el = driver.find_element(By.XPATH, xpath)
            el.click()
        elif command[0] == "frame":
            xpath = command[1]

            frame = driver.find_element(By.XPATH, xpath)
            driver.switch_to.frame(frame)
        elif command[0] == "sms":
            sms = input("SMS Code?")
            xpath = command[1]
            el = driver.find_element(By.XPATH, xpath)
            el.send_keys(sms)
            
        elif command[0] == "wait":
            element = WebDriverWait(driver, 10).until(EC.title_contains(command[1]))
        driver.save_screenshot("after.jpeg")


    for command in commands:
        try:
            # print(command)
            # log = driver.get_log("performance")
            # if "Wbb_csrf" in log: 
            #     ind = log.index("Wbb_csrf")
            #     print(log[ind:ind + 30] )
            execute(command)
        except Exception as e:
            print("!!!!!!!!!!!!!!!!!!!!!!!")
            print(e)
    
    asdf = input("done?")

    print("===============COMPLETE===============")
    
    

if __name__ == "__main__":
   
    main()