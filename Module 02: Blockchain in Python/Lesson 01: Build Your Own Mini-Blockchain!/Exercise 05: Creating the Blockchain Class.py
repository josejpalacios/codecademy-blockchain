# =============
# blockchain.py
# =============
#imports the Block class from block.py
from block import Block

class Blockchain:
    def __init__(self):
      # Task 1: Initalize instance variables chain and all_transactions
      self.chain = []
      self.all_transactions = []
      # Task 3: call genesis_block method
      self.genesis_block()
    
    def genesis_block(self):
      # Task 2: complete method
      self.chain.append(Block([], 0))

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
