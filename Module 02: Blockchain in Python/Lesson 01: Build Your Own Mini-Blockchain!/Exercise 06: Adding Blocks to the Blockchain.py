# =============
# blockchain.py
# =============
#imports the Block class from block.py
from block import Block

class Blockchain:
  def __init__(self):
    self.chain = []
    self.all_transactions = []
    self.genesis_block()

  def genesis_block(self):
    transactions = {}
    genesis_block = Block(transactions, "0")
    self.chain.append(genesis_block)
    return self.chain

  # prints contents of blockchain
  def print_blocks(self):
    for i in range(len(self.chain)):
      current_block = self.chain[i]
      print("Block {} {}".format(i, current_block))
      current_block.print_contents()    
  
  # add block to blockchain `chain`
  def add_block(self, transactions):
    # Task 1: complete add_block method
    previous_hash = self.chain[-1].hash
    # Create new block
    new_block = Block(transactions, previous_hash)
    # Append new_block to chain
    self.chain.append(new_block)

# ========
# block.py
# ========
import datetime
from hashlib import sha256

class Block:
  def __init__(self, transactions, previous_hash):
    self.timestamp = datetime.datetime.now()
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.hash = self.generate_hash()
    
  def print_block(self):
    # prints block contents
    print("timestamp:", self.timestamp)
    print("transactions:", self.transactions)
    print("current hash:", self.generate_hash())
    
  def generate_hash(self):
    block_contents = str(self.timestamp) + str(self.transactions) + str(self.previous_hash)
    block_hash = sha256(block_contents.encode())
    return block_hash.hexdigest()
