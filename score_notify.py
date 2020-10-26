import requests
from bs4 import BeautifulSoup #pip install beautifulsoup4

team_name = input("Enter the team name:").lower().split()
team_name = "+".join(team_name)
print(team_name)
URL = f"https://www.google.com/search?q={team_name}"
HEADER = {"user_agenet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}
page = requests.get(URL,headers = HEADER)
print(page)