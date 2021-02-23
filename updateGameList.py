import errno, os, winreg, xml.etree.ElementTree as ET

server_uuid = "176b5dd4-56f7-422e-ad14-6b31aef1343b"
launch_command = "\"c:\\Program Files\\Moonlight Game Streaming\\Moonlight.exe\" stream " + server_uuid + " \"{0}\""
emulationstation_location = os.environ['USERPROFILE'] + "\\.emulationstation\\"
moonlight_rom_location = emulationstation_location + "roms\\moonlight\\"
moonlight_gamelist = emulationstation_location + "\\gamelists\\moonlight\\gamelist.xml"
moonlight_boxart = os.environ['LOCALAPPDATA'] + "\\Moonlight Game Streaming Project\\Moonlight\\cache\\boxart\\" + server_uuid + "\\"

def updateMoonlightImages(game_name, game_id):
    tree = ET.parse(moonlight_gamelist)
    for game in tree.findall('game'):
        gametext = game.find('name').text
        if (gametext == game_name):
            print("text match found for " + game_name)
            image = game.find('image')
            if (image is None):
                print("no image tag found!")
                boxart = moonlight_boxart + str(game_id) + ".png"
                child = ET.Element('image')
                child.text=boxart
                game.append(child)
            else:
                print("updating image!")
                boxart = moonlight_boxart + str(game_id) + ".png"
                game.find("image").text = boxart
    tree.write(moonlight_gamelist)
    
def updateMoonlightConfig(game_name, game_id):
    f = open(moonlight_rom_location + game_name + ".cmd", "w")
    f.write(launch_command.format(game_name))
    f.close()
    updateMoonlightImages(game_name, game_id)

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\\Moonlight Game Streaming Project\\Moonlight\\hosts\\1\\apps", 0, winreg.KEY_READ)

# remove all old launch files from roms folder
filelist = [ f for f in os.listdir(moonlight_rom_location) if f.endswith(".cmd") ]
for f in filelist:
    os.remove(os.path.join(moonlight_rom_location, f))

# get game list from registry and create launch files
for i in range(0, winreg.QueryInfoKey(key)[0]):
    skey_name = winreg.EnumKey(key, i)
    skey = winreg.OpenKey(key, skey_name)
    try:
        updateMoonlightConfig(winreg.QueryValueEx(skey, 'name')[0], winreg.QueryValueEx(skey, 'id')[0])
        print(winreg.QueryValueEx(skey, 'name')[0] + str(winreg.QueryValueEx(skey, 'id')[0]))
    except OSError as e:
        if e.errno == errno.ENOENT:
            # DisplayName doesn't exist in this skey
            pass
    finally:
        skey.Close()
