
Sway-spotlight allows a user to give screen width priority to a focused window.

Sway-spotlight is written in Python3 and requires the following:

i3ipc        : Communicate with Sway  
python-evdev : Keyboard input

Usage:  
1. Clone Sway-spotlight repository: git clone https://github.com/drmcbrayer89/sway-spotlight
2. Make Sway-spotlight accessible via PATH: cp ~/sway-spotlight/sway-spotlight.py /usr/local/bin/swayspotlight
3. Ensure it's executable: chmod +x /usr/local/bin/swayspotlight
4. Add to ~/.config/sway/config: "exec_always swayspotlight"

Bindings:
- Mod(Win) + Shift + F : Increase width on focused window 
- Mod(Win) + Shift + R : Reset workspace to default widths

Enjoy!

<img width="3440" height="1440" alt="20261114_02h57m54s_grim" src="https://github.com/user-attachments/assets/b3dbc037-e5b1-4fa0-a286-d65cdaf1bbdd" />
