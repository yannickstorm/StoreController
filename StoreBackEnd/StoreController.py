import time
import cc1101
import logging

logging.basicConfig(level=logging.INFO)

class StoreCmdSet:
    def __init__(self, id):
        self.id = id
        self.listCmd = []

    def print(self):
        print("Store: " + self.id)

    def configureCmd(self, cmdStop, cmdUp, cmdDown):

        self.listCmd.append( bytes.fromhex(cmdStop) ) # Stop command
        self.listCmd.append( bytes.fromhex(cmdUp) ) # Up command
        self.listCmd.append( bytes.fromhex(cmdDown) ) # Down command

 
class ClusterOfStores:

    def __init__(self, name):
        self.name = name
        self.listOfStores = []

C3C3D96999A5AA66A99969A95A95A9A96AA95C3D96999A5AA66A99969A95A95A9A96AA95
        self.listOfStores.append( StoreCmdSet(0) ) 
        self.listOfStores[-1].configureCmd("C3C3D96999A5AA66A99969A95A95A9A96AA95C3D96999A5AA66A99969A95A95A9A96AA95", "61E1ED2CB4D4D2CACAAAAB2B354CD32B4D55301ED2CB4D4D2CACAAAAB2B354CD32B4D553", "61E1EAB4D2B3534CCCCD34CB2D3352B54AB2AE1EAB4D2B3534CCCCD34CB2D3352B54AB2A")
        self.listOfStores.append( StoreCmdSet(1) )
        self.listOfStores[-1].configureCmd("C3C3D5665AA596956656556A656A55655A6A9C3D5665AA596956656556A656A55655A6A9", "61E1EB34CCAD4AB2CCB2CB4CAB354B4CB3552E1EB34CCAD4AB2CCB2CB4CAB354B4CB3552", "61E1ECAACCB352AB4B553354D34B535354D2AE1ECAACCB352AB4B553354D34B535354D2A")
        self.listOfStores.append( StoreCmdSet(2) ) 
        self.listOfStores[-1].configureCmd("C3C3D659A9999A965AA66A9655556A5A99969C3D659A9999A965AA66A9655556A5A99969", "61E1ECB4B4AB353334B2B2AB333334D34B54CE1ECB4B4AB353334B2B2AB333334D34B54C", "61E1ED4D4D52D32AAAACB32AAAB2D2CD3534AE1ED4D4D52D32AAAACB32AAAB2D2CD3534A")
        self.listOfStores.append( StoreCmdSet(3) ) 
        self.listOfStores[-1].configureCmd("C3C3DAA59A9569A65A669A69A5A99A66A656603DAA59A9569A65A669A69A5A99A66A6566", "61E1EAD4B32D535554CCAAAB355552AB4D4CB01EAD4B32D535554CCAAAB355552AB4D4CB", "61E1EB4AAAAB4CCD34ACCB4ACD2B4B352CB2B01EB4AAAAB4CCD34ACCB4ACD2B4B352CB2B")
        self.listOfStores.append( StoreCmdSet(4) )

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
