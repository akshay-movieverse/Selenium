from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.webdriver import FirefoxProfile
options = Options()
options.headless = True
#options.add_argument('--profile-directory=Default')

profile = FirefoxProfile(r"./Test")

#options.add_argument("--user-data-dir=selenium")
browser = webdriver.Firefox(profile,options=options,executable_path='geckodriver.exe')
browser.get("https://colab.research.google.com/drive/1WOuGTFKaifStm16Cat5xQYYOHk6LAlSB#scrollTo=1oyhP-htn0J4")


print("workin")


time.sleep(10)
            

# clickElement=browser.find_element_by_xpath("/html/body")
                
# clickElement.send_keys(Keys.CONTROL + Keys.F9 )
time.sleep(2)
browser.quit()

