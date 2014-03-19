#!/usr/bin/env Python
#
# Junjie Qian <jqian>

""" reducer function
"""

import string

def reducer(L):
	""" reducer, collect all the results from all sets
	@param distribution, the final reuse distance distribution
	"""
	distribution = {}
	for item in L:
		for record in item:
			if record in distribution:
				distribution[record] += item[record]
			else:
				distribution[record] = item[record]
		item.clear()
	return distribution
