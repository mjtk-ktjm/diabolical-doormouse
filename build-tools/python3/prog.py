import argparse

parser = argparse.ArgumentParser(description='Replace tokens with ENV constants.')
parser.add_argument('function', metavar='func', type=str, nargs=1,
                    help='The function to perform on the tempalte. [print, copy, replace]')
parser.add_argument('template', metavar='file', type=str, nargs=1,
                    help='The file to perform the substitutions against.')
parser.add_argument('location', metavar='file', type=str, default=None, 
                    help='The directory or filename to output the replaced text file.')

args = parser.parse_args()
print(args)
