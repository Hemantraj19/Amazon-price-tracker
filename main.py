from bs4 import BeautifulSoup
import requests
from twilio.rest import Client

account_sid = "your account sid"
auth_token = "your auth token"

link = input("Enter the link of the product: ")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
                  "Safari/537.36"

}
response = requests.get(url=link, headers=headers)
amazon_web_page = response.text
soup = BeautifulSoup(amazon_web_page, "lxml")

title = str(soup.find(name="span", id="productTitle").getText()).strip()
price = float(str(soup.find(name="span", class_="a-price-whole").getText()).replace(",", ''))
print(f"The product is {title} with current price: Rs {price}")

min_price = int(input("At what price would you like to receive notification?: "))
print("Your notification service is set successfully, we will notify you when the price goes down.")
client = Client(account_sid, auth_token)

if price < min_price:
    message = client.messages.create(
            body=f"{title} is now Rs {price}",
            from_='number_you_got_from_twilio',
            to='your_phone_number'
        )
