# !/usr/bin/env Python
#
# Junjie Qian, <jqian>

""" Main function for mapreduce work
"""

import string
import sys
from threading import Thread
import Queue
from multiprocessing import Pool

"""
"""

import threading
lock = threading.Lock()

fshared = open("shared.result", 'w')
fprivate = open("privated.result", 'w')

def mapper(L, shared):
	addrline = {} # key is addr, value is index
	sharedistance = {}
	privatedistance = {}
	index = 0 
	print len(L)
	for addr in L:
		index += 1
		if addr in addrline:
			distance = index - addrline[addr]
			if addr in shared:
				if distance in sharedistance:
					sharedistance[distance] += 1
				else:
					sharedistance[distance] = 1
			else:
				if distance in privatedistance:
					privatedistance[distance] += 1
				else:
					privatedistance[distance] = 1
		addrline[addr] = index
	L = []
	addrline.clear()
#	del L[:]
	with lock:
		print "acquire lock"
		for element in sharedistance:
			fshared.write(str(element) + ":" + str(sharedistance[element]) + '\n')
		for element in privatedistance:
			fprivate.write(str(element) + ":" + str(privatedistance[element]) + '\n')

def mapreduce (filename, setnum = 8192, cores = 20):
	""" mapreduce function, need to first pass to identify addr types, second to pass each addr to one set
	split the file into pieces according to sets
	@param shared/private, the dict to identify shared or private ones
	@param 
	"""
	fp = open(filename, 'r')
	shared   = {}
	privated = {}
	addrlist = []
	for i in range(8192):
		addrlist.append([])
	for line in fp:
		try:
			word = line.split("   ")
			tid  = int(word[0], 0)
			inst = int(word[1], 0)
			addr = int(word[2], 0)
		except:
			continue
		if addr in shared:
			shared[addr] += 1 # to record the shareness
		elif addr in privated:
			if not tid == privated[addr]:
				del privated[addr]
				shared[addr] = 2
		else:
			privated[addr] = tid
		if addr == addrlist[-1]:
			continue
		else:
			setid = addr%setnum
			addrlist[setid].append(addr)
	privated.clear()  # memory free. most accesses are private
	fp.close()

	''' following is test
	'''
	for element in shared:
		print element
	''' test ends '''

	results = []
	for i in range(8192):
		results.append({})
#	i = 0
#	pool = Pool()
#	for element in addrlist:
#		 threading.start_new_thread(mapper, (element, results[i]))
#		 element = []
#		 i + =1
#	work_queue = Queue()
#	for element in addrlist:
#		work_queue.put(element)
##	threads = [Thread(target=mapper, args=(addrlist[i], results[i])) for i in range(8192)]
	threads = []
	for i in range(8192):
		threads.append(Thread(target=mapper, args=(addrlist[i], shared)))
	for t in threads:
		t.start()
	for t in threads:
		t.join()
	del addrlist[:]
	"""
	fshared = open("shared.result", 'w')
	fprivate = open("privated.result", 'w')
	finalresult = {}
	for i in range(len(results)):
		for item in results[i]:
			if item > 256:
				item = 256
			if item in finalresult:
				finalresult[item] += results[i][item]
			else:
				finalresult[item] = results[i][item]
	del results[:]
	for item in finalresult:
		if item in shared:
			fshared.write(str(item) + " " + str(finalresult[item]) + '\n')
		else:
			fprivate.write(str(item) + " " + str(finalresult[item]) + '\n')
	fshared.close()
	fprivate.close()
	"""

def main():
	try:
		script, filename = sys.argv
	except:
		sys.exit("filename needed")
	
	mapreduce(filename)
	
if __name__ == "__main__":
	main()
