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
