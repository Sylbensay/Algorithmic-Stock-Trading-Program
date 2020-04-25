"""CSC 161 Project: Milestone IV Libray Extra Credit

Sylvester Benson-Sesay
Lab Section TR 12:30-1:45pm
Spring 2019
"""
# File: tradinglib.py


def main():
    '''
    This library contains four classes StockTrading,
    GetPrice, Average and State_of_Market.
    '''
    pass


class StockTrading:  # buy/sell/neither trading of stock
    def __init__(self, funds, stocks):  # initializer
        ''' gets funds and number of stocks owned '''
        self.funds = funds  # instance variables
        self.stocks = stocks
        stocks_owned = self.stocks
        cash_balance = self.funds

    def sell_stock(self, qty, price):  # sell method
        ''' sells qty number of stocks for price'''
        self.funds = self.funds + (qty*price)
        self.stocks = self.stocks - qty

    def buy_stock(self, qty, price):  # buy method
        ''' buys qty number of stocks for price'''
        self.funds = self.funds - (qty*price)
        self.stocks = self.stocks + qty

    def get_stockowned(self):  # get number of stocks
        ''' gives number of stocks owned'''
        return self.stocks

    def get_cash_balance(self):  # get balance
        ''' gives cash balance'''
        return self.funds

    def no_trade(self, qty, price):  # no trade method
        ''' do not trade qty number of stock '''
        cash_balance = self.funds
        stocks_owned = self.stocks


class GetPrice:  # fetch price from doc row
    def __init__(self, data, col):
        ''' finds the day of transaction'''
        self.data = data
        self.col = col

    def get_price(self, day):  # get day from col
        ''' gets the price from a columns open,
        high, low, close, adj close and volume'''
        line_ = self.data[day]
        line_ = line_.split(',')
        if self.col == "date":
            column = line_[0]
        elif self.col == "open":
            column = float(line_[1])
        elif self.col == "high":
            column = float(line_[2])
        elif self.col == "low":
            column = float(line_[3])
        elif self.col == "close":
            column = float(line_[4])
        elif self.col == "adj close":
            column = float(line_[5])
        elif self.col == "volume":
            column = float(line_[6])
        return column


class Average:  # finding the moving average
    def __init__(self, amt):
        ''' to calculate average'''
        self.amt = amt

    def get_average(self):  # state average
        ''' calculate average of 20 prices'''
        avrg = self.amt/20
        return avrg


class State_of_Market:  # condition of market
    def __init__(self, cost, market_value):
        ''' evaluates the market'''
        self.market_value = market_value
        self.cost = cost

    def what_to_do(self):  # decision to buy or sell or neither
        ''' decides to buy, sell or do nothing'''
        if self.cost <= self.market_value-(0.05*self.market_value):
            return 'buy'
        elif self.cost >= self.market_value+(0.05*self.market_value):
            return 'sell'
        else:
                return 'pass'
if __name__ == '__main__':
    main()
