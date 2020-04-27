import config
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
username = config.username

def gotoprofile(driver):
    time.sleep(5)
    try:
        search_button = driver.find_element_by_link_text(username)
        search_button.click()
    except Exception as ex:
        print('Exception while gotoprofile user profile : ',ex)
        print('alternate method / loading by url')
        driver.get(config.instagram_url+'/'+username)
    return driver

def get_following_count(driver):
    try:
        search_text=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span")
        following = search_text.text
        config.following_count = int(following)
    except Exception as ex:
        print(ex)

def get_follower_count(driver):
    try:
        search_text=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span")
        follower = search_text.text
        config.follower_count = int(follower)
    except Exception as ex:
        print(ex)

def get_post_count(driver):
    try:
        search_text=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span")
        post = search_text.text
        config.post_count = int(post)
    except Exception as ex:
        print(ex)


def get_follower_list(driver):
    time.sleep(2)
    try:
        search_button=driver.find_element_by_xpath("//a[contains(@href,'/following')]")
        search_button.click()
    except Exception as ex:
        print('Exception while loading following : ',ex)
    time.sleep(2)
    
    try:
        search_button=driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        search_button.click()
    except Exception as ex:
        print('Exception while clicking popup : ',ex)
    
    

def get_unfollowers(driver):
    time.sleep(5)
    try:
        search_button=driver.find_element_by_xpath("//a[contains(@href,'/following')]")
        search_button.click()
    except Exception as ex:
        print('Exception while loading following : ',ex)
    time.sleep(5)
    following = get_names(driver)

    try:
        search_button=driver.find_element_by_xpath("//a[contains(@href,'/followers')]")
        search_button.click()
    except Exception as ex:
        print('Exception while loading followers : ',ex)
    time.sleep(5)
    followers = get_names(driver)
    not_following_back = [user for user in following if user not in followers]
    print(len(not_following_back))
    config.follower = followers
    config.following = following
    config.unfollower = not_following_back

def get_names(driver):
    time.sleep(2)    
    scroll_box = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
    last_ht, ht = 0, 1
    while last_ht != ht:
        last_ht = ht
        time.sleep(1)
        ht = driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
    links = scroll_box.find_elements_by_tag_name('a')
    names = [name.text for name in links if name.text != '']
    # close button
    try:
        search_button=driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]")
        search_button.click()
    except Exception as ex:
        print('Exception while closeing popup : ',ex)
    return names

def initializer_follow_following_post(driver):
    get_follower_count(driver)
    get_following_count(driver)
    get_post_count(driver)
    get_unfollowers(driver)
