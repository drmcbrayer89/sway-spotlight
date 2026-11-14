#!/usr/bin/env python3
import time
import signal
import sys
import evdev
from evdev import ecodes, categorize, UInput 
import i3ipc

# trying to fix issue preventing "exec focus" from working as a config entry
sway = None

time.sleep(1)

sway = i3ipc.Connection(auto_reconnect=True)

# window_id : original width
width_states = {}

def toggle_focus():
    global sway, width_states
    
    # get tree & focused window from sway
    tree = sway.get_tree()
    focused = tree.find_focused()
    
    # safety check
    if not focused or focused.type != 'con':
        return

    window_id = focused.id

    # if the id has been seen before, restore; else resize to 67%
    if window_id in width_states:
        original_width = width_states.pop(window_id)
        sway.command(f'resize set width {original_width} px')
    else:
        width_states[window_id] = focused.rect.width
        print(f'id: {window_id} width(px): {width_states[window_id]}')
        sway.command(f'resize set width 67 ppt')


def find_keyboard():
    while True:
        devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
        for device in devices:
            keys = device.capabilities().get(ecodes.EV_KEY, [])
            if ecodes.KEY_A in keys and ecodes.KEY_ENTER in keys:
                if "keyboard" in device.name.lower():
                    return device
        time.sleep(1)

dev = find_keyboard()

# This is straight from gemini, not gonna lie
uinput = UInput.from_device(dev, name="hotkey-monitor")

time.sleep(0.5)

# grab keyboard to prevent keypress from going into window
dev.grab()

# End gemini lmfao

# set() stores only unique items! this is nifty.
active_keys = set()

# handle keyboard input
for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        key = categorize(event)

        if key.keystate == key.key_down:
            active_keys.add(key.scancode)
        elif key.keystate == key.key_up:
            active_keys.discard(key.scancode)
        
        if (ecodes.KEY_LEFTMETA in active_keys and 
            ecodes.KEY_LEFTSHIFT in active_keys and
            ecodes.KEY_F in active_keys and
            key.keystate == key.key_down
        ):
            toggle_focus()
            continue
        
        uinput.write_event(event)
        uinput.syn()







