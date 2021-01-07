# Final version of script.py used and created for Exercise 12
from blockchain import Blockchain

block_one_transactions = {"sender":"Alice", "receiver": "Bob", "amount":"50"}
block_two_transactions = {"sender": "Bob", "receiver":"Cole", "amount":"25"}
block_three_transactions = {"sender":"Alice", "receiver":"Cole", "amount":"35"}
fake_transactions = {"sender": "Bob", "receiver":"Cole, Alice", "amount":"25"}

# Task 1: Create Blockchain object
local_blockchain = Blockchain()
# Print contents of local_blockchain
local_blockchain.print_blocks()

# Task 2: Add blocks 1 to 3 individually
local_blockchain.add_block(block_one_transactions)
# Add block 2
local_blockchain.add_block(block_two_transactions)
# Add block 3
local_blockchain.add_block(block_three_transactions)
# Print contents of local_blockchain
local_blockchain.print_blocks()

# Task 3: Change second block's transactions to fake_transactions.
local_blockchain.chain[2].transactions = fake_transactions
# Check if blockchain is still valid
local_blockchain.validate_chain()
