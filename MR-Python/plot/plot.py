#!/usr/bin/env python
#
# Junjie Qian

import string
import sys
import os
import matplotlib.pyplot as plt

colorlist  = ['bo-', 'r^-', 'g*-', 'cD-']

def sumup(filename):
	fp = open(filename, 'r')
	result = {}
	for line in fp:
		word = line.split(':')
		distance = word[0]
		num = int(word[1], 0)
		if distance in result:
			result[distance] += num
		else:
			result[distance] = num
	fp.close()
	return result

def plot(result, i):
	distancelist = []
	countlist    = []
	for element in result:
		distancelist.append(element)
		countlist.append(result[element])

def main():
	try:
		script, filepath, appname = sys.argv()
	except:
		print "USAGE: %prog filepath appname"

	if os.path.isfile(filepath):
		sumup(filepath)
	else:
		for root, dirs, files in os.walk(filepath):
			f = [os.path.join(root, fl) for fl in files]
			f.sort(key=lambda x: x.split('.')[0])
			i = 0
			for filename in f:
				result = {}
				result = sumup(filename)
				plot(result, i)
				i += 1
