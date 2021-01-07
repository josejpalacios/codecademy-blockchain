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
    for i in range(1, len(self.chain)):
      current = self.chain[i]
      previous = self.chain[i-1]
      if(current.hash != current.generate_hash()):
        print("The current hash of the block does not equal the generated hash of the block.")
        return False
      if(current.previous_hash != previous.generate_hash()):
        print("The previous block's hash does not equal the previous hash value stored in the current block.")
        return False
    return True
  
  def proof_of_work(self,block, difficulty=2):
    # Task 1: Create local variable proof with block's generated hash value
    proof = block.generate_hash()
    # Task 2: Loop until correct hash value is generated
    while(proof[:2] != '0' * difficulty):
      # Increment nonce by 1
      block.nonce += 1
      # Generate new hash value
      proof = block.generate_hash()
    # Once correct hash has been found, set nonce back to 0
    self.nonce = 0
    # Return hash value
    return proof


# ========
# block.py
# ========
import datetime
from hashlib import sha256

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
