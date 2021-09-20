import wmi
import os
import subprocess
import re
import socket, sys

ip = 'PMIRSINIWH0011'
username = 'g-csct'
password = 'Help0000'
from socket import *
try:
    print("Establishing connection to %s" %ip)
    connection = wmi.WMI('PMIRSINIWH0011', user=username, password=password)
    print("Connection established 11")

    for d in connection.query('SELECT * FROM CIM_DataFile WHERE Name = "C:\\Temp\NSM_CLIENT"'):
        for file in result:
            print (file.Name)

    connection = wmi.WMI('PMIRSINIWH0008', user=username, password=password)
    print("Connection established 88")
except wmi.x_wmi:
    print("Your Username and Password of "+getfqdn(ip)+" are wrong.")