from __future__ import print_function #For getting the Python 2 printing!
import hashlib
import datetime as date
import json

class Block():
    def __init__(self, index, timestamp, data, previousHash = ''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.calculateHash()

    def calculateHash(self):
        hash = hashlib.sha256()
        hash.update(str(self.index) + str(self.timestamp) + str(self.data) + str(self.previousHash))
        return hash.hexdigest()


class Blockchain():
    def __init__(self):
        self.chain = []
        self.chain.append(self.createGenesisBlock())

    def createGenesisBlock(self):
        return Block(0, self.getStrDateTime(), "Genesis Block", "0")

    def getStrDateTime(self):
        return str(date.datetime.now())

    def getLatestBlock(self):
        return self.chain[-1]

    def addBlock(self, newBlock):
        newBlock.previousHash = self.getLatestBlock().hash
        newBlock.hash = newBlock.calculateHash()
        self.chain.append(newBlock)

    def isChainValid(self):
        currentIndex = 1

        while currentIndex < len(self.chain):
            block = self.chain[currentIndex]

            if(block.hash != block.calculateHash()):
                return False

            if(block.previousHash != self.chain[currentIndex-1].hash):
                return False

            currentIndex += 1

        return True


def MainMenu():
    print('-===== [ MY BLOCKCHAIN ]====-')
    geirCoin = Blockchain()
    geirCoin.addBlock(Block(1, geirCoin.getStrDateTime(), {"amount": 4}))
    geirCoin.addBlock(Block(2, geirCoin.getStrDateTime(), {"amount": 23}))

    jsonified = json.dumps([b.__dict__ for b in geirCoin.chain], indent=2, sort_keys=True)
    print(jsonified)
    
    # print("Is my blockchain valid?", geirCoin.isChainValid())

    # TAMPER WITH THE CHAIN
    # geirCoin.chain[1].data = {"amount": 10}
    # print("Is my blockchain valid?", geirCoin.isChainValid())

MainMenu()
