#encoding=utf-8

import hashlib
import json
from time import time
from textwrap import dedent
from uuid import uuid4

from flask import Flask



class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        self.new_block(previous_hash=1,proof=100)

    def new_block(self):
        #添加新的区块和添加它到链中
        block={
            'index':len(self.chain)+1,
            'timestamp':time(),
            'transactions':self.current_transactions,
            'proof':proof,
            'previous_hash':previous_hash or self.hash(self.chain[-1]),
        }

        self.current_transactions = []

        self.chain.append(block)

        return block

    def new_transation(self,sender,recipient,amount):
        #添加新的交易
        self.current_transactions.append({
            'sender':sender,
            'recipient':recipient,
            'amount':amount,
        })

        return self.last_block['index']+1

    @staticmethod
    def hash(block):
        #哈希区块的信息
        block_string = json.dump(block,sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        #从链中拿到上个区块
        return self.chain[-1]

    def proof_of_work(self,last_proof):

        proof = 0
        while self.valid_proof(last_proof,proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof,proof):

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()

        return guess_hash[:4]=="0000"


app = Flask(__name__)

node_identifier = str(uuid4()).replace('-'.'')

blockchain = Blockchain()

@app.route('/mine',methods=['GET'])
def mine():
    return "we'll mine a new block"

@app.route('/transactions/new',methods=['POST'])
def new_transaction():
    return "we'll add a new transaction"

@app.route('/chain',methods=['GET'])
def full_chain():
    response = {
        'chain':blockchain.chain,
        'length':len(blockchain.chain),
    }
    return jsonify(response),200

if __name__ == '__main__':
    app.run(host='0.0.0.0',post=5000)
