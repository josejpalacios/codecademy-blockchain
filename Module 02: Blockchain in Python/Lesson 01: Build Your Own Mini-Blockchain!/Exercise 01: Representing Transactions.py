transaction1 = {
  'amount': '30',
  'sender': 'Alice',
  'receiver': 'Bob'}
transaction2 = { 
  'amount': '200',
  'sender': 'Bob',
  'receiver': 'Alice'}
transaction3 = { 
  'amount': '300',
  'sender': 'Alice',
  'receiver': 'Timothy' }
transaction4 = { 
  'amount': '300',
  'sender': 'Rodrigo',
  'receiver': 'Thomas' }
transaction5 = { 
  'amount': '200',
  'sender': 'Timothy',
  'receiver': 'Thomas' }
transaction6 = { 
  'amount': '400',
  'sender': 'Tiffany',
  'receiver': 'Xavier' }

mempool = [transaction1, transaction2, transaction3, transaction4, transaction5, transaction6]

# add your code below

# Task 1: Create my_transaction
my_transaction = {
  'amount': '100',
  'sender': 'Jose',
  'receiver': 'Charlie'
}

# Task 2: Add my_transaction to mempool
mempool.append(my_transaction)

# Task 3: Create block_transactions list and add three transactions from mempool
block_transactions = [mempool[index] for index in range(0, 3)]
