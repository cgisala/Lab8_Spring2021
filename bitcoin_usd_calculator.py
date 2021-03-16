import requests

def main():
    bitcoin_price = get_bitcoin_price() # gets the current bitcoin price 
    bitcoin_amount = user_input() # get the amount of bitcoin the user wants convert to USD
    bitcoin_usd = bitcoin_usd_rate(bitcoin_price) # get bitcoin rate in USD
    usd = bitcoin_usd_calculator(bitcoin_usd, bitcoin_amount) # calculates the usd value based on the amount of bitcoin the user wants
    print_results(bitcoin_amount, usd)

def get_bitcoin_price():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    return requests.get(url).json() 

def bitcoin_usd_rate(data):
    return data['bpi']['USD']['rate_float']

def user_input():
    while True:
        try:
            bitcoin = float(input('\nHow many bitcoin do you want to convert to USD? '))
            if bitcoin <= 0:
                print('\n*** Error: enter a positive value ***')
            else:
                return bitcoin
        except:
            print('\n*** Error: enter a numerical value ***')

def bitcoin_usd_calculator(rate, amount):
    return round(rate * amount,2)

def print_results(amount, usd):
    print(f'\n{amount} bitcoin is equals to $ {usd}\n')

if __name__ == '__main__':
    main()