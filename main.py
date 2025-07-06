import os

from rich.console import Console
from args import args
from pynput import keyboard

from img import *

console = Console()

image_formats = ["png", "jpeg", "jpg"]

def show(file):
    art = draw(file, args.cols if args.cols else 80, 0.43)
    for line in art:
        for s in line:
            symb, style = s
            console.print(symb, style=style, end="")
        console.print("", end="\n")

def save_f(file, out):
    art = draw(file, args.cols if args.cols else 80, 0.43)
    with open(out, "w") as f:
        for line in art:
            a = ""
            for s in line:
                a += s[0]
            f.write(a + '\n')

def main():
    if not os.path.exists(args.file) and not args.file.startswith("http"):
        raise Exception("Path not found!")

    if args.is_directory:
        files = os.listdir(args.file)
        files = [x for x in files if x.split(".")[-1] in image_formats]

        start = args.start if args.start is not None else 0

        with keyboard.Events() as events:
            for i in range(start, len(files), 1):
                file = files[i]
                if args.save:
                    save_f(file, os.path.join(args.save, file + ".txt"))
                    continue

                show(file=os.path.abspath(os.path.join(args.file, file)))
                event = events.get(1e6)

                if event.key == keyboard.KeyCode.from_char('d'):
                    pass
                elif event.key == keyboard.KeyCode.from_char('s'):
                    break
    else:
        if args.save:
            save_f(args.file, os.path.join(args.save, args.file + ".txt"))
        else:
            show(args.file)

if __name__ == "__main__":
    main()
