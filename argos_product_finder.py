
from marshal import load
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.options import Options
import logging
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

from time import sleep


driver = webdriver.Firefox(executable_path=r'C:\\Users\\Toshiba\\Documents\\Hiresh Personal Work\\Programming\\pythonFiles\\webscrapingprojects\\geckodriver.exe')
driver.get("https://www.argos.co.uk/")

driver.implicitly_wait(10)

#Accepting Cookies Pop-up

accept_cookies_button = driver.find_element_by_id("consent_prompt_submit")
accept_cookies_button.click()

#Locate search bar and input 'Iphone 11 64GB'

search_bar = driver.find_element_by_id("searchTerm")
search_bar.send_keys("Iphone 11 64GB")

search_bar_button = driver.find_element_by_class_name("_2mKaC")
search_bar_button.click()

#Choose product

product = driver.find_element_by_xpath("//a[@aria-labelledBy = 'product-title-2153591']")
product_link = product.get_attribute("href")
driver.get(product_link)
 
#Add to trolley

add_to_trolley = driver.find_element_by_xpath("//button[@data-test='add-to-trolley-button-button']")
add_to_trolley.click()

continue_shopping_button = driver.find_element_by_xpath("//button[@class='Buttonstyles__Button-sc-42scm2-2 fyVwdD']")
continue_shopping_button.click()
