from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

__data_columns = [
    'Contract Name', 
    'Last Trade', 
    'Last Price', 
    'Bid', 
    'Ask', 
    'Change', 
    '% Change', 
    'Volume', 
    'Open Interest', 
    'Implied Volatility'
]

def validate_ticker(ticker):
    req = requests.get(f'https://finance.yahoo.com/quote/{ticker}/options')
    soup = BeautifulSoup(req.content, 'html.parser')    
    date_div = soup.find('div', class_='option-contract-control')
    return date_div != None

def get_maturities(ticker):
    req = requests.get(f'https://finance.yahoo.com/quote/{ticker}/options')
    soup = BeautifulSoup(req.content, 'html.parser')    
    date_div = soup.find('div', class_='option-contract-control')
    
    maturities = []
    for option in date_div.contents[0].contents:
        maturities.append((option.text, option.attrs['value']))
    
    return maturities

def __get_page(ticker, maturity_value):
    req = requests.get(f'https://finance.yahoo.com/quote/{ticker}/options?date={maturity_value}')
    return BeautifulSoup(req.content, 'html.parser')

def __parse_options_table(table):
    prices, options = [], []

    for option in table:
        index, info = 0, []

        for data in option.find_all('td'):
            if index == 2:
                prices.append(data.text)
            else:
                info.append(data.text)
            
            index += 1
        
        options.append(info)
    
    return pd.DataFrame(np.array(options), index=prices, columns=__data_columns)

def get_calls(ticker, maturity_value):
    table = __get_page(ticker, maturity_value).find('table', class_='calls').find('tbody').find_all('tr')
    return __parse_options_table(table)

def get_puts(ticker, maturity_value):
    table = __get_page(ticker, maturity_value).find('table', class_='puts').find('tbody').find_all('tr')
    return __parse_options_table(table)

def get_all_calls(ticker):
    maturities = get_maturities(ticker)

    calls = {}
    for _, value in maturities:
        calls[value] = get_calls(ticker, value)
    
    return calls

def get_all_puts(ticker):
    maturities = get_maturities(ticker)

    puts = {}
    for _, value in maturities:
        puts[value] = get_puts(ticker, value)

    return puts