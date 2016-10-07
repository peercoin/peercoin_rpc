# peercoin_rpc

Peercoin_rpc is a simple and minimal library made for communication with `ppcoind` via JSON-RPC protocol.
It has a single dependency - a python `requests` library and it supports both mainnet and testnet peercoin network with authentication or SSL encryption.
There is a single class to be imported from the library - `Client`.
`Client` class methods are named the same as `ppcoind` RPC methods so learning curve is non-existant.

## Install

> pip install --user git+git://github.com/peerchemist/peercoin_rpc.git

## How to use

> from peercoin_rpc import Client

Spawn a new Client object with desired arguments:

> ppcnode = Client(testnet=True, username="username", password="password")

Use it:

> ppcnode.getinfo()
> ppcnode.getpeerinfo()

