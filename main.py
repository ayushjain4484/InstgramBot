#importing
import config, login, accountinfo, action
import time
from selenium import webdriver
from time import sleep
import random
#initialize local variable
#config.init()

#setting up driver
driver_path = config.driver_path

#getting chrome started
driver = webdriver.Chrome(executable_path=driver_path)
driver.maximize_window()
#get url
driver.get(config.instagram_url)

#login
login.login(driver)

#profile page
accountinfo.gotoprofile(driver)

#get unfollowers
#accountinfo.get_unfollowers(driver)
time.sleep(2)
#accountinfo.initializer_follow_following_post(driver)
#print('post: ',config.post_count)
#print('follower: ',config.follower_count)
#print('following: ',config.following_count)
#print('follower: ',len(config.follower))
#print('following: ',len(config.following))
#print('unfollower: ',len(config.unfollower))

hashtag = random.choice(config.hashtags)
comments = config.comments
#action.like_photo(driver,hashtag)
action.comment_like_photo(driver, hashtag, comments)