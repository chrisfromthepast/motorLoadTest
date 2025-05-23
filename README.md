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


There is a load cell on its way, which we will also query to get 1 value for mass.
Not sure of those details right now, but it would probably be the only input register, and perhaps the device id is hardcoded, in which case the alpha would move to a different device ID

Functions:
Calibrate: this should open a window so that modbus parameters can be changed and stored in the program as a default
Poll: poll the modbus (this could be continuous, or one shot, but it needs to be at a specific time when the motor itself if under tension and drawing current.
Loadcell should be continuously polled, and displayed on the UI 5 times.a second
Barcode: take in keyboard input of a barcode number in our inventory system, use Flex API to query the inventory system to return the serial number for the motor under test. Display this serial number on the UI, and place it into a specific field in the pdf we are modifying.
pdf: there is a pdf that is the standard form we use, we just want to stick the data we are collecting into some of the fields on this pdf: 3 voltages, 3 currents, a serial number, a load cell number, serial number and time stamp.

This pdf needs to be saved in the maintenance log in flex (using their API) and it also needs to go to a folder in our company goggle docs using a different API

Need some sort of error handling


The reports already exist as .pdf’s, so the print function needs to modify the pdf, add values from memory

## Python Version

This project requires **Python 3.8**.  
Please ensure you are using Python 3.8 when creating your virtual environment or running the code.

## Creating a Python 3.8 Virtual Environment

1. Delete any existing `venv` folder.
2. Run: `python3.8 -m venv venv`
3. Activate the environment and install requirements:
   ```
   venv\Scripts\activate
   pip install -r requirements.txt
   ```
