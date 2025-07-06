import os
import io
import requests

from PIL import Image

from .avg import *

gscale = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

def draw(imgn: str, cols, scale):
    img = Image.open(io.BytesIO(requests.get(imgn).content) if imgn.startswith("http") else imgn)

    W, H = img.size

    w = W/cols
    h = w/scale

    rows = int(H/h)

    if cols > W or rows > H:
        raise Exception("Image is too small!")

    asc = []

    for j in range(rows):
        y1 = j*h
        y2 = (j+1)*h

        if j == rows-1:
            y2 = H

        asc.append([])

        for i in range(cols):
            x1 = i*w
            x2 = (i+1)*w

            if i == cols-1:
                x2 = W

            cimg = img.crop((x1, y1, x2, y2))
            brightness = get_average_brightness(cimg)

            asc[j].append((gscale[int((brightness*len(gscale)-1)/255)], get_average_color(cimg)))

    return asc
