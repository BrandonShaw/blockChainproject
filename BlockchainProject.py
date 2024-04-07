#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Import Libraries
import hashlib
import datetime as date
import csv
import random
import time

#Create Class Block
class Block:
    
    #Init the class with values
    def __init__(self, index, timeStamp, data, payee, payor, amountSent, prevHash):
        
        #init the values with self
        self.index = index
        self.timeStamp = timeStamp
        self.data = data
        self.payee = payee
        self.payor = payor
        self.amountSent = amountSent
        self.prevHash = prevHash
        self.hash = self.calculateHash()
        
    #Calculate the hash using sha256 or sha512
    def calculateHash(self):
        
        #Calculate the hash
        hashString = str(self.index) + str(self.timeStamp) + str(self.data) + str(self.prevHash)
        
        #return calculated value
        return hashlib.sha512(hashString.encode()).hexdigest()
    
#Create Class Blockchain
class Blockchain:
    
    #Init the class
    def __init__(self):
        
        #Create  Gensis Block
        self.chain = [self.createGenBlock()]
        
    #Create Genesis Block
    def createGenBlock(self):
        
        #Return & Create the genesis block
        return Block(0, date.datetime.now(), "Genesis Block", 0, 0, 0, "000000")
    
    #Get Newest Block
    def getNewestBlock(self):
        
        #Grab the last block
        return self.chain[-1]
    
    #Add a new block
    def addBlock(self, newBlock):
        
        #Create & Append the new block
        newBlock.prevHash = self.getNewestBlock().hash
        newBlock.hash = newBlock.calculateHash()
        self.chain.append(newBlock)
        
    #Check if valid
    def isValid(self):
        
        #Check the whole chain
        for i in range(1, len(self.chain)):
            
            #def Vars
            currentBlock = self.chain[i]
            prevBlock = self.chain[i-1]
            
            #If hash is calculated wrong
            if currentBlock.hash != currentBlock.calculateHash():
                return False
            
            #If hashes do not match
            if currentBlock.prevHash != prevBlock.hash:
                return False
            
        #Good to go
        return True
    
#Users Class
class userWallet:
    
    #Init the class with values
    def __init__(self, walletID, ownerName, timeStamp, cashAmount):
        
        #init the values with self
        self.walletID = walletID
        self.ownerName = ownerName
        self.timeStamp = timeStamp
        self.cashAmount = cashAmount
    
#Mine Block
def generateSomeTransactions ():
    
    #Vars
    counter = 1
    amount = 10

    #Add some blocks to the chain
    while (counter <= amount):
    
        #time.sleep(random.randint(1,2))
    
        #Create Block
        blockchain.addBlock(Block(counter, date.datetime.now(), "Transaction " + str(counter), 1, 2, random.randint(1,1000), ""))

        #Add Counter
        counter += 1
        
def printTransactionBlockChain ():
    
    #Print out block chain
    for block in blockchain.chain:

        #Create output
        print("Transaction: " + str(block.index))
        print("Timestamp: " + str(block.timeStamp))
        print("Data: " + str(block.data))
        print("Payee: " + str(block.payee))
        print("Payor: " + str(block.payor))
        print("Amount Sent: " + str(block.amountSent))
        print("Hash: " + str(block.hash))
        print("Previous Hash: " + str(block.prevHash))
        print("-----------------------------------------------------------------------------")
        print("")
    
#Make the Blockchain
blockchain = Blockchain()

#Create some user Wallets
firstUser = userWallet(1, "Brandon Shaw", date.datetime.now(), 5212)
secondUser = userWallet(2, "Nick Mahoney", date.datetime.now(), 1823)
thirdUser = userWallet(3, "Bob Builder", date.datetime.now(), 9537)
 
#transscounter
transCounter = 11
    
#Create some random transactions on the blockchain
generateSomeTransactions()
    
#Print Hello Message to User w/ instructions
print("Welcome " + firstUser.ownerName + ", you currently have $" + str(firstUser.cashAmount))
print("-----------------------------------------------------------------------------") 
    
#Loop user in here
while (0 == 0):
    
    #List commands to user
    print("Please use one of the following commands:")
    print("'send': to send money to another user")
    print("'check': to see your current balance")
    print("'view': to see the transaction blockchain")
    print("")
    
    #Take users input
    userInput = input("Please Enter Command Here: ")
    print("")
    
    #Case tree for inputs
    match userInput:
        
        #send money
        case "send":
            print("#############################")
            print("     Send Money to User")
            print("#############################")
            print("")
            
            breakCheck = False
            
            #Loop if user makes mistakes
            while (0 == 0):
                
                #Show possible users to send money too
                print("Possible Users Are: ")
                print(str(secondUser.walletID) + "|" + secondUser.ownerName)
                print(str(thirdUser.walletID) + "|" + thirdUser.ownerName)
                print("")
                
                #Ask for user input
                userInputTwo = input("Please Enter Which User You Would Like To Send Money Too: ")
                print("")

                #check if user wanted to go back
                if (userInputTwo == "exit"):
                    break
                    
                #Check to make sure it is a valid user
                if ((userInputTwo == '2') or (userInputTwo == '3')):
                    
                    while (0 == 0):
                    
                        #Ask user how much
                        userInputThree = input("Please Enter How Much You Would Like To Send: ")
                        print("")

                        #check if user wanted to go back
                        if (userInputThree == "exit"):
                            
                            breakCheck = True
                            break
                        
                        #Check to see if user has enough
                        if (int(userInputThree) <= firstUser.cashAmount):

                            #Has enough money
                            print("#############################")
                            print("       Sending money...")
                            print("#############################")
                            print("")

                            #Take away the money from the user
                            firstUser.cashAmount = firstUser.cashAmount - int(userInputThree)
                            
                            #Second user
                            if (userInputTwo == '2'):
                                
                                #Add the money to the wanted user
                                secondUser.cashAmount =  secondUser.cashAmount + int(userInputThree)

                                #Tell User Money is Sent
                                print("$" + str(userInputThree) + " has been sent to " + secondUser.ownerName)
                                print("")
                                
                            #Third User
                            else:
                            
                                #Add the money to the wanted user
                                thirdUser.cashAmount =  thirdUser.cashAmount + int(userInputThree)

                                #Tell User Money is Sent
                                print("$" + str(userInputThree) + " has been sent to " + thirdUser.ownerName)
                                print("")
                            
                            #Add Transaction onto the BlockChain
                            blockchain.addBlock(Block(transCounter, date.datetime.now(), "Transaction " + str(transCounter), 1, userInputTwo, int(userInputThree), ""))
                            
                            #Add
                            transCounter += 1
                            
                            #Break afterwards
                            breakCheck = True
                            
                            break

                        #NOT ENOUGH
                        else:

                            #tell user not enough money
                            print("")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("You do not have enough money for this transaction... Please select a lower amount to continue")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("")
        
                #Not valid user
                else:
                
                    #tell user NOT valid user
                    print("")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("PLEASE SELECT A VALID USER")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("")
                    
                #Break if needed
                if (breakCheck == True):
                    
                    break
                
        #Check money
        case "check":
            print("#############################")
            print(" Checking current Balance...")
            print("#############################")
            print("")
            print("Hello, " + firstUser.ownerName + ", you currently have $" + str(firstUser.cashAmount))
            print("")
        
        #View Blockchain
        case "view":
            print("#############################")
            print("     Viewing Blockchain")
            print("#############################")
            print("")
            printTransactionBlockChain()
        
        #Default Case
        case default:
            
            print("#############################")
            print("PLEASE INPUT A VALID COMMAND!")
            print("#############################")
            print("")


# In[ ]:





# In[ ]:




