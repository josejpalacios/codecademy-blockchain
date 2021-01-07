new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

# Task 1: import sha256
from hashlib import sha256

# Task 2: Create difficulty variable. Sets the amount of leading zeros that must be found in the hash produced by the nonce. Create nonce variable
difficulty = 2
nonce = 0

# Task 3: creating the proof
info = str(nonce) + str(new_transactions)
# Create hash value
proof = sha256((info).encode()).hexdigest()
# printing proof
print(proof)
  
# Task 4: finding a proof that has 2 leading zeros
while(proof[:2] != '0' * difficulty):
  # Increment nonce by 1
  nonce += 1
  # Convert nonce and new_transactions into strings
  info = str(nonce) + str(new_transactions)
  # Create hash value
  proof = sha256((info).encode()).hexdigest()
# Store proof into final_proof  
final_proof = proof

# printing final proof that was found
print(final_proof)
