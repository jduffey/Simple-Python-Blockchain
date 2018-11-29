import datetime
import hashlib

BLOCKS_TO_GENERATE = 10

class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    startTime = 0
    timestamp = 0

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        hashTime = self.timestamp - self.startTime
        return ( "Block Hash: " + str(self.hash()) +
                 "\nBlockNo: " + str(self.blockNo) +
                 "\nBlock Data: " + str(self.data) +
                 "\nHashes (nonce): " + str(self.nonce) +
                 "\nTimestamp: " + str(self.timestamp) +
                 "\nHashTime: " + str(hashTime) +
                 "\n--------------")

class Blockchain:

    diff = 20
    maxNonce = 2**32
    target = 2 ** (256-diff)

    block = Block("This string doesn't matter")
    head = block

    def add(self, block, startTime):

        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1
        block.timestamp = datetime.datetime.now()
        block.startTime = startTime

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        startTime = datetime.datetime.now()
        print("Start:", startTime)
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block, startTime)
                print(block)
                break
            else:
                block.nonce += 1

blockchain = Blockchain()

for n in range(BLOCKS_TO_GENERATE):
    blockchain.mine(Block("Block " + str(n+1)))

while blockchain.head != None:
    blockchain.head = blockchain.head.next
