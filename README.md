# DolphinFeeder
Gamecube and Wii game backup "compression" is frequently done with the .dec filetype.  Unfortunately the best PC emulator for these games will not play these files.  It can become somewhat of a hassle to have to unzip these files, then convert them from .dec to .iso to finally be able to play them with Dolphin.  Dolphin feeder is a simple windows application to streamline this process being a middleman between you or a frontend software and the Dolphin emulator.

## Requirements
- Dolphin Emulator
- nNasos 1.8

## Current Features
- **Drag and Drop Functionality**
	<br>For those who do not use a front end, you can just drag and drop your unzipped .dec files onto the included .exe or .bat file and play in minutes.
- **Portable**
	<br>These files do not need to be anywhere special as long as the config file is set up properly.
- **Automatic Cleanup**
	<br>When you are done playing, the program will delete the converted .iso file so your drive does not get overfilled.  It will obviously keep the source file.

## Planned Features
- **Ability to drag and drop / run zipped files**
	<br>This is to streamline the process even more by allowing you to just run your zipped .dec files and not have to have them unzipped first.  (Using a front-end like launchbox already solves this).
- **Add Dolphin command line args to config.txt**
	<br>Right now it only uses default "-b -e" arguments to just load a game.
- **Additional comman line arguments**
	<br>Planned: Option to verify the .dec file before conversion.  Option to not delete the file at the end.

## Setup
Right now this is a windows only program.  Go to the releases page and you can download one of two versions.

- **Compiled Windows .exe version**
- **Python Source File with a .bat file**

Each version works the same.  Some people might not want to download an exe so the other option is there.  The .exe is just the python file ran through auto-py-to-exe.  Both are 100% portable and do not need to be installed.

### Usage
- **First, setup config.txt file**
	<br>Open config.txt then copy and paste the path to the required programs and save the file.  Make sure this file is housed right next to your DolphinFeeder application.
- **You are done**
	<br>Just drag and drop any .dec file onto DolphinFeeder.exe or pyDragAndDrop.bat.  Note that they cannot be in a zipped format.  The program will convert the .dec, run dolphin then remove the excess file after you are done playing.
-  **Optional Frontend Setup**
	<br>There are many different front ends but the setup should be similar.  Instead of pointing your frontend to run dolphin.exe, you want to point it to either DolphinFeeder.exe or pyDragAndDrop.bat.  Again remember, the files must be unzipped already.  I personally use launchbox which has a setting to check in the emulators settings to "Extract ROM archives before running".  
