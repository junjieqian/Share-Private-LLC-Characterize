# !/usr/bin/env Python
#
# Junjie Qian, <jqian>

""" Main function for mapreduce work
"""

import string

class mapreduce:
	def __init__(self, filename, setnum, cores=None):
		self.filename = filename
		self.setnum   = setnum
		self.cores    = cores

	def getrecords(filename, setnum):
		fp = open(filename, 'r')
		for line in fp:
			try:
				word = line.split()
				tid  = int(word[0], 0)
				inst = int(word[1], 0)
				addr = int(word[2], 0)
			except:
				continue
			setid = addr%setnum
