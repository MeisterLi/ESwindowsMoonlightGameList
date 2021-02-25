# ESwindowsMoonlightGameList
Automatic population of the EmulationStation roms folder with startable .cmd files to launch Moonlight as well as grabbing boxarts from Moonlight for ES on Windows

![Screenshot](https://github.com/MeisterLi/ESwindowsMoonlightGameList/blob/main/Screenshot.png)

# Setup (on the client machine):

~~## Determine your Moonlight Server's UUID. 
In windows, you can find it in the registry at HKEY_CURRENT_USER\SOFTWARE\Moonlight Game Streaming Project\Moonlight\hosts\\{hostnumber}
open the included file and change the "UUID" field to the UUID you just found.~~ No longer needed. However if you want to use a different host than the first in the Moonlight Host list, change the "1" in "uuid_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\\Moonlight Game Streaming Project\\Moonlight\\hosts\\1", 0, winreg.KEY_READ)" to a different number corresponding to the host.

## Update some Configs
Edit the "emulationstation_location" if you don't use the regular EmulationStation install that uses %USERPROFILE%\\.emulationstation (i.E. you're using RetroBat)
Edit the "moonlight_rom_location" if you use a different roms folder (i.E. you're using RetroBat)

## Create the folder "moonlight" in your emulationstation/roms/ directory

## Add "Moonlight" to your es_systems.cfg. 
See "es_systems.cfg" for an example

# Excecute the Script with Python 3

Enjoy!

Note: You may have to Scrape and/or start the game after it's entry has been made in order for the boxart to be fetched. Emulationstation does not seem to add games to the gamelist.xml otherwise.
