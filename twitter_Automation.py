import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def twitter():
    username = "" # username
    password ="" # add 
    browser = webdriver.Firefox()
    browser.get('https://www.twitter.com')

    time.sleep(4)

    Login = browser.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div').click()
    time.sleep(1)
    user = browser.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input').send_keys(username)
    #time.sleep(1)
    password = browser.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input').send_keys(password)

    log = browser.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div').click()

    time.sleep(5)
    print("successful")
    browser.close()

twitter()