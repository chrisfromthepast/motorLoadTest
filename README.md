This project is depreciated. please go to 

https://github.com/OMahoneyM/Hoist-Load-Tester



# motorLoadTest
RS485 to pdf data generation tool
The goal of this project is to generate reports from data collected from RS485 modbus devices


Modbus calibration:

Wave share RS485 to ETH is the server , it should pass the rs485 straight through. I was able to get data from the alpha20 to some of the modbus test programs available for windows, usually with a 30 day trial. 
TCP to RTU modbus server is at 10.10.100.254 port 502 I have not been able to get a class c address (there is an addidional instance of this server at (192.68.13.91)) to work across our network, so this currently assumes you are directly connected to a computer via ethernet to the class a address
 

alpha20A+ rules:
200ms between queries
8-bit binary, hexadecimal 0-9, A-F 2 hexadecimal characters contained in each 8-bit field of the message 
Format of Data Bytes:  4 bytes (32 bits) per parameter. Floating point format ( to IEEE 754) Most significant byte first (Alternative least significant byte first) 
 Error Checking Bytes 2 byte Cyclical Redundancy Check (CRC) 
1 start bit, 8 data bits, least significant bit sent first 1 bit for even/odd parity 1 stop bit if parity is used; 1 or 2 bits if no parity
Baud rate should be 19200

Actual data transmission is a query of the input registers. So, modbus function code 04 reads the input registers
Two consecutive 16 bit registers represent one parameter. Refer table 4 for the addresses of 3X registers (Parameters measured by the instruments). Each parameter is held in the 3X registers. Modbus Code 04 is used to access all parameters.
And the data we want is :
Voltage 1, 2, 3 and current 1,2,3 so, that’s the first 12 registers, and the query will look something like this:
Device code:01
Function code 04
Start address high 00
Start address low 0
Number of registers: 12 means the high byte is 1 and the low byte is 4? I'm not clear on this
And then you send 2 crc words
