import argparse

parser = argparse.ArgumentParser(description="Display photo in a terminal")

parser.add_argument("file", help="File to be displayed", type=str)
parser.add_argument("--cols", dest="cols", help="Column count", type=int)
parser.add_argument("--directory", dest="is_directory", help="Whether path is a directory", type=bool)
parser.add_argument("--save", dest="save", help="File to save to (if --directory is specified - directory), specifiing this will disable image rendering in terminal", type=str)
parser.add_argument("--start", dest="start", help="If in directory mode, specifies start index.", type=int)
parser.add_argument("--color", dest="color", help="If specified, the art will be printed in color", type=bool, default=False)

args = parser.parse_args()
