import time
import requests
from bs4 import BeautifulSoup
from plyer import notification


def get_score(team_name):
    search_team = team_name.split()
    search_team.append("cricket+score")
    search_team = "+".join(search_team)

    URL = f"https://www.google.com/search?q={search_team}"

    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0"}
    page = requests.get(URL, headers=header)

    soup = BeautifulSoup(page.content, 'lxml')
    scores = soup.find("div", class_="imso_mh__scr-sep")
    score_team_1 = scores.find(
        "div", class_="imspo_mh_cricket__first-score imspo_mh_cricket__one-innings-column-with-overs").text
    score_team_2 = scores.find(
        "div", class_="imspo_mh_cricket__second-score imspo_mh_cricket__one-innings-column-with-overs").text

    teams = soup.find_all(
        "div", class_="ellipsisize liveresults-sports-immersive__team-name-width kno-fb-ctx")
    team_list = []
    for t in teams:
        team_list.append(t.text)

    summary = soup.find(
        "div", class_="imso_mh__score-txt imso-ani imspo_mh_cricket__summary-sentence").text

    data = {
        "teams": team_list,
        "score_1": score_team_1,
        "score_2": score_team_2,
        "summary": summary
    }
    return data


while True:
    data = get_score("Uganda")
    notification.notify(
        title=f"{data['teams'][0]} vs {data['teams'][1]}",
        message=f"{data['teams'][0]} {data['score_1']} - {data['score_2']} {data['teams'][1]}\n{data['summary']}",
        timeout=10
    )
    time.sleep(10)
