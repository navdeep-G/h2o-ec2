#!/usr/bin/env python

import os
import sys
import time
import boto
import boto.ec2

regionName = 'us-east-1'
amiId = 'ami-0b100e61'
debug = 0
ec2 = boto.ec2.connect_to_region(regionName, debug=debug)

#Start up Instances:
txt = open("nodes-public",'r')
lines = txt.read().split('\n')
for line in lines:
	print line
reservations = ec2.get_all_instances()
for r in reservations: 
	for i in r.instances:
		print i
#instance[0].instances[0].start()