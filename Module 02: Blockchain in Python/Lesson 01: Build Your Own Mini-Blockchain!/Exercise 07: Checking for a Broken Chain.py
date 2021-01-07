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
    previous_block_hash = self.chain[len(self.chain)-1].hash
    new_block = Block(transactions, previous_block_hash)
    self.chain.append(new_block)

  def validate_chain(self):
    # Task 1: complete validate_chain method
    # Iterate through entire blockchain after the genesis block
    for i in range(1, len(self.chain)):
      # Create current variable
      current = self.chain[i]
      # Create previous variable
      previous = self.chain[i-1]
      # Task 2: Verify hash of current block does not equal hash generated for current block
      if (current.hash != current.generate_hash()):
        # Blockchain is not valid, return False
        return False
      # Task 3: Verify previous hash for current block does not equal hash generated for previous block
      elif (current.previous_hash != previous.generate_hash()):
        # Blockchain is not valid, return False
        return False
    # For loop completed and blockchain is validated, return true
    return True
    
# ========
# block.py
# ========
import datetime
from hashlib import sha256

#changed data to transactions

class Block:
    def __init__(self, transactions, previous_hash):
        self.time_stamp = datetime.datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.generate_hash()

    def generate_hash(self):
        block_header = str(self.time_stamp) + str(self.transactions) +str(self.previous_hash) + str(self.nonce)
        block_hash = sha256(block_header.encode())
        return block_hash.hexdigest()

    def print_contents(self):
        print("timestamp:", self.time_stamp)
        print("transactions:", self.transactions)
        print("current hash:", self.generate_hash())
        print("previous hash:", self.previous_hash) 
