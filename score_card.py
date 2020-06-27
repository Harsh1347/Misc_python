import requests
from bs4 import BeautifulSoup
import time
from plyer import notification
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

team = input("Enter the team name : ")
driver = webdriver.Firefox(executable_path='D://GitHub//Miscellaneous_python_work//data//geckodriver.exe')
driver.get("https://www.google.com")
element = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input")
element.send_keys(team)
element.send_keys(Keys.RETURN)
time.sleep(2)
URL = driver.current_url
driver.quit()
header = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}
page = requests.get(URL,headers = header)
soup = BeautifulSoup(page.content,'lxml')
score = soup.find('div',class_="imso_mh__ma-sc-cont").text
team1 = score[0]
team2 = score[-1]
team_name = []
names = soup.find_all('div',class_="ellipsisize liveresults-sports-immersive__team-name-width kno-fb-ctx")
for n in names:
    team_name.append(n.text)
while(True):
    notification.notify(
        title = "Score Update",
        message = f"{team_name[0]} {team1} - {team2} {team_name[1]}",
        app_icon = "data\icon.ico",
        timeout = 5

        )        
    time.sleep(10)