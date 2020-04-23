# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:48:33 2020

@author: guilh
"""

# This codes implements a solution to the codenation test
import requests
import json
import hashlib

# Function to change the JSON Values
def changejsonvalues(JSONObject, Pair, Value):
    JSONObject[Pair] = Value

# my token a90b0ba4999ff974a99887d6397969d6520f35dd
mytoken = 'a90b0ba4999ff974a99887d6397969d6520f35dd'

# URL string
geturl = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={}".format(mytoken) 
posturl = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token={}".format(mytoken)

# Send get request
getrequest = requests.get(geturl)

# Get content from json and put on variable
JSON = json.loads(getrequest.content)

# Get the encrypted message from JSON
encryptedmessage = JSON.get('cifrado')

# Control variables
a = 0
minnumber = 97
maxnumber = 122

# Decrypted
decrypted = ""
#print(decrypted)

letterlist = []

# Loop to break encryption
while a < len(encryptedmessage):
    
    # Control variable
    constantnumber = 0
    
    # Actual letter
    actualletter = ord(encryptedmessage[a])
    
    # Control
    if (actualletter not in range(minnumber, (maxnumber + 1))):
        
        # Add the value to the list
        letterlist.append(chr(actualletter))
        
        # Increment
        a += 1
        
        # Loop control
        continue
    
    # Loop to make the right letter
    while constantnumber < 10:
    
        # Control to not break the logic
        if (actualletter - 1) < minnumber:
            actualletter = maxnumber
            # Increment
            constantnumber += 1
        
        # Decrement to reach right letter
        actualletter -= 1
        
        # Increment
        constantnumber += 1
    
    # Add the value to the list
    letterlist.append(chr(actualletter))    
    
    # Increment
    a += 1

# Put the letter decrypted list on variable
decrypted = decrypted.join(letterlist)

# Call function to change JSON values
changejsonvalues(JSON, 'decifrado', decrypted) 

# Create the hash
toencrypt = decrypted.encode('utf-8')
encryptedsummary = hashlib.sha1(toencrypt).hexdigest()

# Call function to change JSON values
changejsonvalues(JSON, 'resumo_criptografico', encryptedsummary)

"""
AFTER DOING THIS CODE, I'VE JUST USED INSOMNIA REST
API TO SEND THE FILE TO ACELERA DEV
"""
