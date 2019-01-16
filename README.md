# peercoin_rpc

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI](https://img.shields.io/pypi/v/peercoin_rpc.svg?style=flat-square)](https://pypi.python.org/pypi/peercoin_rpc/)
[![](https://img.shields.io/badge/python-2.7+-blue.svg)](https://www.python.org/download/releases/2.7.0/) 


Peercoin_rpc is a simple and minimal library made for communication with `peercoind` via JSON-RPC protocol.
It has a single dependency - a Python `requests` library and it supports both mainnet and testnet peercoin network with authentication or SSL encryption.
There is a single class to be imported from the library - `Client`.

`Client` class methods are named the same as `ppcoind` RPC methods so learning curve is non-existant.

## Install

> pip install git+git://github.com/peercoin/peercoin_rpc.git

or

> pip install peercoin_rpc

## How to use

> from peercoin_rpc import Client

Spawn a new Client object with desired arguments:

> ppcnode = Client(testnet=True, username="username", password="password", ip=<ip>, port=<port>)

Use it:

> ppcnode.getinfo()

> ppcnode.getpeerinfo()

> ppcnode.getbalance()
