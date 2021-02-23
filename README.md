# ESwindowsMoonlightGameList
Automatic population of the EmulationStation roms folder with startable .cmd files to launch Moonlight as well as grabbing boxarts from Moonlight for ES on Windows

# Setup (on the client machine):

## Determine your Moonlight Server's UUID. 
In windows, you can find it in the registry at HKEY_CURRENT_USER\SOFTWARE\Moonlight Game Streaming Project\Moonlight\hosts\\{hostnumber}
open the included file and change the "UUID" field to the UUID you just found. Also edit the "emulationstation_location" if you have not installed it in %USERPROFILE%\\.emulationstation

## Create the folder "moonlight" in your emulationstation/roms/ directory

## Add "Moonlight" to your es_systems.cfg. 
See "es_systems.cfg" for an example

# Excecute the Script with Python 3

Enjoy!

Note: You may have to Scrape and/or start the game after it's entry has been made in order for the boxart to be fetched. Emulationstation does not seem to add games to the gamelist.xml otherwise.
