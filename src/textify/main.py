# Main order : 5
# Do everything here.

import os
from . import screenshot, ocr, editor

def main():
    print("Select an Area..")
    image_path = screenshot.capture_area()

    if not image_path:
        print("No area selected.")
        return

    try:
        print("Running OCR...")
        text = ocr.extract_text(image_path)

        print("Opening editor ..")
        editor.open_editor(text)

    finally:
        if os.path.exists(image_path):
            os.remove(image_path)
            print(f"Deleted the tmp screenshot : {image_path}")

if __name__ == "__main__":
    main()
