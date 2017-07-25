#!/usr/local/bin/python3
import argparse
import os, jinja2

parser = argparse.ArgumentParser(prog='sub_vars.py', \
                                 description='Substitue ENV vars into tokenized file.')

group = parser.add_mutually_exclusive_group()
group.add_argument('-p', '--print', action='store_const', const='p', dest='func', \
                  help='Print the untokenized file text and exit.')
group.add_argument('-c', '--copy', action='store_const', const='c', dest='func', \
                  help='Untokenize the file and save it in -d DESTINATION')
group.add_argument('-r', '--replace', action='store_const', const='r', dest='func', \
                  help='Replace the tokenized text file with the untokenized version.')

parser.set_defaults(func='p')

args = parser.parse_args()

print(args)

