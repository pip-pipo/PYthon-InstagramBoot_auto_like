# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time


# driver = webdriver.Firefox()

# driver.get('https://www.youtube.com/watch?v=b5jt2bhSeXs/')

# # link = driver.find_element_by_link_text("Tech With Tim")
# # link.click()

# try:
#     element=WebDriverWait(driver,10).until(
#         EC.presence_of_element_located((By.LINK_TEXT,"Tech With Tim")))
#     element.click()
#     element=WebDriverWait(driver,10).until(
#         EC.presence_of_element_located((By.ID,"textt"))
#     )
#     element.click()
# finally:
#     # driver.quit()
#     print('hello')

# ======================================================
# from selenium import webdriver

# driver = webdriver.Firefox()

# driver.get("https://instagram.com/accounts/login/")

# driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input').send_keys('pyjonathon')

# driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input]').send_keys('mdjonathon.1!')

# =========================
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time


# class InstagrameBot:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#         self.driver = webdriver.Firefox()

#     def CloseBrowser(self):
#         self.driver.close()

#     def Login(self):
#         # "//input[@name='username']"
#         driver = self.driver
#         driver.get("https://www.instagram.com/")
#         time.sleep(3)
#         user_name = driver.find_element_by_xpath("//input[@name='username']")
#         user_name.clear()
#         user_name.send_keys(self.username)
#         password = driver.find_element_by_xpath("//input[@name='password']")
#         password.clear()
#         password.send_keys(self.password)
#         password.send_keys(Keys.RETURN)
#         time.sleep(3)
#         # login_button_click=driver.find_element_by_xpath("//button[@type='submit']")
#         # login_button_click.click()
#     def Like_photos(self,hashtag):
#         driver =self.driver
#         driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
#         time.sleep(3)

#         for i in range(1, 7):
#             driver.execute("window.scrollTo(0,document.body.scrollHeight);")
#             time.sleep(3)

# Boot=InstagrameBot('pyjonathon','pyjonathon.1!')
# Boot.Login()
# Boot.Like_photos("Bangladesh")


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys


def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(3)
        user_name = driver.find_element_by_xpath("//input[@name='username']")
        user_name.clear()
        user_name.send_keys(self.username)
        password = driver.find_element_by_xpath("//input[@name='password']")
        password.clear()
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

        # gathering photos
        pic_hrefs = []
        for i in range(1, 7):
            try:
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href)
                 for href in hrefs_in_view if href not in pic_hrefs]
                # print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

        # Liking photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(2)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))

                def like_button(): return driver.find_element_by_xpath(
                    '//span[@aria-label="Like"]').click()
                like_button().click()
                for second in reversed(range(0, random.randint(18, 28))):
                    print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                    + " | Sleeping " + str(second))
                    time.sleep(1)
            except Exception as e:
                time.sleep(2)
            unique_photos -= 1


if __name__ == "__main__":

    username = "your username"
    password = "your password"

    ig = InstagramBot(username, password)
    ig.login()

    hashtags = ['amazing', 'beautiful', 'adventure', 'photography', 'nofilter',
                'newyork', 'artsy', 'alumni', 'lion', 'best', 'fun', 'happy',
                'art', 'funny', 'me', 'followme', 'follow', 'cinematography', 'cinema',
                'love', 'instagood', 'instagood', 'followme', 'fashion', 'sun', 'scruffy',
                'street', 'canon', 'beauty', 'studio', 'pretty', 'vintage', 'fierce']

    while True:
        try:
            # Choose a random tag from the list of tags
            tag = random.choice(hashtags)
            ig.like_photo(tag)
        except Exception:
            ig.closeBrowser()
            time.sleep(60)
            ig = InstagramBot(username,password)
            ig.login()
