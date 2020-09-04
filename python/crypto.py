import urllib.parse
import http_req
import json
import vim
import config
import json

def ping():
    """
    Ping the price url, print whether the server is alive.
    """
    url  = _price_url() + "/ping" 
    resp = http_req.get(url)
    print("Response = ", resp)

def print_name(asset_ticker):
    """
    Convert a ticker to its name.
    """
    lower_case_ticker = asset_ticker.lower()
    print("Ticker : ", asset_ticker, " = ", config.ticker_converter[lower_case_ticker])

def print_price(asset):
    """
    Print the price of an asset.
    """
    query_id = _get_query_id(asset)
    currency = _vs_currency()
    resp     = _get_price_data(query_id, currency)
    price    = resp.get(query_id).get(currency)
    print("1 ", query_id, " = ", price, currency)

def _get_price_data(query_id, currency):
    params = {'ids': query_id, 'vs_currencies': currency}
    url = _price_url() + "/simple/price?" + urllib.parse.urlencode(params)
    resp = http_req.get(url)
    return json.loads(resp)

def _get_query_id(asset):
    """
    Learn whether to use the name given, or convert the ticker to its relevant name.
    """
    vc_user_input = vim.eval('g:vc_user_input')
    if (vc_user_input == config.TICKER):
        return config.ticker_converter[asset]
    elif (vc_user_input == config.NAME):
        return asset
    else:
        raise ValueError("Invalid user_input = ", vc_user_input, ", should be set to ", config.TICKER, " or", config.NAME, ".")

def _price_url():
    return vim.eval('g:price_url')

def _vs_currency():
    return vim.eval('g:vs_currency')

