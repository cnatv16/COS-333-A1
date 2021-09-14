#!/usr/bin env python

#---------------------------------------------------------------------------------
# reg.py
# Authors: Camila Vasquez & Tanzila Morshed
#---------------------------------------------------------------------------------

from sys import argv, stderr, exit
from contextlib import closing
from sqlite3 import connect

#---------------------------------------------------------------------------------

DATABASE_URL = 'file: reg.sqlite?mode=ro'

def main():

    #if len(argv) == 0:
     #   print('Usage: python reg.py', file=stderr)
     #   exit(1)

    if argv[1] == '-h':
        print('usage: reg.py [-h] [-d dept] [-n num] [-a area] [-t title] \n')
        print('Registrar application: show overviews of classes \n') 
        exit(0)

# args parse somewhere 
# try:with connect (DATABASE_URL, uri = True) as connection:

          