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
# 7b5ed8155d70293bb42ff9df339d62e63170c581cb7a26fb09a7306eaf1b676a
  
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
# 006d7590979a7a2177c9a9e5fcbe4314c567bcd84a5e5667931d593ec4f8ba98
