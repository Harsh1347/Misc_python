import requests
from bs4 import BeautifulSoup
import time
from plyer import notification

team = input("Enter the team name : ").lower().split()
team = "+".join(team)
print(team)
count = 0
while(True):
    URL = f"https://www.google.com/search?q={team}"
    header = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}
    page = requests.get(URL,headers = header)
    
    soup = BeautifulSoup(page.content,'lxml')
    try:
        match_time = soup.find('span',class_ = "imso_mh__ft-mtch imso-medium-font imso_mh__ft-mtchc").text
    except:
        match_time = soup.find('span',class_="liveresults-sports-immersive__game-minute").text
    
    
    score = soup.find('div',class_="imso_mh__ma-sc-cont").text
    team_name = []
    names = soup.find_all('div',class_="ellipsisize liveresults-sports-immersive__team-name-width kno-fb-ctx")
    for n in names:
        team_name.append(n.text)

    if match_time == "Full-time":
        team1 = score[0]
        team2 = score[-1]
        notification.notify(
            title = "Score Update",
            message = f"FULL-TIME \n{team_name[0]} {team1} - {team2} {team_name[1]}",
            app_icon = "data//football.ico",
            timeout = 10)
        break

    if match_time == "Half-time":
        team1 = score[0]
        team2 = score[-1]
        notification.notify(
            title = "Score Update",
            message = f"HALF-TIME \n{team_name[0]} {team1} - {team2} {team_name[1]}",
            app_icon = "data//football.ico",
            timeout = 10)
        time.sleep(600)

    if count ==0:
        team1 = score[0]
        team2 = score[-1]
        count+=1
        notification.notify(
            title = "Score Update",
            message = f"{team_name[0]} {team1} - {team2} {team_name[1]} \n {match_time} mins ",
            app_icon = "data//football.ico",
            timeout = 5

            )
    else:
           
        if team1 != score[0] or team2 !=score[-1]:
            team1 = score[0]
            team2 = score[-1]
            notification.notify(
                title = "Score Update",
                message = f"{team_name[0]} {team1} - {team2} {team_name[1]} \n {match_time} mins ",
                app_icon = "data//football.ico",
                timeout = 5

                    )
    time.sleep(10)