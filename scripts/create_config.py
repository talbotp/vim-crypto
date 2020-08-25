# Python3 module for loading out config file.
# Which is used to convert tickers to names of the top 100 marketcap coins.
import sys
sys.path.insert(1, './python')      # Help to import http_req
import http_req
import json

current_page = 1                    # Paginate starting from the top.
max_number_of_markets = 500         # Add the top N markets to our config file.

def get_json(page):
    """Fetch the market json data from the given page from our converter api"""
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=' + str(page) + '&sparkline=false'
    response = http_req.get(url)
    return json.loads(response)

# Open and truncate our file, then start the dict.
config_file = open('./python/config.py', 'w')
config_file.write('ticker_converter = {\n')

response_json = get_json(current_page)
market_iter   = iter(response_json)

while max_number_of_markets != 0:
    try:
        current_market = next(market_iter)
    except StopIteration:
        # Iterate onto the next page.
        current_page   += 1
        response_json  = get_json(current_page)
        market_iter    = iter(response_json)
        current_market = next(market_iter)
        
    current_symbol = current_market['symbol']
    current_id     = current_market['id']
        
    if max_number_of_markets == 1:
        entry = '\t"' + current_symbol + '" : "' + current_id + '"\n}\n'   # Remove last comma and close dict.
    else: 
        entry = '\t"' + current_symbol + '" : "' + current_id + '",\n'
    
    config_file.write(entry)
    print(entry)
    max_number_of_markets -= 1

# Close our updated config file.
config_file.close()

print('Finished writing the config file.')

