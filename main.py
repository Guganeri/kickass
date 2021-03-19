from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import csv

PATH_WEBDRIVER="/home/android/Downloads/chromedriver"
WINDOW_SIZE = "1920,1080"


def report(url):
    WEB_REPORT = url
    i = 1
    while i < 11:
        print (f'Report: {i} | Meliante: {WEB_REPORT}')
        i += 1

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(PATH_WEBDRIVER, options=chrome_options)
        #driver = webdriver.Chrome(executable_path=PATH_WEBDRIVER, chrome_options=chrome_options)

        #navigate to url
        driver.get("https://extremereportbot.com/report/")
        #actions
        driver.find_element_by_name("extremereportbot").send_keys(WEB_REPORT + Keys.RETURN)
        driver.find_element(By.ID, "IL_SR_X1").click()
        driver.implicitly_wait(10)
        driver.find_element(By.ID, "user_confirm").click()
        driver.find_element(By.CSS_SELECTOR, ".csgo > .option_label").click()
        driver.find_element(By.CSS_SELECTOR, ".ui:nth-child(3) > label").click()
        driver.find_element(By.ID, "report_confirm").click()

with open('blacklist.csv', newline='') as f:

    count = 0
    reader = csv.reader(f)    
    data = list(reader)
    lenList = len(data)

    while count < lenList:     
        perfil = data[count]
        report(perfil[-1])
        print("------------------NEXT REPORT ------------------")
        count += 1

#def main():
#    #main()
#    i = 1
#    print('teste')
