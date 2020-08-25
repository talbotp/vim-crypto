" Cancel setup if python3 is not available.
if !has("python3")
    echo "vim has to be compiled with python3 for vim-crypto to run, vim-crypto is disabled."
    finish
endif

" Cancel setup if its already been ran.
if exists('g:vim_crypto_plugin_loaded')
    finish
endif
let g:vim_crypto_plugin_loaded = 1


" Setup variables which can be changed in vimrc

" The url used to get price data.
if exists('g:default_price_url')
    let g:price_url = g:default_price_url
else
    let g:price_url = 'https://api.coingecko.com/api/v3'
endif 

" The default currency to be used
if exists('g:default_vs_currency')
    let g:vs_currency = g:default_vs_currency
else 
    let g:vs_currency = 'usd'
endif

" Notify vim's python interpreter where our python code lives.
let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

python3 << EOF

import sys
import vim
from os.path import normpath, join

plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python'))
sys.path.insert(0, python_root_dir)

import crypto

EOF

function! VCPing()
   python3 crypto.ping()
endfunction

function! VCName(asset_ticker)
    execute "python3 crypto.ticker_to_name(\"" . a:asset_ticker . "\")"
endfunction

function! VCPrice(asset_ticker)
    execute "python3 crypto.price(\"" . a:asset_ticker . "\")"
endfunction

