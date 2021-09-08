from PIL import Image
import numpy as np
import difflib


def transform_to_str(img):
    image = Image.open(img)
    arr = str(np.asarray(image, dtype="uint8"))
    print(arr)
    return arr



def deff(s1, s2):
    normalized1 = s1.lower()
    normalized2 = s2.lower()
    matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
    return (round(matcher.ratio(), 3)*100)
print('Photo 1 and 2 are', deff(transform_to_str('ADD PHOTO!!!'),transform_to_str('ADD PHOTO')), '% similar.')