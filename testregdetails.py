#!/usr/bin env python

#---------------------------------------------------------------------------------
# testregdetails.py
# Authors: Camila Vasquez & Tanzila Morshed
#---------------------------------------------------------------------------------

from sys import argv, stderr, exit
import os
#from contextlib import closing
#from sqlite3 import connect
#import argparse, re, textwrap
#---------------------------------------------------------------------------------

def main():
    os.system('python3 ' + argv[1]+ ' 8321')
    os.system('python3 ' + argv[1]+ ' 9032')
    os.system('python3 ' + argv[1]+ ' 9977')
    os.system('python3 ' + argv[1]+ ' 9012')
    os.system('python3 ' + argv[1]+ ' 10188')

    os.system('python3 ' + argv[1])
    os.system('python3 ' + argv[1]+ ' 8321 9032')
    os.system('python3 ' + argv[1]+ ' abc123')
    os.system('python3 ' + argv[1]+ ' 9034')

if __name__ == "__main__":
    main()