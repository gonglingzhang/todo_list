# -*-encoding:utf-8-*-
# run conversion.py and palette.py

import os, sys
input_file = sys.argv[1]
output_file = input_file.split(".")[0] + '.gif'


def run(input_file, output_file):
	os.system('python3 palette.py ' + input_file)
	os.system('python3 conversion.py ' + input_file + ' ' + output_file)
	

if __name__ == '__main__':
	run(input_file, output_file)
