class Strategy:
    def __init__(self, options=[]):
        self.options = options
    
    # Add payoff value thing
    def value_at_maturity(self, spot):
        return sum([option.value_at_maturity(spot) for option in self.options])
    
    def add_option(self, option):
        self.options.append(option)