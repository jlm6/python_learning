import requests
import json
import datetime
import easyquotation
data_list = []
diff_list = []
cryto_list = []
diff_cryto = []

def apicall(stock, KEY, target_call):
    parameters = \
        {
            'function': target_call,
            'symbol': stock,
            'apikey': KEY,
        }
    URL = "https://www.alphavantage.co/query"
    response = requests.get ( URL, params = parameters )
    data = response.json ()
    return data["Time Series (Daily)"]

def new_daily( stock, key):
    target_call = 'TIME_SERIES_DAILY'
    data = apicall(stock, key, target_call)
    message = ''
    # data_list = []
    for item in data:
        data_list.append(data[item])
    stock_info = {
        'Opening Price': float ( data_list[0]['1. open'] ),
        'Daily Highest': float ( data_list[0]['2. high'] ),
        'Daily Lowest': float ( data_list[0]['3. low'] ),
        'Closing Price': float ( data_list[0]['4. close'] ),
    }
    for k, v in stock_info.items():
        message += f"{k}: ${v}\n"
    message +=  f"Trade Volume: {data_list[0]['5. volume']}\n"

    diff_10 = round(float((float(data_list[10]['4. close']) - float(data_list[0]['4. close'])) / float(data_list[0]['4. close']))*100, 3)
    diff_30 = round(float((float(data_list[30]['4. close']) - float(data_list[0]['4. close'])) /float(data_list[0]['4. close']))*100, 3)
    diff_90 = round(float((float(data_list[90]['4. close']) - float(data_list[0]['4. close'])) /float(data_list[0]['4. close']))*100, 3)
    diff_list.extend([diff_10, diff_30, diff_90])
    day = 10
    for item in diff_list:
        if item > 0:
            message += f"% Diff {day}Days: {item}%📈\n"
        else:
            message += f"% Diff {day}Days: {item}%📉\n"
        day *= 3
    diff_list.clear()
    return message
def hkstock(stock):
    message = ''
    quotation = easyquotation.use('hkquote')
    stock = stock.zfill(5)
    data = quotation.real(stock)
    stock_info = {
        'Current Price': data[stock]['price'],
        'Today Highest': data[stock]['high'],
        'Today Lowest': data[stock]['low'],
        'Opening Price': data[stock]['openPrice']
    }
    message += f"Current Time: {data[stock]['time']}\n"
    message += f"Stock name: {stock}.HK\n"
    for key, values in stock_info.items():
        message += f"{key}: ${values}\n"
    return message

def crpto_apicall(stock, KEY, target_call):
    parameters = \
        {
            'function': target_call,
            'symbol': stock,
            'market': 'USD',
            'interval': '5min',
            'outputsize': 'full',
            'apikey': KEY,
        }
    URL = "https://www.alphavantage.co/query"
    response = requests.get ( URL, params = parameters )
    data = response.json ()
    return data["Time Series Crypto (5min)"]

def crypto_intraday(stock,key):
    message = ''
    target_call = 'CRYPTO_INTRADAY'
    data = crpto_apicall(stock, key, target_call)
    for values in data.values():
        cryto_list.append(values)
    current_info = {
        'Current_Price': cryto_list[0]['1. open'],
        'Highest_Price': cryto_list[0]['2. high'],
        'Lowest_Price': cryto_list[0]['3. low'],
    }
    message += f"Digital_Cuurency_Code: {stock.upper()}\n"
    for k, v in current_info.items():
        message += f"{k}(USD): ${v}\n"
    diff_dict = {
        'diff_30min': round(float((float(cryto_list[6]['1. open']) - float(cryto_list[0]['1. open'])) / float(cryto_list[0]['1. open']))*100, 3),
        'diff_1hr': round(float((float(cryto_list[12]['1. open']) - float(cryto_list[0]['1. open'])) / float(cryto_list[0]['1. open']))*100, 3),
        'diff_3hr': round(float((float(cryto_list[36]['1. open']) - float(cryto_list[0]['1. open'])) / float(cryto_list[0]['1. open']))*100, 3),
        'diff_6hr': round(float((float(cryto_list[72]['1. open']) - float(cryto_list[0]['1. open'])) / float(cryto_list[0]['1. open']))*100, 3),
    }
    for key, values in diff_dict.items():
        if values > 0:
            message += f"% {key}: +{values}%📈\n"
        else:
            message += f"% {key}: {values}%📉\n"

    return message
