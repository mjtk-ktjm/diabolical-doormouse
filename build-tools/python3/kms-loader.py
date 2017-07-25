"""
Replace tokens with unencrypted KMS values using Jinja.
"""
import os, sys
from os.path import abspath, dirname, join, isfile
import argparse 
from jinja2 import Template

# print, copy, replace
# requires name of template to render to stdout
argv_len = len(sys.argv)
source_file = None
dest_file = None

# not going to matter once we are using argparse
#if sys.argv[1] not in ['print', 'copy', 'replace']:
#  user_function = sys.argv[1]
#else:
#  user_function = 'print'

user_function = sys.argv[1]

if argv_len not in [3,4] or user_function not in ['print', 'copy', 'replace']:
  # print help and exit(1)
  print("nope")
  sys.exit(1)

if sys.argv[1]=='copy':
  if argv_len!=4:
    print("A destination file path is required to copy a file with replacement.")
    sys.exit(1)

source_file = sys.argv[2]

if argv_len==4:
  print("copying?")
  dest_file = sys.argv[3]

ROOT_DIR = abspath(dirname(__file__))
template_file = os.path.join(ROOT_DIR, source_file)
template = Template(open(template_file).read())
rendered_file_contents = template.render(os.environ)

if user_function=='print':
  print(rendered_file_contents)
elif user_function=='replace':
  with open(source_file, "w") as template_out:
    template_out.write(rendered_file_contents)
elif user_function=='copy':
  with open(dest_file, "w") as template_out:
    template_out.write(rendered_file_contents)

