# vim-crypto

This project is a vim plugin which simply allows you to check cryptocurrency asset prices from within your vim editor, by consuming the coingecko API.

The aim is to eventually have a coingecko within Vim, that is a list of assets sorted by marketcap.


## Installation

You can install this plugin in the following ways:

TODO: Test other vim plugin managers.

### Install with [vim-plug][]

Use vim-plug by adding to your '.vimrc' in your plugins section:

'''viml
Plug 'talbotp/vim-crypto'
'''

Then dont forget to call ':PlugInstall()'.

## Configuration

There are a couple of global configuration options, these defaults are set in 'plugin/vim-crypto.vim'
These can be overwritten in your '.vimrc':

* 'g:vc_vs_currency'
This is the currency that the asset price will be fetched in, the default is USD.
If you wish to use eg GBP, then add this to your '.vimrc'.

'''viml
let g:vc_vs_currency = 'gbp'
'''

* 'g:vc_user_input'
When fetching a price, you can provide the ticker, or the name, and the default will use the ticker.
to use the name instead, add this to your '.vimrc'. A Python error is thrown, if this global value is not set to
'ticker' or 'name'.

'''viml
let g:vc_user_input = 'name'
'''

* 'g:vc_price_command'
This is the vim command to check the price of an asset, to change it, add this to your '.vimrc'.
The default command name is 'Vcp'.
'''viml
let g:vc_price_command = '<YOUR_COMMAND_NAME>'
'''

## Usage 

Currently, you can do the following:

* Fetch an asset price:

'''viml
:Vcp <ASSET_NAME> 
'''

This will return the asset's name 

* Fetch the name of an assets ticker.

'''viml 
:call VCName("<ASSET_NAME>")
'''

* Ping the price server

'''viml
:call VCPing()
'''

### When using ticker's instead of name.

'python/config.py' contains a map of ticker to name pairs, in the release it will contain the top 500 
marketcap coins. This list is populated from a python script 'scripts/create_config.py', which can be used to populate
the config with a larger list.


[vim-plug]: https://github.com/junegunn/vim-plug

