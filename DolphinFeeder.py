"""
DolphinFeeder.py
"""

import re
import os
import sys
import time
from sys import argv

verify = 0
close = 1

def helpPrint(platform):
    if platform == 0: # Windows exe
        print()
        print("dec2Dolphin Help")
        print("-------------------------------")
        print()
        print("Base use (When in applications directory with config file)")
        print("> ./dec2Dolphin.exe \"PATH/TO/YOUR/decFILE.dec\"")
        print()
        input("Press any key to exit...")
        os._exit(0)
    else: # Python script
        print()
        print("dec2Dolphin Help")
        print("-------------------------------")
        print()
        print("Base use (When in applications directory with config file)")
        print("> python dec2Dolphin.py \"PATH/TO/YOUR/decFILE.dec\"")
        print()
        input("Press any key to exit...")
        os._exit(0)

# Check number of args
if (len(argv) < 2 or len(argv) > 2):
    print("Invalid # of args, do -help for info")

# Check if being ran through .exe or .py
# The default directory is different depending on platform
if argv[0].rsplit(".", 1)[1] == "exe":

    if argv[1] == "-help":
        helpPrint(0)

    try:
        print("Running from Windows Exe...")
        print("-------------------------------")
        a = argv[0].rsplit("\\", 1)[0]
        a = a + "\\config.txt"
        print("Looking for config file here: " + a)
        f = open(a, "r")
    except:
        print("No config file found, put config.txt in same directory as dec2Dolphin (Shown above)")
        print("Press enter to exit...")
elif argv[0].rsplit(".", 1)[1] == "py":

    if argv[1] == "-help":
        helpPrint(1)
    try:
        print("Running from Python Script...")
        print("-------------------------------")
        f = open("config.txt", "r")
    except:
        print("No config file found, put config.txt in same directory as dec2Dolphin (Shown above)")
        print("Press enter to exit...")

# Extract paths from config.txt
nasosPath = re.findall(r'"([^"]*)"', f.readline())[0]
dolphinPath = re.findall(r'"([^"]*)"', f.readline())[0]

# Get input file for nNasos
decFile = argv[1]
print("Input .dec File: " + decFile)
output = decFile.rsplit(".", 1)[0]

# Run nNasos
print("Converting .dec -> .iso")
os.system(nasosPath + " " + "-n " +  "\"" + decFile + "\"")

# Run Dolphin
print("Starting Dolphin")
os.system(dolphinPath + " -b -e " + "\"" + output + "\"")

# When emulation is finished, remove ISO
print("Removing Extracted .dec File at: " + output)
os.system("DEL /f " + "\"" + output + "\"")

print("Deletion Complete")
print("Auto-closing in 3 seconds...")
time.sleep(5)
os._exit(0)