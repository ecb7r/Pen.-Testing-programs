# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 22:18:23 2021

@author: Eric B

This tool is used to crack passwords from a shadow file by using any
wordlist you put a path for. I removed the Blowfish and Crypt algorithms methods
from the functions.

Python 3.7 language

Instructions: to run the program, go to the directory where this file is saved,
then type sudo python3 [this program's name] [directory of shadow file] [directory of wordlist]
you can also add a '-m' to the end to get the mangle rules which check to see if the password
is capitalized or if it's capitalized and has a special character at the end.
"""

import sys #import sys library
import crypt #import crypt library
 
def wordlistChecker(shadowHash, wordlist): #function to compare wordlist hash with shadow file hashes
    
    try: #lets try to open the wordlist given
        
        wlist = open(wordlist, 'r') #open the wordlist designated earlier
    
    except: #if it won't open or wrong path lets print an error and close the program
        
        print("Wordlist wasn't found or path was incorrect!") #error message
        sys.exit() #close the program if the try fails
        
    cryptType = shadowHash.split("$")[1] #get the encryption ID
    
    if cryptType == '6': #if the encryption ID is 6 then it runs this loop
        
        print("Algorithm: SHA-512") #prints that the algorithm is SHA-512
        salt = shadowHash.split("$")[2] #finds the salt after the encryption ID
        insalt = "$" + cryptType + "$" + salt + "$" #creates the whole salt to crypt.crypt later
        
        for password in wlist.readlines(): #for loop to read through the wordlist
            
            password = password.strip('\n') #strip the new lines
            sha512_passwordHash = crypt.crypt(password, insalt) #get the SHA-512 hash to compare
                                                                #with the shadow's hash
            
            if(sha512_passwordHash == shadowHash): #if the hashes are equal
                
                print("Password: " + password) #print the password
                print("____________________\n") #just to separate the user, algorithm, and password
        
    if cryptType == '5': #if the encryption ID is 5 then it runs this loop
        
        print("Algorithm: SHA-256") #prints that the algorithm is SHA-256
        salt = shadowHash.split("$")[2] #finds the salt after the encryption ID
        insalt = "$" + cryptType + "$" + salt + "$" #creates the whole salt to crypt.crypt later
        
        for password in wlist.readlines(): #for loop to read through the wordlist
            
            password = password.strip('\n')  #strip the new lines
            sha256_passwordHash = crypt.crypt(password, insalt) #get the SHA-256 hash to compare
                                                                #with the shadow's hash
            
            if(sha256_passwordHash == shadowHash): #if the hashes are equal
                
                print("Password: " + password) #print the password
                print("____________________\n") #just to separate the user, algorithm, and password
                
    if cryptType == '1': #if the encryption ID is 1 then it runs this loop
        
        print("Algorithm: MD5") #prints that the algorithm is MD5
        salt = shadowHash.split("$")[2] #finds the salt after the encryption ID
        insalt = "$" + cryptType + "$" + salt + "$" #creates the whole salt to crypt.crypt later
        
        for password in wlist.readlines(): #for loop to read through the wordlist
            
            password = password.strip('\n') #strip the new lines
            MD5_passwordHash = crypt.crypt(password, insalt) #get the MD5 hash to compare
                                                                #with the shadow's hash
            
            if(MD5_passwordHash == shadowHash): #if the hashes are equal
                
                print("Password: " + password) #print the password
                print("____________________\n") #just to separate the user, algorithm, and password

def manglerListChecker(shadowHash, wordlist): #function called for mangling rules
    
    try: #lets try to open the wordlist given
        
        wlist = open(wordlist, 'r') #open the wordlist designated earlier
    
    except: #if it won't open or wrong path lets print an error and close the program
        
        print("Wordlist wasn't found or path was incorrect!") #error message
        sys.exit() #close the program if the try fails
        
    cryptType = shadowHash.split("$")[1] #get the encryption ID
    
    if cryptType == '6': #if the encryption ID is 6 then it runs this loop
        
        print("Algorithm: SHA-512") #prints that the algorithm is SHA-512
        salt = shadowHash.split("$")[2] #finds the salt after the encryption ID
        insalt = "$" + cryptType + "$" + salt + "$" #creates the whole salt to crypt.crypt later
        
        for password in wlist.readlines(): #for loop to read through the wordlist
            
            password = password.strip('\n') #strip the new lines
            sha512_passwordHash = crypt.crypt(password, insalt) #get the SHA-512 hash to compare
                                                                #with the shadow's hash
            
            if(sha512_passwordHash == shadowHash): #if the hashes are equal
                
                print("Password: " + password) #print the password
                print("____________________\n") #just to separate the user, algorithm, and password
                break
            
            else: #if the hashes aren't equal lets check other options
                
                i = int(1) #here to help increment the ascii values
                password = password.capitalize() #capitalize to check
                sha512_passwordHash = crypt.crypt(password, insalt) #get the SHA-512 hash to compare
                                                                #with the shadow's hash
                
                if(sha512_passwordHash == shadowHash): #if the hashes are equal
                   
                    print("Password: " + password) #print the password
                    print("____________________\n") #just to separate the user, algorithm, and password
                    break
                
                for i in range(15): #for loop to check each special ascii character with each word
                    
                    password = password + chr(33 + i) #increment the ascii number to see all specials
                    sha512_passwordHash = crypt.crypt(password, insalt) #get the SHA-512 hash to compare
                                                                #with the shadow's hash
                    
                    if(sha512_passwordHash == shadowHash): #if the hashes are equal
                        
                        print("Password: " + password) #print the password
                        print("____________________\n") #just to separate the user, algorithm, and password
                        break
                    
                    password = password[:-1] #this is here to remove special characters every time the loop runs
        
    if cryptType == '5': #if the encryption ID is 5 then it runs this loop
        
        print("Algorithm: SHA-256") #prints that the algorithm is SHA-256
        salt = shadowHash.split("$")[2] #finds the salt after the encryption ID
        insalt = "$" + cryptType + "$" + salt + "$" #creates the whole salt to crypt.crypt later
        
        for password in wlist.readlines(): #for loop to read through the wordlist
            
            password = password.strip('\n') #strip the new lines
            sha256_passwordHash = crypt.crypt(password, insalt) #get the SHA-256 hash to compare
                                                                #with the shadow's hash
            
            if(sha256_passwordHash == shadowHash): #if the hashes are equal
                
                print("Password: " + password) #print the password
                print("____________________\n") #just to separate the user, algorithm, and password
                break

            else: #if the hashes aren't equal lets check other options
                
                i = int(1)
                password = password.capitalize() #capitalize to check
                sha256_passwordHash = crypt.crypt(password, insalt) #get the SHA-256 hash to compare
                                                                #with the shadow's hash
                
                if(sha256_passwordHash == shadowHash): #if the hashes are equal
                    
                    print("Password: " + password) #print the password
                    print("____________________\n") #just to separate the user, algorithm, and password
                    break
                
                for i in range(15): #for loop to check each special ascii character with each word
                    
                    password = password + chr(33 + i) #increment the ascii number to see all specials
                    sha256_passwordHash = crypt.crypt(password, insalt) #get the SHA-256 hash to compare
                                                                #with the shadow's hash
                    
                    if(sha256_passwordHash == shadowHash): #if the hashes are equal
                        
                        print("Password: " + password) #print the password
                        print("____________________\n") #just to separate the user, algorithm, and password
                        break
                    
                    password = password[:-1] #this is here to remove special characters every time the loop runs

    if cryptType == '1': #if the encryption ID is 1 then it runs this loop
        
        print("Algorithm: MD5") #prints that the algorithm is MD5
        salt = shadowHash.split("$")[2] #finds the salt after the encryption ID
        insalt = "$" + cryptType + "$" + salt + "$" #creates the whole salt to crypt.crypt later
        
        for password in wlist.readlines(): #for loop to read through the wordlist
           
            password = password.strip('\n') #strip the new lines
            MD5_passwordHash = crypt.crypt(password, insalt) #get the MD5 hash to compare
                                                                #with the shadow's hash
            
            if(MD5_passwordHash == shadowHash): #if the hashes are equal
                
                print("Password: " + password) #print the password
                print("____________________\n") #just to separate the user, algorithm, and password
                break
            
            else: #if the hashes aren't equal lets check other options
                
                i = int(1)
                password = password.capitalize() #capitalize to check
                MD5_passwordHash = crypt.crypt(password, insalt) #get the MD5 hash to compare
                                                                #with the shadow's hash
                
                if(MD5_passwordHash == shadowHash): #if the hashes are equal
                    
                    print("Password: " + password) #print the password
                    print("____________________\n") #just to separate the user, algorithm, and password
                    break
                
                for i in range(15): #for loop to check each special ascii character with each word
                    
                    password = password + chr(33 + i) #increment the ascii number to see all specials
                    MD5_passwordHash = crypt.crypt(password, insalt) #get the MD5 hash to compare
                                                                #with the shadow's hash
                    
                    if(MD5_passwordHash == shadowHash): #if the hashes are equal
                        
                        print("Password: " + password) #print the password
                        print("____________________\n") #just to separate the user, algorithm, and password
                        break
                    
                    password = password[:-1] #this is here to remove special characters every time the loop runs

def main(): #this is our main function to start the program
    
    shadowPath = sys.argv[1] #stores the path to the shadow file
    wordlist = sys.argv[2] #stores the path to the wordlist
    
    try: #lets try to open the shadow file given
        
        shadowFile = open(shadowPath, 'r') #open shadow file and read it
    
    except: #if it won't open or wrong path lets print an error and close the program
        
        print("File wasn't found or path was incorrect!") #error message
        sys.exit() #close the program if the try fails
    
    print("____________________\n") #adds some space between the terminal command and the first user
    if(len(sys.argv) == 3): #if the mangle rules aren't used    
        
        for shadowLines in shadowFile.readlines(): #for loop to read each line in the shadow file
            shadowLines = shadowLines.replace("\n","").split(":") #replace the new line in shadow and split
            
            if not shadowLines[1] in ['x', '*', '!']: #if loop excluding these characters
                userStore = shadowLines[0] #store the username after splitting at :
                shadowHash = shadowLines[1] #store the hash after splitting
                print("Username: " + userStore) #print the username
                wordlistChecker(shadowHash, wordlist) #call wordlistChecker function

    elif(len(sys.argv) == 4 and sys.argv[3] == '-m'): #otherwise if we use the mangle rules
        
         for shadowLines in shadowFile.readlines(): #for loop to read each line in the shadow file   
             shadowLines = shadowLines.replace("\n","").split(":") #replace the new line in shadow and split
             
             if not shadowLines[1] in ['x', '*', '!']: #if loop excluding these characters
                userStore = shadowLines[0] #store the username after splitting at :
                shadowHash = shadowLines[1] #store the hash after splitting
                print("Username: " + userStore) #print the username
                manglerListChecker(shadowHash, wordlist) #call manglerListChecker function

 
 

main() #call the main function

