# To  use SHA-256 in Python 3, string must be encoded before being passed as an argument.
# To encode the string, use the .encode() method.

# Task 1: import sha256
from hashlib import sha256

# Task 2: create text variable
text = "I am excited to learn about blockchain!"

# Task 3: using encode on text, convert text to hash 
hash_result = sha256(text.encode())

# Task 4: Use hexdigest and print result
print(hash_result.hexdigest())

# Task 5: Add exclamation mark to see how code changes

# Without !
# 6866cb54011a5562052b7dbce8d7afa26195cbb7a73c3e70a56dc1a25d6df831

# With !
# 32ad45b332a7e5869d6d5aac178a1af413b04b206047709ea021df8d4d21ff56
