#!/usr/bin/env python
# -*- coding: utf-8 -*-

__copyright__ = "Copyright 2017, The Peerchemist"
__license__ = "MIT"
__email__ = "peerchemist@protonmail.ch"

# Bitcoin API calls 
# https://en.bitcoin.it/wiki/Original_Bitcoin_client/API_calls_list#Full_list

import requests
import json
import os


class Client:
    '''JSON-RPC Client.'''

    def __init__(self, testnet=False, username=None, password=None,
                 ip=None, port=None, directory=None):

        if not ip:
            self.ip = 'localhost'  # default to localhost
        else:
            self.ip = ip

        if not username and not password:
            if not directory:
                try:
                    self.username, self.password = self.userpass()  # try to read from ~/.ppcoin
                except:
                    self.username, self.password = self.userpass(dir='peercoin')  # try to read from ~/.peercoin
            else:
                self.username, self.password = self.userpass(dir=directory)  # try some other directory

        else:
            self.username = username
            self.password = password
        if testnet is True:
            self.testnet = True
            self.port = 9904
            self.url = 'http://{0}:{1}'.format(self.ip, self.port)
        else:
            self.testnet = False
            self.port = 9902
            self.url = 'http://{0}:{1}'.format(self.ip, self.port)
        if port is not None:
            self.port = port
            self.url = 'http://{0}:{1}'.format(self.ip, self.port)

        self.session = requests.Session()
        self.session.auth = (self.username, self.password)
        self.session.headers.update({'content-type': 'application/json'})

    def userpass(self, dir='ppcoin'):
        '''Reads config file for username/password'''

        source = os.path.expanduser('~/.{0}/{0}.conf').format(dir)
        dest = open(source, 'r')
        with dest as conf:
            for line in conf:
                if line.startswith('rpcuser'):
                    username = line.split("=")[1].strip()
                if line.startswith("rpcpassword"):
                    password = line.split("=")[1].strip()

        return username, password

    def req(self, method, params=()):
        """send request to ppcoind"""

        response = self.session.post(self.url,
                   data=json.dumps({"method": method,
                                    "params": params,
                                    "jsonrpc": "1.1"})
                ).json()

        if response["error"] is not None:
            return response["error"]
        else:
            return response["result"]

    def batch(self, reqs: list ):
        """ send batch request using jsonrpc 2.0 """

        batch_data = []

        for req_id, req in enumerate(reqs):
            batch_data.append( {"method": req[0], "params": req[1], "jsonrpc": "2.0", "id": req_id} )

        data = json.dumps(batch_data)
        response = self.session.post(self.url, data=data).json()
        return response

    ## RPC methods
    ### general syntax is req($method, [array_of_parameters])

    def getinfo(self):
        """return getinfo from ppcoind"""
        return self.req("getinfo")

    def walletpassphrase(self, passphrase, timeout=99999999, mint_only=True):
        '''used to unlock wallet for minting'''
        return self.req("walletpassphrase", [passphrase, timeout, mint_only])

    def getblock(self, blockhash):
        '''returns detail block info.'''
        return self.req("getblock", [blockhash])

    def getblockcount(self):
        '''Retrieve last block index'''
        return self.req("getblockcount")

    def getblockhash(self, index):
        '''retrieve block hash'''
        return self.req("getblockhash", [index])

    def gettransaction(self, txid):
        '''get transaction info'''
        return self.req("gettransaction", [txid])

    def getbalance(self, account=None, minconf=6):
        '''retrieve balance, If [account] is specified, returns the balance in the account.'''
        if account:
            return self.req("getbalance", [account, minconf])
        else:
            return self.req("getbalance")

    def getreceivedbyaddress(self, address, minconf=1):
        '''Returns the amount received by <address> in transactions
        with at least [minconf] confirmations.'''
        return self.req("getreceivedbyaddress", [address, minconf])

    def getdifficulty(self):
        '''Get PoS/PoW difficulty'''
        return self.req("getdifficulty")

    def getpeerinfo(self):
        '''Get connected peer's info'''
        return self.req("getpeerinfo")

    def getaddressesbyaccount(self, account=""):
        '''can be used to list asociated addresses'''
        return self.req("getaddressesbyaccount", [account])

    def getnewaddress(self, label=""):
        '''return new address'''
        return self.req("getnewaddress", [label])

    def getaccount(self, address):
        '''get account associated with <address>'''
        return self.req("getaccount", [address])

    def getaccountaddress(self, account):
        '''get address associated with the <account>'''
        return self.req("getaccountaddress", [account])

    def sendtoaddress(self, recv_addr, amount, comment=""):
        '''send ammount to address, with optional comment. Returns txid.
        sendtoaddress(ADDRESS, AMMOUNT, COMMENT)'''
        return self.req("sendtoaddress", [recv_addr, amount, comment])

    def sendfrom(self, account, address, amount):
        '''send outgoing tx from specified account to a given address'''
        return self.req("sendfrom", [account, address, amount])

    def sendmany(self, recv_dict, account="", comment=""):
        '''send outgoing tx to many addresses, input is dict of addr:coins, returns txid'''
        #{"addr1":#coin,"addr2":#coin,"addr3":#coin...}
        return self.req("sendmany", [account, recv_dict, comment])

    def getconnectioncount(self):
        '''Get number of active connections'''
        return self.req("get_conn_count")

    def getrawtransaction(self, txid, verbose=0):
        '''get raw transaction
        If verbose=0, returns serialized, hex-encoded data for transaction txid.
        If verbose is non-zero, returns a JSON Object containing information about the transaction.
        Returns an error if <txid> is unknown.'''
        return self.req("getrawtransaction", [txid, verbose])

    def getrawmempool(self):
        '''returns raw mempool'''
        return self.req("getrawmempool")

    def listtransactions(self, account="", many=999, since=0):
        '''list all transactions associated with this wallet'''
        return self.req("listtransactions", [account, many, since])

    def listreceivedbyaddress(self, minconf=0, includeempty=True):
        '''get list of all accounts in the wallet'''
        return self.req("listreceivedbyaddress", [minconf, includeempty])

    def listreceivedbyaccount(self, minconf=0, includeempty=True):
        '''list received by account'''
        return self.req("listreceivedbyaccount", [minconf, includeempty])

    def listaccounts(self, minconf=1):
        '''list accounts in the wallet'''
        return self.req("listaccounts", [minconf])

    def listunspent(self, minconf=1, maxconf=999999):
        '''list only unspent UTXO's'''
        return self.req("listunspent", [minconf, maxconf])

    def dumpprivkey(self, addr):
        '''returns privkey of address in WIF format.'''
        return self.req("dumpprivkey", [addr])

    def importprivkey(self, wif, account_name=""):
        '''Import privatekey in WIF format'''
        return self.req("importprivkey", [wif, account_name])

    def createrawtransaction(self, inputs, outputs):
        '''[{"txid":input_txid,"vout":0}, ...], {recv_addr: amount, change: amount, ...}'''
        if not isinstance(outputs, dict):
            raise TypeError('outputs variable must be a dictionary')
        if not isinstance(inputs, list):
            raise TypeError('inputs variable must be a list')
        return self.req("createrawtransaction", [inputs, outputs])

    def decoderawtransaction(self, txhash):
        '''dump the transaction draft'''
        return self.req("decoderawtransaction", [txhash])

    def signrawtransaction(self, rawtxhash):
        '''signrawtransaction with privkey, returns status and rawtxhash'''
        return self.req("signrawtransaction", [rawtxhash])

    def sendrawtransaction(self, signed_rawtxhash):
        '''sends raw transaction, returns txid'''
        return self.req("sendrawtransaction", [signed_rawtxhash])

    def validateaddress(self, address):
        '''Return information about address.'''
        return self.req("validateaddress", [address])

    def signmessage(self, address, message):
        '''Sign a message with the private key of an address.'''
        return self.req("signmessage", [address, str(message)])

    def verifymessage(self, address, signature, message):
        """Verify a signed message."""
        return self.req("verifymessage", [address, signature, message])

    def encryptwallet(self, passphrase):
        '''Encrypt wallet.'''
        return self.req("encryptwallet",[passphrase])

    def enforcecheckpoint(self, true=1):
        '''true or false to enable or disable enforcement of
           broadcasted checkpoints by developer.'''

        return self.req('enforcecheckpoint', true)

    def keypoolrefill(self, size=100):
        '''fils the keypoool'''

        return self.req('keypoolrefill', [size])
