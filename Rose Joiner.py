import os; import sys
from turtle import clear; import ultrarequests; import discord; import pystyle; import time
from pystyle import Add, Colors, Colorate, Center, Write

# Thanks for using this tool :)

Termed = (f"""
______                   ___       _                 
| ___ \                 |_  |     (_)                
| |_/ /___  ___  ___      | | ___  _ _ __   ___ _ __ 
|    // _ \/ __|/ _ \     | |/ _ \| | '_ \ / _ \ '__|
| |\ \ (_) \__ \  __/ /\__/ / (_) | | | | |  __/ |   
\_| \_\___/|___/\___| \____/ \___/|_|_| |_|\___|_|   
                                                     
""")
text = " A Discord Token Joiner\n Made By Termed$#0001\n https://github.com/NathanOnTop"
BANNERlol = Add.Add(Termed, text, 3)
print(Colorate.Horizontal(Colors.red_to_purple, str(BANNERlol), 1))
print('')
# Input ur discord server url
link = input(Colorate.Horizontal(Colors.red_to_purple,"Input your Discord Server Url: "))
if len(link) > 6:
    link = link[19:]
apilink = "https://discordapp.com/api/v6/invite/" + str(link)

print(link)

with open('tokens.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip()
            headers={
                'Authorization': token
                }
            ultrarequests.post(apilink, headers=headers)
        print(Colorate.Horizontal(Colors.red_to_blue,"[+] All valid tokens have joined!"))
        input(Colorate.Horizontal(Colors.red_to_blue,"Click Enter To Exit: "))




