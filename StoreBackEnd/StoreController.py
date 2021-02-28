import time
import cc1101
import logging

logging.basicConfig(level=logging.INFO)

class StoreController:

    def __init__(self):
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
            transceiver.transmit(bytes([0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x61,0xE1,0xEC,0xCC,0xAA,0xCC,0xB3,0x34,0xCD,0x2D,0x53,0x33,0x4C,0xAB,0x32,0xCA,0xD5,0x4A,0xD0,0x1E,0xCC,0xCA,0xAC,0xCB,0x33,0x4C,0xD2,0xD5,0x33,0x34,0xCA,0xB3,0x2C,0xAD,0x54,0xAD]))
            time.sleep(1.0)
            transceiver.transmit(bytes([0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x61,0xE1,0xED,0x53,0x4C,0xB5,0x2C,0xD4,0xB3,0x55,0x4B,0x52,0xD3,0x4B,0x54,0xB3,0x4A,0xAB,0x2E,0x1E,0xD5,0x34,0xCB,0x52,0xCD,0x4B,0x35,0x54,0xB5,0x2D,0x34,0xB5,0x4B,0x34,0xAA,0xB2]))
            time.sleep(1.0)
            transceiver.transmit(bytes([0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xC3,0xC3,0xD6,0x56,0x96,0x95,0x5A,0x99,0x66,0x96,0xAA,0x95,0xA6,0xAA,0x95,0x66,0x95,0x69,0xA0,0x3D,0x65,0x69,0x69,0x55,0xA9,0x96,0x69,0x6A,0xA9,0x5A,0x6A,0xA9,0x56,0x69,0x56,0x9A]))
            time.sleep(1.0)
            transceiver.transmit(bytes([0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xC3,0xC3,0xD6,0xA9,0xA6,0xA9,0x95,0xAA,0x5A,0xA6,0x6A,0xA6,0x56,0x5A,0xA5,0x59,0xA9,0x66,0x9C,0x3D,0x6A,0x9A,0x6A,0x99,0x5A,0xA5,0xAA,0x66,0xAA,0x65,0x65,0xAA,0x55,0x9A,0x96,0x69]))
            time.sleep(1.0)
            transceiver.transmit(bytes([0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x61,0xE1,0xEB,0x4C,0xD4,0xD2,0xD4,0xCD,0x2A,0xD4,0xB2,0xB3,0x2D,0x4C,0xCB,0x2C,0xD4,0xAC,0xAE,0x1E,0xB4,0xCD,0x4D,0x2D,0x4C,0xD2,0xAD,0x4B,0x2B,0x32,0xD4,0xCC,0xB2,0xCD,0x4A,0xCA]))

            time.sleep(1.0)
            transceiver.transmit(bytes([0x61,0xE1,0xEC,0xCC,0xAA,0xCC,0xB3,0x34,0xCD,0x2D,0x53,0x33,0x4C,0xAB,0x32,0xCA,0xD5,0x4A,0xD0,0x1E,0xCC,0xCA,0xAC,0xCB,0x33,0x4C,0xD2,0xD5,0x33,0x34,0xCA,0xB3,0x2C,0xAD,0x54,0xAD]))
            time.sleep(1.0)
            transceiver.transmit(bytes([0x61,0xE1,0xED,0x53,0x4C,0xB5,0x2C,0xD4,0xB3,0x55,0x4B,0x52,0xD3,0x4B,0x54,0xB3,0x4A,0xAB,0x2E,0x1E,0xD5,0x34,0xCB,0x52,0xCD,0x4B,0x35,0x54,0xB5,0x2D,0x34,0xB5,0x4B,0x34,0xAA,0xB2]))
            time.sleep(1.0)
            transceiver.transmit(bytes([0xC3,0xC3,0xD6,0x56,0x96,0x95,0x5A,0x99,0x66,0x96,0xAA,0x95,0xA6,0xAA,0x95,0x66,0x95,0x69,0xA0,0x3D,0x65,0x69,0x69,0x55,0xA9,0x96,0x69,0x6A,0xA9,0x5A,0x6A,0xA9,0x56,0x69,0x56,0x9A]))
            time.sleep(1.0)
            transceiver.transmit(bytes([0xC3,0xC3,0xD6,0xA9,0xA6,0xA9,0x95,0xAA,0x5A,0xA6,0x6A,0xA6,0x56,0x5A,0xA5,0x59,0xA9,0x66,0x9C,0x3D,0x6A,0x9A,0x6A,0x99,0x5A,0xA5,0xAA,0x66,0xAA,0x65,0x65,0xAA,0x55,0x9A,0x96,0x69]))
            time.sleep(1.0)
            transceiver.transmit(bytes([0x61,0xE1,0xEB,0x4C,0xD4,0xD2,0xD4,0xCD,0x2A,0xD4,0xB2,0xB3,0x2D,0x4C,0xCB,0x2C,0xD4,0xAC,0xAE,0x1E,0xB4,0xCD,0x4D,0x2D,0x4C,0xD2,0xAD,0x4B,0x2B,0x32,0xD4,0xCC,0xB2,0xCD,0x4A,0xCA]))