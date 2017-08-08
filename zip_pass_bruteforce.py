#!/usr/bin/env python
import sys
from zipfile import ZipFile

my_wordlist = sys.argv[1]
my_zip = sys.argv[2]

myzip = ZipFile(my_zip)

with open(my_wordlist) as file:
	print("Started.")
	for password in file:
		try:
			myzip.extractall(pwd=password.strip('\n'))
			print("Found! Password is {}".format(password))
		except:
			pass
	else:
		print("Done!")