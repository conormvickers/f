from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.remote.webdriver import By
import selenium.webdriver.support.expected_conditions as EC  
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import os

# 80hc-36mp-ag17-kjrt
# 6j34-hbpv-kj1k-vo9i
# ctm5-q0d6-57qw-2yey

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

    chrome_prefs = {'download.default_directory' : path}
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    chrome_options.experimental_options["prefs"] = chrome_prefs

    return chrome_options

commands = [
    ["get", "https://home.personalcapital.com/page/login/goHome"],
    ["keys", "/html[1]/body[1]/div[1]/div[1]/form[2]/fieldset[1]/div[6]/div[1]/input[6]", "FukYew32" + Keys.ENTER],
    
]

backup = [
    ["keys", "/html[1]/body[1]/div[1]/div[1]/form[1]/fieldset[1]/div[2]/div[1]/input[5]", "conormvickers@gmail.com" + Keys.ENTER],
    ["keys", "/html[1]/body[1]/div[1]/div[1]/form[2]/fieldset[1]/div[6]/div[1]/input[6]", "FukYew32" + Keys.ENTER],
]

backupup = [
    ["click", "//*[text()[contains(.,'Call ')]]"],
    # ["sms", "(//input[@name='code'])[2]" ],
    ["call", "120"],
    ["keys", "//input[@name='deviceName']", "dear lord" ],
    ["keys", "//input[@type='password']", "FukYew32" + Keys.ENTER],
    ['wait', "30"]

]

downloadCSV = [
    ["get", "https://home.personalcapital.com/page/login/app#/all-transactions"],
    ["wait" "10"],
    ["click", "(//button[@title='Download transactions in CSV format'])[1]"]
    
    ]

if __name__ == "__main__":
    print("lets get started boi")

    for fname in os.listdir('.'):
                if fname.endswith('.png'):
                    os.remove("./" + fname)

    driver = webdriver.Chrome(options=set_chrome_options())
    
    logged_in = False

    def execute(command):
        driver.save_screenshot("before.png")
        if command[0] == "get":
            driver.get(command[1])
        elif command[0] == "keys":
            xpath = command[1]
            currentElement = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            driver.implicitly_wait(2)

            el = driver.find_element(By.XPATH, xpath)
            el.send_keys(command[2])
        elif command[0] == "click":
            xpath = command[1]
            currentElement = WebDriverWait(driver, 10).until(
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
            print("entering: " )
            print(sms)
            el.send_keys(sms + Keys.ENTER)
            
        elif command[0] == "wait":
            print("waiting...")
            driver.implicitly_wait(int(command[1]))
        elif command[0] == "call":
            xpath = "//input[@name='deviceName']"
            print("waiting for call...")
            i = 0
            passed = False
            while not passed and i < 60:
                passed = ("conormvickers@gmail.com" in driver.page_source)
                print(passed)
                print(i)
                i = i + 1
                time.sleep(5)
            print("after waiting")
            

        driver.save_screenshot("after.png")

    def check_if_logged_in(driver):
        try: 
            WebDriverWait(driver, 10).until( EC.title_is("Empower - Dashboard"))
            
            print("             I'M IN          " + driver.title)
            return True
        except:
            print("********** Failed to get to dashboard ***********")
            print(driver.title)
            return False
    

    for command in commands:
        try:
            print(command)
            execute(command)
        except Exception as e:
            print("!!!!!!!!!!!!!!!!!!!!!!!")
            print(e)
            print("checking if can login")
            driver.save_screenshot("error_normal.png")
            break
    
    
    logged_in = check_if_logged_in(driver)
    if not logged_in:    
        for command in backup:
            try:
                print(command)
                execute(command)
            except Exception as e:
                print("!!!!!!!!!!!!!!!!!!!!!!!")
                print(e)
                driver.save_screenshot("error.png")
                break
    logged_in = check_if_logged_in(driver)
    if not logged_in:
        for fallback in backupup:
            try: 
                print(fallback)
                execute(fallback)
            except Exception as e:
                print("!!!!!!!!!!!!!!!!!!!!!!!")
                print(e)
                driver.save_screenshot("damn.png")
                break
    logged_in = check_if_logged_in(driver)

    if logged_in:
   

        for fallback in downloadCSV:
            try: 
                print(fallback)
                execute(fallback)
            except Exception as e:
                print("!!!!!!!!!!!!!!!!!!!!!!!")
                print(e)
                driver.save_screenshot("downloaderror.png")
                break

        foundfile = False
        filename = ""
        i = 0
        while not foundfile and i < 60:
            for fname in os.listdir('.'):
                if fname.endswith('.csv'):
                    foundfile = True
                    filename = fname
            print("waiting for csv")
            i = i + 1
            time.sleep(1)
        print("found file...." + filename)
        # os.remove("./" + filename)
    print("===============COMPLETE===============")
    

    driver.close()