from rich.console import Console

from args import *
from .img import draw

image_formats = ["png", "jpeg", "jpg"]

console = Console()

def show(file):
    art = draw(file, args.cols if args.cols else 80, 0.43, args.color)
    for line in art:
        if args.color:
            for s in line:
                symb, style = s
                console.print(symb, style=style, end="")
        else:
            for s in line:
                symb, _ = s
                print(symb, end="")
        console.print("", end="\n")

def save_f(file, out):
    art = draw(file, args.cols if args.cols else 80, 0.43, args.color)
    with open(out, "w") as f:
        for line in art:
            a = ""
            for s in line:
                a += s[0]
            f.write(a + '\n')
