#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016 Peerchemist
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

import getpass
import requests, json

class Client:
    
    def __init__(self, testnet=False, username=None, password=None, ip="127.0.0.1", port=None):

        self.ip = ip
        if not username and not password:
            self.username, self.password = self.userpass() ## try to read from ~/.ppcoin
        else:
            self.username = username
            self.password = password
        if testnet == True:
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

        self.headers = {'content-type': 'application/json'}

    def userpass(self):
        '''Reads .ppcoin/ppcoin.conf file for username/password'''
        with open('/home/{0}/.ppcoin/ppcoin.conf'.format(getpass.getuser()), 'r') as conf:
            for line in conf:
                if line.startswith('rpcuser'):
                    username = line.split("=")[1].strip()
                if line.startswith("rpcpassword"):
                    password = line.split("=")[1].strip()
        
            return username, password
    
    def req(self, method, params=()):
        """send request to ppcoind"""

        response = requests.post(self.url, 
            auth=(self.username, self.password), headers=self.headers, 
            data=json.dumps({"method": method,
                    "params": params,
                    "jsonrpc": "1.1"})
                ).json()
        
        assert response["error"] == None
        return response["result"]
        
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
        return self.req("getnewaddress", [label])

    def sendtoaddress(self, recv_addr, amount, comment=""):
        '''send ammount to address, with optional comment. Returns txid.
        sendtoaddress(ADDRESS, AMMOUNT, COMMENT)'''
        return self.req("sendtoaddress", [recv_addr, amount, comment])

    def sendmany(self, recv_dict, account="", comment=""):
        '''send outgoing tx to many addresses, input is dict of addr:coins, returns txid'''
        #{"addr1":#coin,"addr2":#coin,"addr3":#coin...}
        return self.req("sendmany", [account, recv_dict, comment])

    def getconnectioncount(self):
        '''Get number of active connections'''
        return self.req("get_conn_count")

    def getrawtransaction(self, txid, verbose=1):
        '''get raw transaction'''
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

    def listunspent(self, minconf=1, maxconf=999999): #listunspent 0 999999 '["1BxtgEa8UcrMzVZaW32zVyJh4Sg4KGFzxA"]'
        '''list only unspent UTXO's'''
        return self.req("listunspent", [minconf, maxconf])

    def dumpprivkey(self, addr):
        '''returns privkey of address'''
        return self.req("dumpprivkey", [addr])

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
        return self.req("sendrawtransaction", [signed_rawtxhash, 1])

    def validateaddress(self, address):
        '''Return information about address.'''
        return self.req("validateaddress", [address])

    def signmessage(self, address, message):
        '''Sign a message with the private key of an address.'''
        return self.req("signmessage", [address, str(message)])
    
    def verifymessage(self, signature, message):
        """Verify a signed message."""
        return self.req("verifymessage", [signature, message])

