import requests
from bs4 import BeautifulSoup
import smtplib
import time

#URL = input("Enter the Url:")
#URL = URL.strip()
#CurPrice = input('Enter the current price:')
CurPrice = float(34000)


URL = 'https://www.amazon.in/Test-Exclusive-608/dp/B07HGBMJT6/ref=sr_1_1?keywords=oneplus&qid=1562392047&s=gateway&smid=A35FCS7U51TK3C&sr=8-1'
header = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}
#print(URL)
def check_price():
    page = requests.get(URL,headers = header)
    
    soup = BeautifulSoup(page.content,'lxml')
    
    print("")
    
   #price = soup.find('td',class_='a-span12')
    price = soup.find('tr',id = 'priceblock_ourprice_row').find('span').text
    print(price)
    price = price[2:] 
    
    price = price.replace(",", "")
    
    price = price.strip()
    
    converted_price = float(price)
       
    #print(converted_price)
    
    if (converted_price) < CurPrice:
        send_mail()
    else:
        print('NO PRICE DROP')
    
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('harshvai07@gmail.com','pmypizfrsvbbzfrq')
    
    subject = 'Price'
    
    body = URL
    
    msg = f"Subject : {subject}\n\n{body}"
    
    server.sendmail('harshvai07@gmail.com','harshapj2@hotmail.com',msg)
    
    print('E-MAIL HAS BEEN SENT')
    
    server.quit()
    
check_price()
#while(True):

    #time.sleep(86400)