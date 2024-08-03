from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

MY_EMAIL = "example@gmail.com"
MY_PASSWORD = "password"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")

time.sleep(2)
log_in_button = driver.find_element(By.XPATH, '//*[@id="q1413426407"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in_button.click()

time.sleep(2)
fb_log_in = driver.find_element(By.XPATH, '//*[@id="q-314954669"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
fb_log_in.click()

# Switch from the base window(Tinder) to the Fb Log in window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

# Put in details
time.sleep(2)
email_field = driver.find_element(By.CSS_SELECTOR, "input[id*=email]")
email_field.send_keys(MY_EMAIL)
time.sleep(1)
password_field = driver.find_element(By.CSS_SELECTOR, "input[id*=pass]")
password_field.send_keys(MY_PASSWORD, Keys.ENTER)

# Switch back to base window (Tinder)
driver.switch_to.window(base_window)

time.sleep(10)
allow_location = driver.find_element(By.XPATH, '//*[@id="q-314954669"]/div/div/div/div/div[3]/button[1]/div[2]/div[2]')
allow_location.click()

time.sleep(10)
block_notifications = driver.find_element(By.XPATH, '//*[@id="q-314954669"]/div/div/div/div/div[3]/button[2]/div[2]/div[2]')
block_notifications.click()

time.sleep(3)
accept_cookies = driver.find_element(By.XPATH, '//*[@id="q1413426407"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]/div')
accept_cookies.click()

for n in range(100):
    time.sleep(5)
    try:
        like_button = driver.find_element(By.XPATH, '//*[@id="q1413426407"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button')
        like_button.click()

    except NoSuchElementException:
        try:
            like_button = driver.find_element(By.XPATH,'//*[@id="q1413426407"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
            like_button.click()

        except NoSuchElementException:
            time.sleep(2)

    except ElementClickInterceptedException:
        # When a match happens
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        except NoSuchElementException:
                time.sleep(2)

        # When Tinder asks to put app on Home Screen
        try:
            not_interested_button = driver.find_element(By.XPATH,"//*[@id='q-314954669']/div/div/div[2]/button[2]/div[2]/div[2]/div")
            not_interested_button.click()

        except NoSuchElementException:
                time.sleep(2)

driver.quit()
