Sway-spotlight allows a user to give screen width priority to a focused window.

Sway-spotlight is written in Python3 and requires the following:

i3ipc        : Communicate with Sway  
python-evdev : Keyboard input

Usage:  
1. Clone Sway-spotlight repository: git clone https://github.com/drmcbrayer89/sway-spotlight
2. Make Sway-spotlight accessible via PATH: cp ~/sway-spotlight/sway-spotlight.py /usr/local/bin/swayspotlight
3. Ensure it's executable: chmod +x /usr/local/bin/swayspotlight
4. Add to ~/.config/sway/config: "exec_always swayspotlight"

Hotkey is bound to Mod(Win) + Shift + F. Will add customization later if this gains some traction.

Enjoy!
