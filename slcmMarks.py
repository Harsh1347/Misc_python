import requests
from bs4 import BeautifulSoup
import mechanize
import pytesseract
import cv2

BASE_URL = "https://slcm.manipal.edu/"
homeUrl = "https://slcm.manipal.edu/loginForm.aspx"
acadsUrl = "https://slcm.manipal.edu/Academics.aspx"
credentials = {
    'txtUserid': "",
    'txtpassword': ""
}
action = "./loginForm.aspx"

# s = requests.session()
# page = s.get(homeUrl)
pytesseract.pytesseract.tesseract_cmd = ".//Tesseract-OCR//tesseract.exe"


# cname = list(s.cookies.get_dict().keys())[0]
# cvalue = list(s.cookies.get_dict().values())[0]


response = []
browser = mechanize.Browser()
login = browser.open(homeUrl)
print(login)
soup = BeautifulSoup(login.read(), 'html.parser')
img = (soup.find('img', id="imgCaptcha"))
final_url = BASE_URL+str(img.get('src'))
response = requests.get(final_url)
if response.status_code == 200:
    print("yay")
    with open(f".//filename{1}.jpg", 'wb') as f:
        f.write(response.content)
else:
    print("booo")


img = cv2.imread(f'.//filename{1}.jpg', 0)
text = pytesseract.image_to_string(img)
CODE = text.strip()
browser.select_form(name='form1')
browser.form['txtUserid'] = '170907514'
browser.form['txtpassword'] = ""
browser.form['txtCaptcha'] = CODE
browser.method = "POST"
ress = browser.submit()
xx = browser.open(acadsUrl)
yy = xx.read()
soup = BeautifulSoup(yy, 'html.parser')
# print(soup.prettify())
div = soup.find('div', {'id': 'accordion'})
sub_names = [sub.text for sub in soup.find_all(
    'a', {'data-parent': '#accordion'})]
sub_names = [sub.split('\n')[2] for sub in sub_names]
sub_names = [' '.join(s.split(' ')[4:]) for s in sub_names]
sub_names = [s[1:] for s in sub_names]
sub_names = [i.strip() for i in sub_names]
sub_marks = soup.find_all(
    'td', style="border-collapse: collapse; border: 1px solid black; text-align: center")
print(sub_names)

for k, sub in enumerate(sub_marks):

    for i in sub:
        response.append(i)
