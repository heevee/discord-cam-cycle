# discord-cam-cycle
An interactive way to let users switch between your webcam scenes while using OBS Virtual Cam
## Getting started
### Steps:
#### 1: Follow [this link](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/) and create a Discord bot
#### 2: Follow [this link](https://obsproject.com/) and download + install OBS Studio
#### 3: Follow [this link](https://www.autohotkey.com/) and install AutoHotKey, remember the installation path since you will need it for later.
#### 4: Follow [this link](https://obsproject.com/forum/resources/obs-virtualcam.539/) and download + install OBS VirtualCam
#### 5: Setup your scenes with the content of your choosing. Use [this](https://obsproject.com/wiki/Sources-Guide) as guide if you're confused
#### 6: Setup [this](https://github.com/SimonGZ/OBS-next-scene-hotkey) script, **remember to add a hotkey of your choosing in the hotkeys section of OBS, I chose shift+F1 as hotkey since it doesn't mess up anything when pressed. If you choose a different hotkey you have to alter the code in `bot.py`**
#### 7: Add your token (for the Discord bot) and AutoHotKey path (for example: C:\\\Program Files\\\AutoHotkey\\\AutoHotkey.exe) in a file called ".env" in the root folder of your project. Like this:
```
TOKEN=your_discord_token
AHK=your_autohotkey_path
```
#### 8: Clone this project and install the requirements (`pip install -r requirements.txt`)
#### 9: Just run `bot.py` and choose OBS Virtual Cam as your webcam source on Discord, remember to start the Virtual Cam in OBS
#### 10: As soon as someone types `!switch` in the Discord chat it will change the webcam view
