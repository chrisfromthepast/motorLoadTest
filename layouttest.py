import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="darkly")  # Always create the root window first
mainframe = ttk.Frame(root, padding=(3,3,12,12)).grid(column=0, row=0, sticky=(N, S, E, W))

root.title("AVL Motor Load Tester")
root.geometry("950x600")

# Modbus IP
modbus_ip_var = ttk.StringVar(value="192.168.13.51")  # Default value
modbus_ip_label = ttk.Label(mainframe, text="Modbus IP: ").grid(column=0, row=0)
modbus_ip_entry = ttk.Entry(mainframe, textvariable=modbus_ip_var).grid(column=1, row=0)

# Tester
device_tester = ttk.StringVar()
device_tester_label = ttk.Label(mainframe, text="Device Tester: ").grid(column=0, row=1)
device_tester_entry = ttk.Entry(mainframe, textvariable=device_tester).grid(column=1, row=1)

# Device Owner
device_owner = ttk.StringVar()
device_owner_label = ttk.Label(mainframe, text="Device Owner: ").grid(column=0, row=2)
device_owner_entry = ttk.Entry(mainframe, textvariable=device_owner).grid(column=1, row=2)

# Address
owner_addr = ttk.StringVar()
owner_addr_label = ttk.Label(mainframe, text="Owner Address: ").grid(column=0, row=3)
owner_addr_entry = ttk.Entry(mainframe, textvariable=owner_addr).grid(column=1, row=3)

# Hoist description
hoist_desc = ttk.StringVar()
hoist_desc_label = ttk.Label(mainframe, text="Hoist Description: ").grid(column=0, row=4)
hoist_desc_entry = ttk.Entry(mainframe, textvariable=hoist_desc).grid(column=1, row=4)

# Manufacturer
manufacturer = ttk.StringVar()
manufacturer_label = ttk.Label(mainframe, text="Manufacturer: ").grid(column=0, row=5)
manufacturer_entry = ttk.Entry(mainframe, textvariable=manufacturer).grid(column=1, row=5)

# Model
model = ttk.StringVar()
model_label = ttk.Label(mainframe, text="Model: ").grid(column=0, row=6)
model_entry = ttk.Entry(mainframe, textvariable=model).grid(column=1, row=6)

# Serial No
serial_no = ttk.StringVar()
serial_no_label = ttk.Label(mainframe, text="Serial Number: ").grid(column=0, row=7)
serial_no_entry = ttk.Entry(mainframe, textvariable=serial_no).grid(column=1, row=7)

# Rated Capacity
rated_cap = ttk.StringVar()
rated_cap_label = ttk.Label(mainframe, text="Rated Capacity: ").grid(column=0, row=8)
rated_cap_entry = ttk.Entry(mainframe, textvariable=rated_cap).grid(column=1, row=8)

# Power Supply
power_supply = ttk.StringVar()
power_supply_label = ttk.Label(mainframe, text="Power Supply: ").grid(column=0, row=9)
power_supply_entry = ttk.Entry(mainframe, textvariable=power_supply).grid(column=1, row=9)

# Pounds
pounds = ttk.StringVar()
pounds_label = ttk.Label(mainframe, text="Pounds: ").grid(column=0, row=10)
pounds_entry = ttk.Entry(mainframe, textvariable=pounds).grid(column=1, row=10)

# Overload
overload = ttk.StringVar()
overload_label = ttk.Label(mainframe, text="Overload: ").grid(column=0, row=11)
overload_checkbox = ttk.Checkbutton(mainframe, variable=overload, onvalue=True, offvalue=False).grid(column=1, row=11)
#pounds_entry = ttk.Entry(mainframe, textvariable=pounds).grid(column=1, row=10)

# Current draw
current_draw = ttk.StringVar()
current_draw_label = ttk.Label(mainframe, text="Current Draw: ").grid(column=0, row=12)
current_draw_entry = ttk.Entry(mainframe, textvariable=current_draw).grid(column=1, row=12)

# Current Values
test_current_heading = ttk.Label(mainframe, text="Test Current Draw").grid(column=2, row=0, columnspan=2)

current_p1_label = ttk.Label(mainframe, text="Phase 1: ").grid(column=2, row=1)
current_p1_entry = ttk.Entry(mainframe).grid(column=3, row=1)

current_p2_label = ttk.Label(mainframe, text="Phase 2: ").grid(column=2, row=2)
current_p2_entry = ttk.Entry(mainframe).grid(column=3, row=2)

current_p3_label = ttk.Label(mainframe, text="Phase 3: ").grid(column=2, row=3)
current_p3_entry = ttk.Entry(mainframe).grid(column=3, row=3)

# Comments

# Date

# Signiture

#



root.mainloop()
