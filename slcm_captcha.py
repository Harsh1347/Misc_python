import requests
from bs4 import BeautifulSoup
import time

BASE_URL = "https://slcm.manipal.edu/"
header = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}

for i in range(100):
    
    s = requests.session()
    page = s.get(BASE_URL,headers = header)
    soup = BeautifulSoup(page.content,'lxml')

    img = (soup.find('img',id = "imgCaptcha"))

    final_url = BASE_URL+str(img.get('src'))
    print(final_url)

    response = s.get(final_url)
    print(response.status_code)
    if response.status_code == 200:
        with open(f"C:\\Users\\Admin\\desktop\\captcha\\captcha{i}.jpg", 'wb') as f:
            f.write(response.content)