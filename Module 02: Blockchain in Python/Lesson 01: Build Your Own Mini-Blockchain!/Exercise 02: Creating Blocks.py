# Recall that a Block contains the following properties:
# - Timestamp
# - Transaction
# - Hash
# - Previous Hash
# - Nonce

# Task 1: import datetime library
from datetime import datetime

# Task 2: print current date and time
print(datetime.now())

class Block:
# Task 3: complete constructor for block class
  def __init__(self, transactions, previous_hash):
    # Initialize instance variables
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.nonce = 0
    # Task 4: Create timestamp instance variable
    self.timestamp = datetime.now()
