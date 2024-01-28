import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = ("https://www.amazon.com/Crucial-DDR4-Laptop-Memory-CT8G4SFRA32A/dp/B08C4Z69LN/ref=sr_1_4?crid=2UU5KJ45ZXBXP&dib"
       "=eyJ2IjoiMSJ9.hxnMcQH2gsHcWggDe1FI3RXsMiwqpkd6pP5XqV74jbIwBsGxoDh9gRslnZ5-YNQ_1jScU5aa2rGKnT__pTjh6w"
       ".IiWdB5KvsrG52FREIvTto8FUBh4PPBf8hdcEzHR-K8s&dib_tag=se&keywords=ram%2Bddr4%2Bfor%2Blaptop&qid=1705041401"
       "&sprefix=%2Caps%2C1045&sr=8-4&th=1")

r = requests.get(URL,
                 headers={'Accept-Language': "en-US,en;q=0.9",
                          'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                        "like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"}

                 )

print(r.status_code)
r_html = r.text
# print(r_html)


soup = BeautifulSoup(r_html, "lxml")
# print(soup.prettify())

price = soup.find(name="span", class_="a-price-whole").getText()
# print(price)
price_without_currency = price.split("$")[0]
price_as_float = float(price_without_currency)
print(price_as_float)

product_title = soup.find(id="productTitle").getText().strip().encode("ascii", "ignore")
product_title = product_title.decode()

product_price = float(price.replace("$", "").replace(",", ""))

BUY_PRICE = 20

my_gmail = "fibonaccicoder@gmail.com"
my_pwd = "rzxcuuauafzitjrk"

if price_as_float < BUY_PRICE:
    # message = f"{title} is now {price}"
    print("Message sending!")

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=my_pwd)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs=my_gmail,
            msg=f"Subject:Today Price\n\nPrice of the product:${product_price}\nLink:{URL}"
        )
    connection.close()
    print("MESSAGE SEND!!")
else:
    print("Check again your connection")

