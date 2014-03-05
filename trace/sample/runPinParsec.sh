#!/bin/bash

if [[ `hostname -s` = node2 ]]; then
	:
else
	echo "Need to run on Node2 of ADSL Cluster"
	exit
fi

CurrentDir=`dirname $0`

pin=/opt/pin/pin
pintool=/opt/pin/source/tools/ManualExamples/obj-intel64/threadtrace.so
parsecmgmt=/opt/benchmarks/parsec-3.0/bin/parsecmgmt

# change this to run different core number, or put it into one loop
core=8

# input set: native->Huge input for performance analysis on real machines
# do not change this, unless you know what you are doing
input=native

#parsec="parsecmgmt -a run -p"

# use go through the benchmark list here, because failed to build 'vips' benchmark*
for benchmark in canneal dedup ferret fluidanimate freqmine raytrace streamcluster splash2.ocean_cp splash2_fft; do
	if [ ! -d $CurrentDir/$benchmark ]; then
		mkdir -p $CurrentDir/$benchmark
	fi
	$parsecmgmt -a run -p $benchmark -n $core -i $input
	cd $CurrentDir/$benchmark # CurrentDir is changing
#	$pin -t $pintool -- $parsecmgmt -a run -p $benchmark -n $core -i $input
  echo "======================Done with $benchmark==============="
done

unset CurrentDir
