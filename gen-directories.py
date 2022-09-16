import argparse
import os
parser = argparse.ArgumentParser(description='Generate directories from list')
parser.add_argument('-i', '--input-file', type=str, help="File path of the list directories", required=True)

args = parser.parse_args()

input_file = args.input_file

infile = open(input_file, 'r')

lines = infile.readlines()

for line in lines:
  directory = line.replace(' ' , '-').lower().strip()
  os.mkdir(directory)
