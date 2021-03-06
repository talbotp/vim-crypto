"" Cancel setup if python3 is not available.
if !has("python3")
    echo "vim has to be compiled with python3 for vim-crypto to run, vim-crypto is disabled."
    finish
endif

"" Cancel setup if its already been ran.
if exists('g:vim_crypto_plugin_loaded')
    finish
endif
let g:vim_crypto_plugin_loaded = 1


"" Setup variables which can be changed in vimrc

"" The url used to get price data.
if !exists('g:vc_price_url')
    let g:vc_price_url = 'https://api.coingecko.com/api/v3'
endif 

"" The currency to be used for price checks etc.
if !exists('g:vc_vs_currency') 
    let g:vc_vs_currency = 'usd'
endif

"" The default input to be used when fetching prices, ie ticker vs asset name.
" Options are 'ticker' or 'name
if !exists('g:vc_user_input')
    let g:vc_user_input = 'ticker'
endif

"" Command for fetching the price of a single asset.
if !exists('g:vc_price_command')
    command! -nargs=* Vcp :call VCPrice(<q-args>)
else 
    execute "command! -nargs=* ". g:vc_price_command. " :call VCPrice(<q-args>)"
endif

"" Notify vim's python interpreter where our python code lives.
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
    execute "python3 crypto.print_name(\"" . a:asset_ticker . "\")"
endfunction

function! VCPrice(asset)
    execute "python3 crypto.print_price(\"" . a:asset . "\")"
endfunction

