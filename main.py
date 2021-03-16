from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

#path chrome driver browser
driver = webdriver.Chrome(executable_path=r"")

#navigate to url
driver.get("https://extremereportbot.com/report/")
#actions
driver.find_element_by_name("extremereportbot").send_keys("" + Keys.RETURN)
driver.find_element(By.ID, "IL_SR_X1").click()
driver.implicitly_wait(10)
driver.find_element(By.ID, "user_confirm").click()
driver.find_element(By.CSS_SELECTOR, ".csgo > .option_label").click()
driver.find_element(By.CSS_SELECTOR, ".ui:nth-child(3) > label").click()
driver.find_element(By.ID, "report_confirm").click()
