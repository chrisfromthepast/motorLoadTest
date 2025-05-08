from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('10.10.100.254')
result = client.read_coils(1, 1)

print(result.bits[0])
client.close()