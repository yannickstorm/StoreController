import time
import logging

logging.basicConfig(level=logging.INFO)

class StoreCmdSet:
    def __init__(self, id):
        self.id = id
        self.listCmd = []
        
        self.listCmd.append( bytes.fromhex("61E1ECCCAACCB334CD2D53334CAB32CAD54AD01ECCCAACCB334CD2D53334CAB32CAD54AD") )
        self.listCmd.append( bytes.fromhex("61E1ED534CB52CD4B3554B52D34B54B34AAB2E1ED534CB52CD4B3554B52D34B54B34AAB2") )
        self.listCmd.append( bytes.fromhex("C3C3D65696955A996696AA95A6AA95669569A03D65696955A996696AA95A6AA95669569A") )

    def print(self):
        print("Store: " + self.id)
 
class ClusterOfStores:

    def __init__(self, name):
        self.name = name
        self.listOfStores = []

        self.listOfStores.append( StoreCmdSet(0) ) 
        self.listOfStores.append( StoreCmdSet(1) ) 
        self.listOfStores.append( StoreCmdSet(2) ) 
        self.listOfStores.append( StoreCmdSet(3) ) 
        self.listOfStores.append( StoreCmdSet(4) ) 

class DummyController:

    def __init__(self):

        self.clusterOfStores = ClusterOfStores("System open space")
        print("Initializing dummy Store controller")

    def transmitCommand(self, id, cmd):
            print("Sending dummy command from dummy controller: " + str(self.clusterOfStores.listOfStores[id].listCmd[cmd]))

