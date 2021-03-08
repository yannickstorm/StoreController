import time
import cc1101
import logging

logging.basicConfig(level=logging.INFO)

class StoreCmdSet:
    def __init__(self, id):
        self.id = id
        self.listCmd = []
        
        self.listCmd.append( bytes.fromhex("C3C3D96999A5AA66A99969A95A95A9A96AA95C3D96999A5AA66A99969A95A95A9A96AA95") )
        self.listCmd.append( bytes.fromhex("61E1EAB4D2B3534CCCCD34CB2D3352B54AB2AE1EAB4D2B3534CCCCD34CB2D3352B54AB2A") )
        self.listCmd.append( bytes.fromhex("61E1ED2CB4D4D2CACAAAAB2B354CD32B4D55301ED2CB4D4D2CACAAAAB2B354CD32B4D5530") )

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
        self.listOfStores.append( StoreCmdSet(5) ) 

class StoreController:

    def __init__(self):

        self.clusterOfStores = ClusterOfStores("System open space")

        with cc1101.CC1101(lock_spi_device=True) as transceiver:
            print("defaults:", transceiver)
            transceiver.set_base_frequency_hertz(868.34e6)
            transceiver.set_symbol_rate_baud(2400)
            transceiver._set_modulation_format(0b000)
            transceiver.set_sync_mode(cc1101.SyncMode.NO_PREAMBLE_AND_SYNC_WORD)
            # transceiver.set_sync_mode(cc1101.SyncMode.NO_PREAMBLE_AND_SYNC_WORD)
            # transceiver.set_preamble_length_bytes(2)
            # transceiver.set_sync_word(b"\x12\x34")
            transceiver.disable_checksum()
            transceiver.set_output_power((0, 0xC2))  # 
            print(transceiver)
            print("state", transceiver.get_marc_state().name)
            print("base frequency", transceiver.get_base_frequency_hertz(), "Hz")
            print("symbol rate", transceiver.get_symbol_rate_baud(), "Baud")
            print("modulation format", transceiver.get_modulation_format().name)
            sync_mode = transceiver.get_sync_mode()
            print("sync mode", sync_mode)
            if sync_mode != cc1101.SyncMode.NO_PREAMBLE_AND_SYNC_WORD:
                print("preamble length", transceiver.get_preamble_length_bytes(), "bytes")
                print("sync word", transceiver.get_sync_word())
            print("output power settings (patable)", transceiver.get_output_power())

    def transmitCommand(self, id, cmd):
        try:
            with cc1101.CC1101(lock_spi_device=True) as transceiver:
                print("defaults:", transceiver)
                transceiver.set_base_frequency_hertz(868.34e6)
                transceiver.set_symbol_rate_baud(2400)
                transceiver._set_modulation_format(0b000)
                transceiver.set_sync_mode(cc1101.SyncMode.NO_PREAMBLE_AND_SYNC_WORD)
                # transceiver.set_sync_mode(cc1101.SyncMode.NO_PREAMBLE_AND_SYNC_WORD)
                # transceiver.set_preamble_length_bytes(2)
                # transceiver.set_sync_word(b"\x12\x34")
                transceiver.disable_checksum()
                transceiver.set_output_power((0, 0xC2))  # 
                print(transceiver)
                print("state", transceiver.get_marc_state().name)
                print("base frequency", transceiver.get_base_frequency_hertz(), "Hz")
                print("symbol rate", transceiver.get_symbol_rate_baud(), "Baud")
                print("modulation format", transceiver.get_modulation_format().name)
                sync_mode = transceiver.get_sync_mode()
                print("sync mode", sync_mode)
                if sync_mode != cc1101.SyncMode.NO_PREAMBLE_AND_SYNC_WORD:
                    print("preamble length", transceiver.get_preamble_length_bytes(), "bytes")
                    print("sync word", transceiver.get_sync_word())
                print("output power settings (patable)", transceiver.get_output_power())

                print("\nstarting transmission")
                transceiver.transmit(self.clusterOfStores.listOfStores[id].listCmd[cmd])
        except:
            print("Unable to send command")
