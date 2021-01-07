# SHA-256 algorithm is used to generate the hash of the block using:
# - Timestamp
# - Data
# - Previous Hash

from datetime import datetime
from hashlib import sha256

class Block:
  def __init__(self, transactions, previous_hash, nonce = 0):
    self.timestamp = datetime.now()
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.nonce = nonce
    # Task 4: Uncomment line
    self.hash = self.generate_hash()
    
  def print_block(self):
    # prints block contents
    print("timestamp:", self.timestamp)
    print("transactions:", self.transactions)
    print("current hash:", self.generate_hash())
    
  def generate_hash(self):
    # Task 1: create block_contents
    block_contents = str(self.timestamp) + str(self.transactions) + str(self.nonce) + str(self.previous_hash)
    # Task 2: create block_hash using block_contens, encode() and sha256()
    block_hash = sha256(block_contents.encode())
    # Return hash value using hexdigest()
    return block_hash.hexdigest()
