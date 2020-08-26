from abc import ABC

# Omitted:
# - Change
# - % Change
# - Volume
# - Open Interest

class Option(ABC):
    def __init__(self, name, strike, last_trade, last_price, bid, ask, implied_vol):
        self.name = name
        self.strike = strike
        self.last_trade = last_trade
        self.last_price = last_price
        self.bid = bid
        self.ask = ask
        self.implied_vol = implied_vol

    def value_at_maturity(self, value):
        return 0

class CallOption(Option):
    def __init__(self, name, strike, last_trade, last_price, bid, ask, implied_vol):
        super().__init__(name, strike, last_trade, last_price, bid, ask, implied_vol)
    
    def value_at_maturity(self, spot):
        return max(spot - self.strike, 0)

class PutOption(Option):
    def __init__(self, name, strike, last_trade, last_price, bid, ask, implied_vol):
        super().__init__(name, strike, last_trade, last_price, bid, ask, implied_vol)

    def value_at_maturity(self, spot):
        return max(self.strike - spot, 0)