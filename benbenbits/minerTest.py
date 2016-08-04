from BlockMine import *
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

genesis = Block()

private_key = rsa.generate_private_key(
     public_exponent=65537,
     key_size=2048,
     backend=default_backend()
 )

timeTotal = 0
blockTotal = 0
 
block = genesis

while 1:
  miner = BlockChallenge(block, private_key)
  
  while 1:
    if miner.tryOnce():
      break

  print(miner.winningHash.hexdigest())
  
  print("Mined in " + str(miner.mineTime) + " seconds. Nonce is " + str(miner.nonce))
  
  block = Block(miner.block, False)

  timeTotal += miner.mineTime
  blockTotal += 1
  
  print("Avg block time: " + str(timeTotal/blockTotal) + "\n")