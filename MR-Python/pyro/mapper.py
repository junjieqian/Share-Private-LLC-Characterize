#!/usr/bin/env python
#
# Junjie Qian <jqian>

""" mapper function
"""

import string
import sys

def mapper(L, results):
	""" mapper function, calculate the inter-median accesses between two accesses to the same record
	Considering even two continuous accesses are to the same line, the remaining distance of LRU is still updated for other lines.
	@param L, the list of the memory addresses belong to one same set
	@param results, the map of the reuse distance distribution
	@param index, the line index of the addr record
	"""
#	results  = {}
	addrline = {}
	index = 0
	for addr in L:
		if addr in addrline:
			distance = index - addrline[addr]
			if distance in results:
				results[distance] += 1
			else:
				result[distance] = 1
		else:
			addrline[addr] = index
		index += 1
	del L[:]
	print "Done"
#	return results
