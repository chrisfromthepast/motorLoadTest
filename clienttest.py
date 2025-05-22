import struct
from pymodbus.client import ModbusTcpClient

# Global variables for each parameter (first six 30000 registers)
volts_1 = None
volts_2 = None
volts_3 = None
current_1 = None
current_2 = None
current_3 = None

def read_first_six_3000_parameters(ip, unit=1):
    """
    Reads the first six 3X (input) parameters, where each parameter is stored in two consecutive 16-bit registers.
    Returns a dictionary with parameter names and their 32-bit values.
    """
    client = ModbusTcpClient(ip)
    result = client.read_input_registers(0, 12, unit=unit)  # 6 parameters x 2 registers each
    client.close()
    params = {}
    if hasattr(result, "registers") and len(result.registers) == 12:
        names = ["volts_1", "volts_2", "volts_3", "current_1", "current_2", "current_3"]
        for i, name in enumerate(names):
            high = result.registers[i*2]
            low = result.registers[i*2+1]
            # Combine to 32-bit and unpack as float (big-endian)
            raw = (high << 16) | low
            bytes_ = raw.to_bytes(4, byteorder='big')
            value = struct.unpack('>f', bytes_)[0]
            params[name] = value
    else:
        print("Read failed:", result)
    return params

# Example usage:
params = read_first_six_3000_parameters('10.10.100.254')

if params:
    volts_1 = params["volts_1"]
    volts_2 = params["volts_2"]
    volts_3 = params["volts_3"]
    current_1 = params["current_1"]
    current_2 = params["current_2"]
    current_3 = params["current_3"]
    print(f"Volts 1: {volts_1}")
    print(f"Volts 2: {volts_2}")
    print(f"Volts 3: {volts_3}")
    print(f"Current 1: {current_1}")
    print(f"Current 2: {current_2}")
    print(f"Current 3: {current_3}")
else:
    print("Could not read all parameters.")