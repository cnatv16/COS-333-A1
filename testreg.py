#!/usr/bin env python

#---------------------------------------------------------------------------------
# testreg.py
# Authors: Camila Vasquez & Tanzila Morshed
#---------------------------------------------------------------------------------

from sys import argv, stderr, exit
import os 
# from contextlib import closing
# from sqlite3 import connect
# import argparse, textwrap
#---------------------------------------------------------------------------------
def main():
    os.system('python '+ argv [1] + ' -d COS')
    os.system('python '+ argv [1] + ' -n 333')
    os.system('python '+ argv [1] + ' -n b')
    os.system('python '+ argv [1] + ' -a Qr')
    os.system('python '+ argv [1] + ' -t intro')
    os.system('python '+ argv [1] + ' -t science')
    os.system('python '+ argv [1] + ' -t C_S')
    os.system('python '+ argv [1] + '  -d cos -n 3')
    os.system('python '+ argv [1] + ' -d cos -a qr -n 2 -t intro')
    os.system('python '+ argv [1] + ' -t "Independent Study"')
    os.system('python '+ argv [1] + ' -t " Independent Study"')
    os.system('python '+ argv [1] + ' -t "Independent Study "')
    os.system('python '+ argv [1] + ' -t "Independent Study  "')
    os.system('python '+ argv [1] + ' -t "  Independent Study"')
    os.system('python '+ argv [1] + ' -t=-c')

if __name__ == "__main__":
    main()