# serial 3
# ocr the captured screenshot.
# optical character recognition

from PIL import Image
import pytesseract



def extract_text(image_path, lang="eng+ben"):
    img = Image.open(image_path)
    config = '--oem 1 --psm 6'
    text = pytesseract.image_to_string(img, lang=lang, config=config)
    return text.strip()

if __name__ == "__main__":
    print("----------------- ocr.py ---------------------")
    print("testing ocr")
    # this part is not including the recently captured /tmp/something.png file,
    # because, this is for independent testing of this current file (ocr.py)
    # so make sure u are giving a filename which is an image with text
    # i am putting one in assets directory.
    print(extract_text("tests/assets/test_english.png"))
    print(extract_text("tests/assets/test_bangla.png"))
    print("----------------------------------------------")
