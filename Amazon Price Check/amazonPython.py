import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/Corsair-2x16GB-3200MHz-Memory-CMK32GX4M2B3200C16/dp/B016ORTNI2/ref=sr_1_1?keywords=32+gb+ram+ddr+3200&qid=1563853588&s=gateway&sr=8-1'

headers = { "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

def check_price():
	page = requests.get(URL, headers=headers)

	soup = BeautifulSoup(page.content, 'html.parser')
	soup2 = BeautifulSoup(soup.prettify(), 'html.parser')

	title = soup2.find(id="productTitle").get_text()

	price = soup2.find(id="priceblock_ourprice").get_text()
	converted_price = float(price[1:7])

	if(converted_price < 154.99):
		send_mail()
	#print(title.strip())
	#print(converted_price)

def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('sun.victor99@gmail.com', 'xqibpfnoxpesmbdb')

	subject = 'Price has went down!'
	body = 'Check the Amazon link: https://www.amazon.com/Corsair-2x16GB-3200MHz-Memory-CMK32GX4M2B3200C16/dp/B016ORTNI2/ref=sr_1_1?keywords=32+gb+ram+ddr+3200&qid=1563853588&s=gateway&sr=8-1'

	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail(
		'sun.victor99@gmail.com',
		'sun.victor99@gmail.com',
		msg
	)
	print("Message has been sent")

	server.quit()


check_price()