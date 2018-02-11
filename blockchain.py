# -*- coding: utf-8 -*-

from time import time
from urllib.request import urlparse
import json, hashlib


class BlockChain:
    def __init__(self):
        self.chain = []
        self.nodes = set()
        self.current_transactions = []
        self.new_block(previous_hash=1, proof=100)

    def valid_chain(self, chain):
        last_chain = chain[0]
        current_index = 0

        while current_index < len(chain):
            block = chain(current_index)

            if block['previous_hash'] != self.hash(last_chain):
                return False

            if not self.valid_proof(last_block['proof'], block['proof'], last_block['previous_hash']):
                return False

            last_block = block
            current_index += 1
        return True

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, receiver, amount):
        self.current_transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })

        return self.last_block['index'] + 1

    def proof_of_work(self, last_block):

        proof = 0
        last_proof = last_block['proof']
        last_hash = self.hash(last_block)

        while self.valid_proof(last_proof, proof, last_hash) is False:
            proof += 1

        return proof

    def register_node(self, address):
        parsed_url = urlparse(address)

        if parsed_url.netloc:
            self.nodes.add(parsed_url.netloc)
        elif parsed_url.path:
            self.nodes.add(parsed_url.path)
        else:
            raise ValueError('Invalid URL')

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @staticmethod
    def valid_proof(last_proof, proof, last_hash):
        guess = f'{last_proof}{proof}{last_hash}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()

        return guess_hash[:4] == '0000'

    @property
    def last_block(self):
        pass


if __name__ == '__main__':
    blockchain = BlockChain()
    # blockchain.new_block()
