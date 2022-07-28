import time  # Importing necessary modules

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "Path to chromedriver.exe"  # Make sure to edit this to your path
driver = webdriver.Chrome(executable_path=PATH)

driver.get("https://www.instagram.com/")


def user_name():  # This function will type your username into username field
    username = driver.find_element("name", "username")
    username.send_keys(Keys.RETURN)
    username.send_keys("<>Your username here<>")


def pass_word():  # This function will type your password into password field
    password = driver.find_element("name", "password")
    password.send_keys(Keys.RETURN)
    password.send_keys("<>Your password here<>")
    password.send_keys(Keys.RETURN)


user_name()
time.sleep(3)  # Increase the time here if your Internet is bit slow
pass_word()
time.sleep(3)
