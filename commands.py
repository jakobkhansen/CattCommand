import os
import re
import json

# Commands file

# Values, modified by settings.json
basecommand = "catt"
volume_increment = 10
rewind_amount = 15
seek_amount = 15
saved_volume = 100

# Loads settings into values from settings.json
def load_settings():
    global basecommand, volume_increment, rewind_amount, seek_amount
    filepath = os.path.dirname(__file__) + "/settings.json"
    config = json.load(open(filepath, "r"))

    basecommand = config["basecommand"]
    volume_increment = config["volume_increment"]
    rewind_amount = config["rewind_amount"]
    seek_amount = config["seek_amount"]

# Gets info from catt
def get_info():
    return exec_command("info")

# Prints info from catt
def print_info():
    print(get_info())

# Toggles play/pause
def play_toggle():
    exec_command("play_toggle")

# Turns volume down
def volumedown():
    command = "volumedown {}".format(volume_increment)
    exec_command(command)

# Turns volume up
def volumeup():
    command = "volumeup {}".format(volume_increment)
    exec_command(command)

# Rewinds the video
def rewind():
    command = "rewind {}".format(str(rewind_amount))
    exec_command(command)

# Gets current volume
def get_volume():
    info = get_info()
    return float(re.findall("^volume_level: (.*)", info, re.MULTILINE)[0])

# Toggles mute
def toggle_mute():
    global saved_volume
    volume_level = get_volume()

    if (volume_level > 0):
        saved_volume = volume_level
        exec_command("volume 0")

    else:
        new_volume = int(saved_volume*100) & 101
        exec_command("volume {}".format(new_volume))

# Gets current time
def get_time():
    info = get_info()
    return float(re.findall("^current_time: (.*)", info, re.MULTILINE)[0])

# Skips ahead
def skip():
    current_time = int(get_time())
    new_time = current_time + seek_amount
    command = "seek {}".format(new_time)
    exec_command(command)

# Stops catt
def stop_stream():
    exec_command("stop")

# Executes a command in shell
def exec_command(command):
    full_command = "{} {}".format(basecommand, command)
    return os.popen(full_command).read()

# List of commands with bindings.
command_list = {
    " ": [play_toggle, "Toggling play"],
    "i": [print_info, None],
    "m": [toggle_mute, "Toggling mute"],

    # Arrow keys
    68: [rewind, "Rewind"],
    65: [volumeup, "Volume up"],
    66: [volumedown, "Volume down"],
    67: [skip, "Skip"],
    "x": [stop_stream, "Goodbye"]
}
