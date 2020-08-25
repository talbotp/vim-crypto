import urllib.parse
import http_req
import json
import vim
import config

def ping():
    """Ping the price url, print whether the server is alive."""
    url = _price_url() + "/ping" 
    resp = http_req.get(url)
    print("Response = ", resp)

def ticker_to_name(asset_ticker):
    """Convert a ticker to its name."""
    lower_case_ticker = asset_ticker.lower()
    print("Ticker : ", asset_ticker, " = ", config.ticker_converter[lower_case_ticker])

def price(asset_ticker):
    """Print the price of an asset."""
    params = {'ids': asset_ticker, 'vs_currencies': _vs_currency()}
    url = _price_url() + "/simple/price?" + urllib.parse.urlencode(params)
    resp = http_req.get(url)
    print("Response = ", resp)

def _get_price(asset_name):
    params = {'ids': asset_name, 'vs_currencies': _vs_currency()}
    url = _price_url() + "/simple/price?" + urllib.parse.urlencode(params)
    resp = http_req.get(url)
    return resp 

def _price_url():
    return vim.eval('g:price_url')

def _vs_currency():
    return vim.eval('g:vs_currency')
