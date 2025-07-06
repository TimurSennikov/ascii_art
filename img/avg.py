import numpy as np
from PIL import Image

def get_average_color(img: Image):
    a = np.mean(img, axis=(0, 1))
    if isinstance(a, np.float64):
        a = [255, 255, 255]

    return f"rgb({int(a[0])},{int(a[1])},{int(a[2])})"

def get_average_brightness(imgo: Image):
    img = imgo.convert('L')

    w, h = img.size 
    avg = 0
    for i in range(w):
        for j in range(h):
            avg += img.getpixel((i, j)) 
    avg /= w*h
    return avg
