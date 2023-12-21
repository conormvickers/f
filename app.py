from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.remote.webdriver import By
import selenium.webdriver.support.expected_conditions as EC  
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

import os

def set_chrome_options() -> Options:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    path = os.getcwd()
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--user-data-dir=" + path + "/selenium")

    print("Connecting data path: " + path + "/selenium")

    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options
commands = [
    ["get", "https://home.personalcapital.com/page/login/goHome"],
    ["keys", "/html[1]/body[1]/div[1]/div[1]/form[2]/fieldset[1]/div[6]/div[1]/input[6]", "FukYew32" + Keys.ENTER],
    ["get", "https://home.personalcapital.com/page/login/app#/all-transactions"],
    ["click", "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/section[1]/div[3]/div[2]/div[1]/div[1]/div[1]/button[2]/*[name()='svg'][1]"]
]

backup = [
    ["keys", "/html[1]/body[1]/div[1]/div[1]/form[1]/fieldset[1]/div[2]/div[1]/input[5]", "conormvickers@gmail.com" + Keys.ENTER],
    ["keys", "/html[1]/body[1]/div[1]/div[1]/form[2]/fieldset[1]/div[6]/div[1]/input[6]", "FukYew32" + Keys.ENTER],
]

backupup = [
    ["click", "//*[text()[contains(.,'Text')]]"],
    ["sms", "//input[@name='code']" ],
    ["keys", "//input[@name='deviceName']", "dear lord" ],
    ["keys", "//input[@type='password']", "FukYew32" + Keys.ENTER],

]
if __name__ == "__main__":
    print("lets get started boi")
    driver = webdriver.Chrome(options=set_chrome_options())
    
    
    def execute(command):
        driver.save_screenshot("before.png")
        if command[0] == "get":
            driver.get(command[1])
        elif command[0] == "keys":
            xpath = command[1]
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
            print("entering" )
            print(sms)
            el.send_keys(sms + Keys.ENTER)
            
        elif command[0] == "wait":
            element = WebDriverWait(driver, 10).until(EC.title_contains(command[1]))
        driver.save_screenshot("after.png")


    for command in commands:
        try:
            print(command)
            execute(command)
        except Exception as e:
            print("!!!!!!!!!!!!!!!!!!!!!!!")
            print(e)
            print("checking if can login")
            driver.save_screenshot("error_normal.png")

            for command in backup:
                try:
                    print(command)
                    execute(command)
                except Exception as e:
                    print("!!!!!!!!!!!!!!!!!!!!!!!")
                    print(e)
                    driver.save_screenshot("error.png")
                    for fallback in backupup:
                        try: 
                            print(fallback)
                            execute(fallback)
                        except:
                            print("FAILURE")
                            driver.save_screenshot("damn.png")

    
    print("===============COMPLETE===============")
    # Do stuff with your driver
    input("all done?")
    driver.close()