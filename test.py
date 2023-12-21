from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import os as os

debug_test_path = ".\\python\\debug.txt"

try:
    service = Service(executable_path=r"C:\Users\cmv025\drivers\chromedriver.exe")
    options = webdriver.ChromeOptions()
    # options.add_argument("--no-sandbox")
    if os.path.exists(debug_test_path):
        print("Debug, no headless")
    else:
        print("In Production")
        options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    # options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=service, options=options)
except Exception as e:
    print(e)


commands = [
    ["get", "https://jefferson.workspaceoneaccess.com/authcontrol/auth/request"],
    ["keys", "//input[@name='username']", ("cmv025" + Keys.ENTER)],
    ["keys", "//input[@name='loginfmt']", ("cmv025@jefferson.edu" + Keys.ENTER)],
    ["keys", "//input[@name='passwd']", ("6yhn^YHN6yhn^YHN" + Keys.ENTER)],
    ["keys", "//input[@value='Sign in']", (Keys.ENTER)],
    ["wait", "Favorites"],
    [
        "get",
        "https://tjuv-my.sharepoint.com/personal/jxl127_jefferson_edu/_layouts/15/onedrive.aspx?FolderCTID=0x01200080B2CF5B82497D439E9E614BA118A379&id=%2Fpersonal%2Fjxl127%5Fjefferson%5Fedu%2FDocuments%2F1%2DBook",
    ],
    ["click", "//div[@title='!ReadyForUpload']"],
    ["click", '//i[@data-icon-name="More"]'],
    ["click", '//button[@name="Download"]'],
]


def execute(command):
    if command[0] == "get":
        driver.get(command[1])
    if command[0] == "keys":
        xpath = command[1]
        currentElement = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        driver.implicitly_wait(10)

        el = driver.find_element(By.XPATH, xpath)
        el.send_keys(command[2])
    if command[0] == "click":
        xpath = command[1]
        currentElement = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        driver.implicitly_wait(10)

        el = driver.find_element(By.XPATH, xpath)
        el.click()
    if command[0] == "wait":
        element = WebDriverWait(driver, 10).until(EC.title_contains(command[1]))


for command in commands:
    try:
        print(command)
        execute(command)
    except Exception as e:
        print("!!!!!!!!!!!!!!!!!!!!!!!")
        print(e)

print("===============COMPLETE===============")

while True:
    a = input("next command type?\n")
    b = input("path?\n")
    command = [a, b]
    execute(command)
