# To capture user selected area : [grim,slurp in wayland] or [maim,slop in x11] 
# Main Flow : 2

import subprocess
import tempfile
from .utils import is_wayland, is_x11

def capture_area():
    temp_file = tempfile.NamedTemporaryFile(suffix=".png",delete=False)
    temp_file.close()

    try:
        if is_wayland():
            area = subprocess.check_output(["slurp"]).decode().strip()
            subprocess.run(["grim", "-g", area, temp_file.name])
        elif is_x11():
            area = subprocess.check_output(["slop"]).decode().strip()
            subprocess.run(["maim", "-g", area, temp_file.name])
        else:
            raise RuntimeError("Unsupported session type")

    except subprocess.CalledProcessError:
        print("Selection cancelled")
        return None


    return temp_file.name

if __name__ == "__main__":
    print("--------------- screenshot.py ----------------")
    print("Screen capture testing.. Select an area.")
    print("Saved to :", capture_area())
    print("----------------------------------------------")
