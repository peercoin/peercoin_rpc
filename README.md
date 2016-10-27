# peercoin_rpc

[![tip for next commit](https://peer4commit.com/projects/193.svg)](https://peer4commit.com/projects/193)
[![PyPI](https://img.shields.io/pypi/pyversions/Django.svg?maxAge=2592000)](https://pypi.python.org/pypi/peercoin_rpc/0.3)

Peercoin_rpc is a simple and minimal library made for communication with `ppcoind` via JSON-RPC protocol.
It has a single dependency - a Python `requests` library and it supports both mainnet and testnet peercoin network with authentication or SSL encryption.
There is a single class to be imported from the library - `Client`.

`Client` class methods are named the same as `ppcoind` RPC methods so learning curve is non-existant.

## Install

> pip install git+git://github.com/peerchemist/peercoin_rpc.git

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

