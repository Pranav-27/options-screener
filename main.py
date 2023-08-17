from yahoo_fin import options
import yahoo_fin.stock_info as si
import pandas as pd

def findPlays(capital, winrate, risk, expiration):
    #pd.set_option('display.max_columns', None)

    chain = options.get_options_chain('AAPL')
    q = si.get_quote_table('AAPL')
    print(q)

def validateExpiration(expiration):
    if len(expiration) != 10 or not (expiration[4] == '-' and expiration[7] == '-'):
        return False
    i = 0
    for i in range(0, 4):
        if not expiration[i].isdigit():
            return False
    i += 1
    for i in range(0, 2):
        if not expiration[i].isdigit():
            return False
    i += 1
    for i in range(0, 2):
        if not expiration[i].isdigit():
            return False
    return True

def takeInput():
    capital, winrate, risk, dte, max_price, min_price = 0, 0, 0, 0, 0, 0
    print('Welcome to the Options Screener for selling cash secured puts (CSP) and covered calls (CC)')
    if input('Modify the tickers.txt file for stocks you want to trade options on or enter 1 to find random plays') == '1':
        while True:
            try:
                min_price = input('What is the minimum price of a stock you are interested in trading? ')
                if min_price == 'exit':
                    exit()
                min_price = float(max_price)
            except ValueError:
                print('Please enter an integer or decimal or type "exit" to leave')
            else:
                break
        
        while True:
            try:
                max_price = input('What is the maximum price of a stock you are interested in trading? ')
                if max_price == 'exit':
                    exit()
                max_price = float(max_price)
            except ValueError:
                print('Please enter an integer or decimal or type "exit" to leave')
            else:
                break
                    

        while True:
            try:
                risk = input('What is your volatility risk tolerance? Enter 0 (low), 1 (medium), or 2 (high): ')
                if risk == 'exit':
                    exit()
                risk = int(risk)
            except ValueError:
                print('Please enter a valid integer or type "exit" to leave')
            else:
                break


    while True:
        try:
            capital = input('How much money do you have to trade with? ')
            if capital == 'exit':
                exit()
            capital = float(capital)
        except ValueError:
            print('Please enter an integer or decimal or type "exit" to leave')
        else:
            break

    while True:
        try:
            winrate = input('What is your desired winrate percentage as a decimal? ')
            if winrate == 'exit':
                exit()
            winrate = float(winrate)
        except ValueError:
            print('Please enter a decimal or type "exit" to leave')
        else:
            break

    
    while True:
        dte = input('What date of expiration are you looking for? (YYYY-MM-DD) ')
        if 'dte' == 'exit':
            exit()
        if not validateExpiration(dte):
            print('Please enter a string in the format YYYY-MM-DD or type "exit" to leave')
        else:
            break
    
    return capital, winrate, risk, dte

def main():
    capital, winrate, risk, dte = 100000, 0.2, 2, '2023-08-16'
    findPlays(capital, winrate, risk, dte)
    #capital, winrate, risk, dte = takeInput()



    



if __name__=="__main__":
    main()