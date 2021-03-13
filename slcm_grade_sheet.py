from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests
import time
import cv2
import numpy
import pytesseract
import random

V = random.randint(0, 1000)

headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
}

s = requests.session()
s.headers.update(headers)


pytesseract.pytesseract.tesseract_cmd = ".//Tesseract-OCR//tesseract.exe"

BASE_URL = "https://slcm.manipal.edu/"

USERNAME = '<USERNAME>'
PASSWORD = '<PASSWORD>'

browser = webdriver.Firefox()
browser.get(BASE_URL)

for cookie in browser.get_cookies():
    c = {cookie['name']: cookie['value']}
    s.cookies.update(c)


img = browser.find_element_by_id('imgCaptcha')
img_src = img.get_attribute("src")

final_url = str(img_src)

response = s.get(final_url)

if response.status_code == 200:
    with open(f".filename{V}.jpg", 'wb') as f:
        f.write(response.content)

img = cv2.imread(f'.//filename{V}.jpg', 0)

time.sleep(2)
text = pytesseract.image_to_string(img)
CODE = text.strip()
# print(CODE)

username = browser.find_element_by_id('txtUserid')
password = browser.find_element_by_id('txtpassword')
code = browser.find_element_by_id('txtCaptcha')

username.send_keys(USERNAME)
password.send_keys(PASSWORD)
code.send_keys(CODE)

browser.find_element_by_id('btnLogin').click()
time.sleep(3)
browser.find_element_by_id('rtpchkMenu_lnkbtn2_1').click()
time.sleep(3)
browser.find_element_by_xpath(
    '/html/body/div[3]/form/div[5]/div/div/div/div[1]/div[2]/ul/li[7]/a/span').click()
time.sleep(3)
browser.switch_to.window(browser.window_handles[1])
time.sleep(2)
browser.find_element_by_xpath(
    '/html/body/div[3]/form/div[5]/div/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div[2]/select/option[8]').click()
