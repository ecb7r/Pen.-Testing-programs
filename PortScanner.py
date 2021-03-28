# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 14:32:30 2021

@author: Eric B

This program is designed to scan an IP address for all open ports
and list each of them.

In my case, the target is on a pfsense internal network so the VM running
this program must be ran on the same internal network or you won't be able to scan 
it. The program uses the socket library to use sockets to scan ports
and it also uses the system library to exit the program if Ctrl+C is pressed or
it closes if it has issues connecting to the target.

The program must be ran from the terminal in the same directory using the command
sudo python3 [this program's name].py -i
The above command will prompt you for the IP address, enter it and press enter
to start the scan. If anything else is entered, it will give an error message for invalid input.

"""

import socket #import socket library
import sys #import system library

target = '' #create a target variable to store IP later.

if(len(sys.argv) == 2 and sys.argv[1] == '-i'): #if the program is ran through terminal with a -i
    print("Please enter the IP address of the target to scan: ") #ask for the IP address
    target = input() #put the IP address input into the target variable

elif(len(sys.argv) == 1): #if the program isn't ran with a -i
    print("Please enter '-i' to enter an IP address to scan.") #print an error
    sys.exit() #and exit the program
    
else: #otherwise if anything else is ran
    print("Invalid input, please try again!") #print an error
    sys.exit() #and exit the program

try: #let's try to find some open ports
    
    for port in range(1,65535): #for each port number in the whole range
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #let's create a socket
        socket.setdefaulttimeout(1) #create a timeout 
        
        result = s.connect_ex((target, port)) #result variable to store the socket value returned
        if result == 0: #if the result returned is 0
            print('Port ', port, ' is open.') #we print that that port is open 
        s.close() #then close the socket
        
except KeyboardInterrupt: #when the user presses Ctrl + C
    print("\n Closing...") #print a closing message
    sys.exit() #and exit
    
except socket.error: #if there's a socket error
    print("\n Issues connecting to target.") #print an error message
    sys.exit() #and exit
