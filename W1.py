
from selenium import webdriver
# import os
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.headless = True
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("user-agent=what")
chrome_options.add_argument("user-data-dir=selenium") 
curl="https://colab.research.google.com/drive/1WOuGTFKaifStm16Cat5xQYYOHk6LAlSB#scrollTo=1oyhP-htn0J4"

browsers = None
import pickle



def Initialize():
    global Instance
    browsers = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe',options=chrome_options)
    browsers.implicitly_wait(5)
    return browsers

def CloseDriver(br):
    browsers=br
    browsers.quit()


def main():
    browser=Initialize()

    browser.get(curl)

 
    try:
        try:
            
            print("hellow")
            input_email=browser.find_element_by_id("Email")
            input_email.send_keys("movieverse.gdbot.1@gmail.com")
            
            next_button=browser.find_element_by_id("next") 
            
            next_button.send_keys(Keys.ENTER)
            
            time.sleep(5)
            input_password=browser.find_element_by_id("password") 
            input_password.send_keys("Gb12341234")
            
            next_button=browser.find_element_by_id("submit") 
            next_button.send_keys(Keys.ENTER)
        except:
            
            time.sleep(20)
            # ex=browser.get_cookies()
            # pickle.dump(ex ,pickle_out )
            # pickle_out.close()
               
            clickElement=browser.find_element_by_xpath("/html/body")
            
            clickElement.send_keys(Keys.CONTROL + Keys.F9 )
            
            time.sleep(30)
            
            print("start")
            browser.switch_to.frame(browser.find_elements_by_tag_name('iframe')[1])
            
            #clickElement.send_keys(Keys.ENTER)
            
            href=browser.find_element_by_xpath("/html/body/div/span[2]/pre/a").get_attribute('href')
            
            browser.execute_script("window.open('');")
            #browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
            browser.switch_to.window(browser.window_handles[1])
            browser.get(href)
            #browser.get(href)
            time.sleep(5)
            
            choose_account=browser.find_element_by_id("choose-account-0")
            
            choose_account.click()
            
            time.sleep(5)
      
            allow_button=browser.find_element_by_id("submit_approve_access")
            
            allow_button.click()
            
            time.sleep(10)
            text_code=browser.find_element_by_tag_name("textarea").get_attribute("textContent")
            
    
            browser.switch_to.window(browser.window_handles[0])
            
            browser.switch_to.frame(browser.find_element_by_xpath("/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/div/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div/iframe"))
            
            time.sleep(5)
            code_input=browser.find_element_by_xpath("/html/body/div/span[2]/pre/input")
            
            code_input.send_keys(text_code)
            code_input.send_keys(Keys.ENTER)
            
            time.sleep(60)
            CloseDriver(browser)
            Status="Pass"
            print(Status)
    except Exception as e:
        print(e)
        Status=e
        
main()

'''
        inputElement=browser.find_element_by_xpath("/html/body/div/span[2]/pre/input")
        inputElement.send_keys("akshayrameshwar2018@gmail.com")'''