# To detect session type ? wayland or x11
# Main flow : 2

import os

def is_wayland():
    return os.environ.get("XDG_SESSION_TYPE", "").lower() == "wayland"

def is_x11():
    return os.environ.get("XDG_SESSION_TYPE", "").lower() == "x11"

if __name__ == "__main__":
    print("----------------- utils.py -------------------")
    print("Is this wayland?", is_wayland())
    print("Is this X11?", is_x11())
    print("----------------------------------------------")
