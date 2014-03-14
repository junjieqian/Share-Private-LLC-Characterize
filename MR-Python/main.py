#!/usr/bin/env Python
#
# Junjie Qian

import string
import sys
import optparse
import os
#from pyro import mapping
#from pyro import reducing
#from pyto import partitioning
from pyro import mapreduce

POSSIBLE_SLAVES = osutil.get_all_cpus()

def helper(filepath, setnum):
	""" assign the mapreduce work
	"""
	print filepath
	print setnum
	if os.path.isfile(filepath):
		mapreduce(filepath, setnum)
	else:
		for root, dirs, files in os.walk(filepath):
			fnames = [os.path.join(root, f) for f in files]
			for f in fnames:
				mapreduce(f, setnum)

def main():
	""" starts from here
	"""
	parser = optparse.OptionParser(usage='Usage: %prog [options] [file path] [total set number]')
	parser.add_option('-r', '--reset', action='store_true', default=False, help='dry run')
	parser.add_option('-f', '--file', dest="filepath", type="string", help="specify files to process")
	parser.add_option('-s', '--set', dest="setnum", type="int", help="specify the total set number")
	options, args = parser.parse_args()
	if not options.filepath or not options.setnum:
		parser.print_help()
		sys.exit(1)
	filepath = options.filepath
	setnum = options.setnum
	helper(filepath, setnum)

if __name__ == '__main__':
	main()
