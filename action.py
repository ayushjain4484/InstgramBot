import config
import time
import random
import sys
from selenium.webdriver.remote.webelement import WebElement

def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


def like_photo(driver, hashtag):
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

        # gathering photos
        pic_hrefs = []
        for i in range(1, 7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                # print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

        # Liking photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(5)
            print('opened photo')
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 10))
                print('capture like button')
                #like_button = driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
                like_button = driver.find_element_by_xpath('//span/button')
                #like_button.click()
                like_button.send_keys("\n")
                #driver.execute_script("arguments[0].click();", like_button)
                time.sleep(2)
                print('clicked like button')
                time.sleep(random.randint(2, 4))
                for second in reversed(range(0, random.randint(18, 28))):
                    print("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                    + " | Sleeping " + str(second))
                    time.sleep(1)
            except Exception as e:
                print('Exception: ',e)
            unique_photos -= 1



def comment_like_photo(driver, hashtag, comments):
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)
        # gathering photos
        pic_hrefs = []
        for i in range(1, 7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                # print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

        # Liking photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(5)
            print('opened photo')
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            comment = 0
            
            #like photo
            try:
                time.sleep(random.randint(2, 10))
                print('capture like button')
                like_button = driver.find_element_by_xpath('//span/button')
                #like_button.click()
                like_button.send_keys("\n")
                #driver.execute_script("arguments[0].click();", like_button)
                time.sleep(2)
                print('clicked like button')
                time.sleep(random.randint(2, 4))
                for second in reversed(range(0, random.randint(18, 28))):
                    print("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                    + " | Sleeping " + str(second))
                    time.sleep(1)
            except Exception as e:
                print('Exception: ',e)
            
            #Comment:
            
            #randomization for comment
            random_num = random.randint(2, 100)
            if random_num%config.comment_freq == 1:
                comment_flag = 1
            else:
                comment_flag = 0
            driver.get(pic_href)
            time.sleep(4)

            comment = random.choice(comments)

            driver.get(pic_href)
            time.sleep(5)
            print('entering comment section')
            ###########################driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            #commenting section
            if comment_flag == 1:
                try:
                    time.sleep(random.randint(2, 10))                
                    print('capturing comment sectiion')
                    #comment_area = driver.find_element_by_tag_name('textarea')
                    comment_area = driver.find_element_by_tag_name('textarea')
                    comment_area.click()
                    time.sleep(2)
                    print('clicked comment')                
                    #comment_area.send_keys(comment)
                    #driver.execute_script('document.querySelector("textarea.Ypffh").innerText = '+'\"'+str(comment)+'\"')
                    comment_area = driver.find_element_by_tag_name('textarea')
                    comment_area.send_keys(comment)
                    time.sleep(2)
                    print('commented: ',comment)
                    print('capturing post')
                    post_button = driver.find_element_by_xpath('//form/button')
                    post_button.click()
                    print('clicked post')
                    time.sleep(3)
                    #comment_area.send_keys("\n")
                    #driver.execute_script("arguments[0].click();", like_button)
                    time.sleep(2)
                
                    time.sleep(random.randint(2, 4))
                except Exception as e:
                    print('Exception: in comment section ',e)

            unique_photos -= 1