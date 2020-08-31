from bs4 import BeautifulSoup
from functools import lru_cache
from enum import Enum
import requests

class Maturity(Enum):
    M1 = 0
    M2 = 1
    M3 = 2
    M6 = 3
    Y1 = 4
    Y2 = 5
    Y3 = 6
    Y5 = 7
    Y7 = 8
    Y10 = 9
    Y20 = 10
    Y30 = 11

@lru_cache(maxsize=1)
def __fetch_risk_free_rates():
    req = requests.get('https://www.treasury.gov/resource-center/data-chart-center/interest-rates/pages/textview.aspx?data=yield')
    soup = BeautifulSoup(req.content, 'html.parser')

    rs = {}
    rates = soup.find('table', class_='t-chart').find_all('tr')[-1].find_all('td')[1:]
    for i in range(len(rates)):
        key = Maturity(i)
        rs[key] = rates[i].text
    
    return rs

@lru_cache(maxsize=12)
def get_risk_free_rate(maturity):
    if not isinstance(maturity, Maturity):
        raise Exception('maturity is not of type Maturity')
    
    risk_free_rates = __fetch_risk_free_rates()
    return risk_free_rates[maturity]