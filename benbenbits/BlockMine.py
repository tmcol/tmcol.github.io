import block_pb2
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import hashlib
import time

diffFloor = 14

targetTime = 3

def getTarget(diff):
    internalDiff =  (int((2**64)/diff) - 1)
    target = internalDiff * (2**(256 - 64 - diffFloor))
    
    print("Diff is: " + str(diff) + "\nTarget:\n" + '{:064x}'.format(target))
    
    return target

class Block:
  def __init__(self, protoBlock = None, serialized = True):
    if protoBlock is not None:
      self.fromProto(protoBlock, serialized)
      return  
    
    self.nextDiff = 4 
    self.thisDiff = 4
    self.time = int(time.time())
    self.num = 1
    self.hash = b'\x00'
    
  
  def fromProto(self, protoBlock, serialized = True):
    if serialized:
      block = block_pb2.Block()
      block.ParseFromString(protoBlock)
    else:
      block = protoBlock

    self.pubkey = block.pubkey
    self.signature = block.signature
    self.hash = block.hash
    self.nonce = block.nonce
    
    self.blockContents = block.cnts
    
    self.thisDiff = self.blockContents.thisDiff
    self.nextDiff = self.blockContents.nextDiff
    self.time = self.blockContents.time
    self.num = self.blockContents.num
    
  def verify(self):
    try:
      self.pubkey.verify(
       self.signature,
       self.blockContents,
       padding.PSS(
           mgf=padding.MGF1(hashes.SHA256()),
           salt_length=padding.PSS.MAX_LENGTH
       ),
       hashes.SHA256()
      )
      return True
    except InvalidSignature:
      return false

class BlockChallenge:
  def __init__(self, prevBlock, key, txns = []):
    self.txns = txns
    self.thisDiff = prevBlock.nextDiff
    self.prevHash = prevBlock.hash
    self.time = int(time.time())
    self.num = prevBlock.num + 1
    
    
    timeDiff = self.time - prevBlock.time
    print("Time diff is " + str(timeDiff))
    if timeDiff == 0:
      self.nextDiff = prevBlock.thisDiff*2
    else:
      self.nextDiff = max(1, int(prevBlock.thisDiff * targetTime/timeDiff))
    
    self.blockContents = block_pb2.BlockContents()
    self.blockContents.nextDiff = self.nextDiff
    self.blockContents.thisDiff = self.thisDiff
    self.blockContents.time = self.time
    self.blockContents.prevHash = self.prevHash
    self.blockContents.num = self.num
    
    for tx in self.txns:
      t = blockContents.txns.add()
      t.sender = tx.sender
      t.recver = tx.recver
      t.amount = tx.amount
      t.signature = tx.signature
      
    self.blockBytes = self.blockContents.SerializeToString()
    
    signer = key.signer(
     padding.PSS(
         mgf=padding.MGF1(hashes.SHA256()),
         salt_length=padding.PSS.MAX_LENGTH
     ),
     hashes.SHA256()
    )
    signer.update(self.blockBytes)
    self.signature = signer.finalize()
    
    self.hashable = self.signature + self.blockBytes
    
    self.nonce = 0
    
    self.target = getTarget(self.thisDiff)
    
    
    self.timeStart = time.time()
 
  def tryOnce(self):
    nonceBytes = self.nonce.to_bytes(8, byteorder='big')
    hash = hashlib.sha256(self.hashable + nonceBytes)
    hashVal = int.from_bytes(hash.digest(), 'big')
    
    if hashVal < self.target:
      self.finishBlock(hash)
      return True
      
    else:
      self.nonce+=1
      return False
    
    
  def finishBlock(self, hash):
    self.winningHash = hash
    
    self.block = block_pb2.Block()
    self.block.cnts.MergeFrom(self.blockContents);
    self.block.signature = self.signature;
    self.block.hash = hash.digest();
    self.block.nonce = self.nonce;
    
    self.mineTime = time.time() - self.timeStart