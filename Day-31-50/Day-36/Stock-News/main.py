import requests
import vonage.client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API = "3G4LQTSSAQJ0U0GT"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = "4aa3c7e7f1f34296a64757910b1590e1"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
#  e.g. [new_value for (key, value) in dictionary.items()]
stock_parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API,
}
response = requests.get(url=STOCK_ENDPOINT, params=stock_parameter)
# print(response.json())

data = response.json()["Time Series (Daily)"]
# print(data)
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
# print(yesterday_data)
yesterday_closing_data = yesterday_data["4. close"]
print(yesterday_closing_data)

# TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_data = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_data)

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
#  Hint: https://www.w3schools.com/python/ref_func_abs.asp""""
diff = abs(float(day_before_yesterday_closing_data) - float(yesterday_closing_data))
up_down = None
if diff > 1:
    up_down = "📉"
else:
    up_down = "📈"

print(diff)

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day
#  before yesterday.
diff_percentage = abs(round(diff / float(yesterday_closing_data) * 100))
print(diff_percentage)
# # TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(diff_percentage) > 0:
    print("Getting News")

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    # TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_parameter = {
        "apiKey": NEWS_API,
        "q": COMPANY_NAME,
    }

    response_news = requests.get(url=NEWS_ENDPOINT, params=news_parameter)
    response_news.raise_for_status()
    news_data = response_news.json()["articles"]
    # print(news_data)

    # TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint:
    #  https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_article = news_data[:3]
    # print(three_article)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

    # TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_article = [
        f"{STOCK_NAME}:{up_down}:{diff_percentage}%\nHeadline:{article['title']}.\nBrief: {article['description']}" for
        article in three_article]
    print(formatted_article)

    # TODO 9. - Send each article as a separate message via Twilio.
    for article in formatted_article:

        client = vonage.Client(key="233ec1c3", secret="hvweWeWuUARVdRI5")
        sms = vonage.Sms(client)

        responseData = sms.send_message(
            {
                "text": article,
                "from": "Vonage APIs",
                "to": "919361263166",

            }

        )
        if responseData["messages"][0]["status"] == "0":
            print("Message send successfully")
        else:
            print(f"Messages failed with error: {responseData['messages'][0]['error-text']}")
else:
    print(f"Stock price of {STOCK_NAME} {COMPANY_NAME} it doesn't make difference {diff_percentage}%")

# Optional TODO: Format the message like this:
"""TSLA: 🔺2% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey have 
gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings 
show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash. 

or "TSLA: 🔻5% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey 
have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F 
filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus 
market crash."""
