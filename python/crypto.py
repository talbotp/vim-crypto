import urllib.parse
import http_req
import json
import vim

def ping():
    """Ping the price url, print whether the server is alive."""
    url = _price_url() + "/ping" 
    resp = http_req.get(url)
    print("Response = ", resp)

def price(asset_name):
    """Simply print the current value of a token."""
    params = {'ids': asset_name, 'vs_currencies': _vs_currency()}
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
