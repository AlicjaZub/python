import requests
from datetime import datetime, timedelta
import smtplib

my_email = "stocks.shares.news@gmail.com"
password = "password"

today = datetime.now()

if today.weekday() == 0:
    yesterday = today - timedelta(days=3)
else:
    yesterday = today - timedelta(days=1)

if yesterday.weekday() == 0:
    day_before_yesterday = (today - timedelta(days=4)).strftime('%Y-%m-%d')
else:
    day_before_yesterday = (today - timedelta(days=2)).strftime('%Y-%m-%d')

yesterday = yesterday.strftime('%Y-%m-%d')

message = []

companies = [("TSLA", "Tesla Inc"), ("GME", "GameStop Corporation"), ("NVDA", "NVIDIA Corporation")]

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCKS_API_KEY = "7PVKUN01D790HYEF"
NEWS_API_KEY ="0e5f5b3e6f00495a85301d2e2523ca45"

def calculate_variance(company_name):
    difference = closing_price_yesterday - closing_price_day_before_yesterday
    percantage = round(((difference / closing_price_day_before_yesterday) * 100), 2)
    difference = round(abs(difference), 2)
    
    if abs(percantage) > 3:
        
        parameters = {
            "q": company_name,
            "from": yesterday,
            "language": "en",
            "sortBy": "relevancy",
            "apiKey": NEWS_API_KEY,
        }           
        
        response = requests.get(url=NEWS_ENDPOINT, params=parameters)
        response.raise_for_status()
        data = response.json()
        message.append(f"{company_name}: {percantage}%" )
        message.append(f" - HEADLINE: {data['articles'][0]['title']}")
        message.append(f" - LINK: {data['articles'][0]['url']}")
    else:
        message.append(f"{company_name}: {percantage}%")
  

for company in companies:
  
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": company[0],
        "apikey": STOCKS_API_KEY
    }

    response = requests.get(url=STOCK_ENDPOINT, params=parameters)
    response.raise_for_status()
    data = response.json()

    closing_price_yesterday = float(data["Time Series (Daily)"][yesterday]["4. close"])
    closing_price_day_before_yesterday = float(data["Time Series (Daily)"][day_before_yesterday]["4. close"])
    
    calculate_variance(company[1])


with smtplib.SMTP("smtp.gmail.com") as connection:
    formatted = ('\n').join(message)
    connection.starttls()
    connection.login(user=my_email, password=password)
    # lower the security in mail settings
    connection.sendmail(from_addr=my_email, to_addrs="alicja@madebyon.com", msg=f"Subject:Shares and News\n\n{formatted}")
    connection.close()


