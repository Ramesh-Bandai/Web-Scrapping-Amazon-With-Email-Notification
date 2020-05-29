#  imports
import requests
from bs4 import BeautifulSoup
import time
import smtplib

url = 'https://www.amazon.com/Apple-MWP22AM-A-AirPods-Pro/dp/B07ZPC9QD4/ref=redir_mobile_desktop?ie=UTF8&aaxitk=Zci00u2LLFiBC.yp9Rzs-g&hsa_cr_id=4185123780601&ref_=sb_s_sparkle'

# header
headers = {
    'authority': 'www.amazon.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content,'html.parser')

title = soup.find_all('h1',{'id':'title'})[0].find_all('span')[0].text.strip()
print(title)

price = soup.find_all('span',{'class':'a-size-mini twisterSwatchPrice'})[0].text.strip()
print(price)


def amazon_send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('tutorpython7@gmail.com','Yourpassword')

    subject = f'Price has fallen to {price}\n'
    message = subject + '\nThe price of ' + title + ' has fallen to ' + str(price)

    server.sendmail('tutorpyuthon7@gmail.com','bennyhinnotieno@gmail.com',message)

    server.quit()



amazon_send_email()