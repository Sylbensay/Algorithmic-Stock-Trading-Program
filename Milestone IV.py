"""

Sylvester Benson-Sesay

"""
# File: project.py



import random
import time
import math
from tradinglib import StockTrading, GetPrice, Average, State_of_Market

#  From milestones I - III
#  All donda descriptions comment removed except for extra credit.
#  donda description comment can be found in Milestone III.


def price_(data, day):  # selects day as a list and returns the price
        x = int(day)  # convert to int just in case otherwise
        line_ = data[x]  # index from the list == the day number
        line_ = line_.split(',')  # separate columns to a new list
        column = float(line_[4])  # selects the 'close' column
        return column  # return selected day value


def transact(funds, stocks, qty, price, buy=False, sell=False):

    if buy is False and sell is False:  # error 1 condition

        return funds, stocks

    elif buy is True and sell is True:  # error 2 condition

        return funds, stocks

    else:
        if buy is True and sell is False:  # buy stock condition
            cost = (price*qty)  # total cost of selected stock

            if cost > funds:  # insufficient funds condition

                return funds, stocks

            else:  # calculating balance and remaining stock
                cash_balance = funds - cost
                stocks_owned = stocks + qty
                return cash_balance, stocks_owned

        if sell is True and buy is False:  # selling stock condition
            cost = (price*qty)

            if qty > stocks:  # insufficient stock condition

                return funds, stocks

            else:  # calculating balance and remaining stock
                cash_balance = funds + cost
                stocks_owned = stocks - qty
                return cash_balance, stocks_owned


def alg_moving_average(filename):
    start = time.time()
    infile = open(filename, 'r')
    data = infile.readlines()
    r = 1  # starts from the first day.
    cash_balance = 1000  # principal
    stocks_owned = 0
    line = (len(data))  # number of days
    num_of_stk = line-1  # minus title
    iterations = num_of_stk - 20  # minus the first 19 numbers
    numb_buys = 0
    numb_sells = 0
    numb_notrade = 0
    for j in range(1, iterations):
        day = 0  # start with 0 when summing for avaerage
        for i in range(r, 21+r):  # moving average
            amnt = price_(data, i)
            day = day + amnt
        r = r+1  # increase the days
        avrg = day/20
        price = price_(data, 20+r)

        # buys if the current day price is 5%, or more, lower than average
        if price <= avrg-(0.05*avrg):
            cash_balance, stocks_owned = transact(cash_balance, stocks_owned,
                                                  10, price, buy=True,
                                                  sell=False)
            numb_buys = 1 + numb_buys
        # sells if the current day price is 5% higher, or more than average
        elif price > 1.05*avrg:
            cash_balance, stocks_owned = transact(cash_balance, stocks_owned,
                                                  10, price, buy=False,
                                                  sell=True)
            numb_sells = 1 + numb_sells
        # does not sell or buy when almost the same
        else:
            cash_balance, stocks_owned = transact(cash_balance, stocks_owned,
                                                  10, price, buy=False,
                                                  sell=False)
            numb_notrade = 0 + numb_notrade

    price = price_(data, iterations)  # sells all remaing stock
    owned = stocks_owned
    cash_balance, stocks_owned = transact(cash_balance, stocks_owned,
                                          stocks_owned, price, buy=False,
                                          sell=True)
    infile.close
    end = time.time()
    time_ = end - start
    return numb_buys, numb_sells, numb_notrade, time_, cash_balance, owned


def alg_mine(filename):
    start = time.time()
    cash_balance = 1000  # principal
    stocks_owned = 0
    infile = open(filename, 'r')
    data = infile.readlines()
    line = (len(data))  # number of days
    num_of_stk = line-1  # minus title
    iterations = num_of_stk - 25
    r = 1
    day = 1
    price = 0
    numb_buys = 0
    numb_sells = 0
    numb_notrade = 0

    Game_of_Thrones = {"House_Stark": ["Catelyn", "Rickon", "Sansa", "Edard",
                       "Arya", "Bran"],
                       "House_Lannister": ["Tywin", "Tyrion", "Jaime",
                                           "Cersei"],
                       "House_Targaryen": ["Daenerys", "JonSnow"]}
    Stock_per_character = {"Catelyn": 5, "Rickon": 5, "Sansa": 20, "Edard": 10,
                           "Arya": 25, "Bran": 15, "Tywin": 10, "Tyrion": 20,
                           "Jaime": 15, "Cersei": 25, "Daenerys": 0,
                           "JonSnow": 0}

    House = list(Game_of_Thrones.keys())
    People = list(Game_of_Thrones.values())

    while day <= iterations:

        choice = random.choice(House)

        if choice == House[0]:  # buy
            character = random.choice(People[0])
            Stocks = Stock_per_character[character]
            sum_price = []
            for i in range(day, day+Stocks+1):
                price = price_(data, i)
                sum_price.append(price)
                day = day + 1

            price = sum(sum_price)
            cash_balance, stocks_owned = transact(cash_balance, stocks_owned,
                                                  Stocks, price,
                                                  buy=True, sell=False)
            last_trade = 'House Lannister'
            numb_buys = numb_buys + 1

        elif choice == House[1]:  # sell
            character = random.choice(People[1])
            Stocks = Stock_per_character[character]
            sum_price = []
            for i in range(day, Stocks+day+1):
                price = price_(data, i)
                sum_price.append(price)
                day = day + 1

            price = sum(sum_price)
            cash_balance, stocks_owned = transact(cash_balance, stocks_owned,
                                                  Stocks, price,
                                                  buy=False, sell=True)
            last_trade = 'House Starks'
            numb_sells = numb_sells + 1

        else:  # neither sell nor buy
            character = random.choice(People[2])
            Stocks = Stock_per_character[character]
            sum_price = []
            for i in range(day, Stocks+day+1):
                price = price_(data, i)
                sum_price.append(price)
                day = day + 1

            price = sum(sum_price)
            cash_balance, stocks_owned = transact(cash_balance, stocks_owned,
                                                  Stocks, price,
                                                  buy=False, sell=False)
            last_trade = 'House Targaryen'
            numb_notrade = numb_notrade + 1

    price = price_(data, day)  # sells all remaing stock
    owned = stocks_owned
    cash_balance, stocks_owned = transact(cash_balance, stocks_owned,
                                          stocks_owned, price,
                                          buy=False, sell=True)
    infile.close
    end = time.time()
    time_ = end - start
    return numb_buys, numb_sells, numb_notrade, time_, cash_balance, owned



def main():
        '''
        Extra Credits
        - Compare and contrast using statistic of Moving avreage and mine
          alogrithm.
        - Used classes and object-oriented design to re-write milestones
          I,II,III.
        - Wrote a module trading.py and imported and successfull use it in
          code.
        '''
        filename = input("Enter a filename for stock data (CSV format): ")
        infile = open(filename, 'r')
        print()

        # Statistic
        moving_buys, moving_sells, moving_notrade, time_mov, cash_mov,\
            stocks_mov = alg_moving_average(filename)
        mine_buys, mine_sells, mine_notrade, time_mine, cash_mine,\
            stocks_mine = alg_mine(filename)

        # % of buys
        totalbuys = moving_buys + mine_buys
        buymoving = round(moving_buys/totalbuys*100)
        buytmine = round(mine_buys/totalbuys*100)
        print('Moving average purchased', buymoving,
              '%  of stocks and Mine had', buytmine, '%  of all purchases')

        # % of sales
        totalsale = moving_sells + mine_sells
        sellmoving = round(moving_sells/totalsale*100)
        sellmine = round(mine_sells/totalsale*100)
        print('Moving average sold', sellmoving, '%  of stock and Mine had',
              sellmine, '%  of all  sales')

        # % of no trade
        totalnotrade = moving_notrade + mine_notrade + 1
        notmoving = round(moving_notrade/totalnotrade*100)
        notmine = round(mine_notrade/totalnotrade*100)
        print('Moving average had', notmoving, '%  of no trades and Mine had',
              notmine, '%  of all no trades')

        # time difference efficiency
        t_diff = round(abs(time_mov-time_mine))
        if time_mov < time_mine:
            print('Moving average faster by', t_diff, 'sec')
        elif time_mov > time_mine:
            print('Moving average slower by', t_diff, 'sec')
        else:
            print('They are the same speed')

        # Profit efficiency
        p_diff = round(abs(cash_mov-cash_mine))
        if cash_mov < cash_mine:
            print('Moving average makes more profit by $', p_diff,
                  'cash balance')
        elif cash_mov > cash_mine:
            print('Moving average makes less profit by $', p_diff,
                  'cash balance')
        else:
            print('They have the same profit from cash balance')

        # stocks gained effieciency
        s_diff = abs(stocks_mov-stocks_mine)
        if stocks_mov < stocks_mine:
            print('Moving average had', s_diff,
                  'more stocks before the final trade')
        elif stocks_mov > stocks_mine:
            print('Moving average had', s_diff,
                  'less stocks before the final trade')
        else:
            print('They have the same number of stocks before final trade')

        # classes and object orientation
        data = infile.readlines()
        cash_balance = 1000
        stocks_owned = 0
        qty = 10
        col = 'open'
        line = (len(data))  # number of days
        num_of_stk = line-1  # minus title
        iterations = num_of_stk - 20  # minus the first 19 numbers
        r = 1
        for j in range(1, iterations):
                day = 0  # start with 0 when summing for avaerage
                for i in range(r, 21+r):  # moving average
                    amnt = GetPrice(data, col)  # called from GetPrice
                    price = amnt.get_price(i)
                    day = price + day
                r = r+1  # increase the days
                a = Average(day)  # calculate average method from Average
                avrg = a.get_average()  # method from Average
                a = int(20+r)
                price = amnt.get_price(a)  # method from GetPrice
                # method to detemine to buy or sell
                x = State_of_Market(price, avrg)
                decision = x.what_to_do()  # method makes decision
                if decision is 'buy':
                    # buy method
                    buy = StockTrading(cash_balance, stocks_owned)
                    buy.buy_stock(qty, price)
                    cash_balance, stocks_owned = buy.get_cash_balance(), \
                        buy.get_stockowned()

                elif decision is 'sell':
                    # sell method
                    sell = StockTrading(cash_balance, stocks_owned)
                    sell.sell_stock(qty, price)
                    cash_balance, stocks_owned = sell.get_cash_balance(), \
                        sell.get_stockowned()

                else:
                    # dont buy or sell
                    y = StockTrading(cash_balance, stocks_owned)
                    y.no_trade(qty, price)
                    cash_balance, stocks_owned = y.get_cash_balance(), \
                        y.get_stockowned()

        price = GetPrice(data, col)
        price.get_price(iterations)
        amnt = GetPrice(data, col)
        price = amnt.get_price(iterations)

        sell = StockTrading(cash_balance, stocks_owned)  # selling all stocks
        sell.sell_stock(stocks_owned, price)
        cash_balance, stocks_owned = sell.get_cash_balance(), \
            sell.get_stockowned()

        print()
        print("The results are", stocks_owned, "stock left",
              "${0:0.2f}".format(cash_balance), "cash balance")

if __name__ == '__main__':
    main()
