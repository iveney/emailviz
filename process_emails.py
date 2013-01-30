#!/usr/bin/env python
# encoding: utf-8
"""
process_emails.py

Created by Zigang Xiao on 2013-01-30.
"""

import sys
import os
import mailbox
import re

def main():
	if (len(sys.argv) < 2):
		print "Usage: ./process_emails.py <mbox>"
		exit(1)
	filename = sys.argv[1]
	mbox = mailbox.mbox(filename)

	# iterate all messages and extract information
	p = re.compile(r'(\b(?:\d{1,3}\.){3}\d{1,3}\b)\]\)')
	for msg in mbox:
		ip_str = msg['Received']
		m = p.search(ip_str)
		date_str = msg['Date']
		print m.group(1), date_str

if __name__ == '__main__':
	main()

