from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.webdriver import FirefoxProfile
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True

options = Options()
options.headless = True
#options.add_argument('--profile-directory=Default')
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")

profile = FirefoxProfile(r"./Test")
# binary=r"C:\Program Files\Mozilla Firefox\firefox.exe"
# options.binary=binary
options.binary=os.environ.get("FIREFOX_BIN")                     #os.environ.get("GECKODRIVER_PATH")
browser = webdriver.Firefox(profile,capabilities=cap,options=options,executable_path=os.environ.get("GECKODRIVER_PATH"))
browser.get("https://colab.research.google.com/drive/1WOuGTFKaifStm16Cat5xQYYOHk6LAlSB#scrollTo=1oyhP-htn0J4")


print("workin")


time.sleep(50)
            

clickElement=browser.find_element_by_xpath("/html/body")
                
clickElement.send_keys(Keys.CONTROL + Keys.F9 )
time.sleep(30)


print(browser.current_url )
#clickElement=browser.find_element_by_xpath("/html/body/div[7]/div[2]/div[1]/div/colab-toolbar-button[1]")
                
#clickElement.click()

time.sleep(10)
print("Success")
time.sleep(2)
browser.quit()

