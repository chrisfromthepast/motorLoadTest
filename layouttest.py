import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="darkly")  # Always create the root window first
mainframe = ttk.Frame(root, padding=(3,3,12,12)).grid(column=0, row=0, sticky=(N, S, E, W))

root.title("AVL Motor Load Tester")
root.geometry("950x600")

modbus_ip_var = ttk.StringVar(value="192.168.13.51")  # Default value

# Add an entry field for the Modbus IP address in your UI
modbus_ip_label = ttk.Label(mainframe, text="Modbus IP: ").grid(column=0, row=0)
modbus_ip_entry = ttk.Entry(mainframe, textvariable=modbus_ip_var).grid(column=1, row=0)

# Tester


# Add a global StringVar for DeviceOwner
device_owner = ttk.StringVar()
device_owner_label = ttk.Label(mainframe, text="Device Owner: ").grid(column=0, row=1)
device_owner_entry = ttk.Entry(mainframe, textvariable=device_owner).grid(column=1, row=1)

# Address

# Hoist description

# Manufacturers

# Model

# Serial No

# Rated Capacity

# Power Supply

# Pounds

# Overload

# Current draw

# Current Values

# Comments

# Date

# Signiture

#



root.mainloop()
