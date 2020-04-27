#importing required module
import config
import time

def login(driver):
    time.sleep(5)
    #username
    try:
        text_input = driver.find_element_by_name('username')
        text_input.send_keys(config.username)
    except Exception as ex:
        print('Exception while fetching username : ',ex)
        
    time.sleep(1)
    #Password
    try:
        text_input = driver.find_element_by_name('password')
        text_input.send_keys(config.password)
    except Exception as ex:
        print('Exception while fetching password : ',ex)

    time.sleep(1)
    #submit username and password
    try:
        search_button = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button')
        search_button.click()
    except Exception as ex:
        print('Exception while submiting',ex)    

    time.sleep(5)
    try:
        search_button = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        search_button.click()
    except Exception as ex:
        print('Exception while finding not now (initial popup) : ',ex)
    return driver

