import struct
from pymodbus.client.sync import ModbusTcpClient

def read_first_six_3000_parameters(ip, unit=1):
    """
    Reads the first six 3X (input) parameters, where each parameter is stored in two consecutive 16-bit registers.
    Returns a dictionary with parameter names and their 32-bit values.
    """

    #break out the globals
    #tick through 3000 times,  check aray size for error checking
    #choose a value frfom the array we build

    client = ModbusTcpClient(ip)
    try:
        if not client.connect():
            print(f"Connection to {ip} failed.")
            return {}
        result = client.read_input_registers(0, 12, unit=unit)
        if not result or not hasattr(result, "registers") or result.registers is None or len(result.registers) != 12:
            print(f"Read failed: {result}")
            return {}
        params = {}
        names = ["volts_1", "volts_2", "volts_3", "current_1", "current_2", "current_3"]
        for i, name in enumerate(names):
            high = result.registers[i*2]
            low = result.registers[i*2+1]
            raw = (high << 16) | low
            bytes_ = raw.to_bytes(4, byteorder='big')
            value = struct.unpack('>f', bytes_)[0]
            params[name] = value
        return params
    except Exception as e:
        print(f"Exception during Modbus read: {e}")
        return {}
    finally:
        client.close()