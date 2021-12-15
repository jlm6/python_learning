def daily(stock, KEY):
    parameters = \
        {
        'function': 'TIME_SERIES_DAILY',
        'symbol': 'GOOG',
        'apikey': API_KEY,
        }
    today = datetime.date.today()
    yesterday = str(today - datetime.timedelta(days=1))

    URL = "https://www.alphavantage.co/query"
    response = requests.get(URL, params = parameters)
    data = response.json()

    stock_info = {
        'Opening Price': float(data["Time Series (Daily)"][yesterday]['1. open']),
        'Daily Highest': float(data["Time Series (Daily)"][yesterday]['2. high']),
        'Daily Lowest': float(data["Time Series (Daily)"][yesterday]['3. low']),
        'Closing Price': float(data["Time Series (Daily)"][yesterday]['4. close']),
    }
    for key, values in stock_info.items():
        print(f"{key}: ${values}")
    print("Trade Volume: ", int(data["Time Series (Daily)"][yesterday]['5. volume']))