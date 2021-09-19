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
os.system('python reg.py -d COS')
os.system('python reg.py -n 333')
os.system('python reg.py -n b')
os.system('python reg.py -a Qr')
os.system('python reg.py -t intro')
os.system('python reg.py -t science')
os.system('python reg.py -t C_S')
os.system('python reg.py -t c%s')
os.system('python reg.py -d cos -n 3')
os.system('python reg.py -d cos -a qr -n 2 -t intro')
os.system('python reg.py -t "Independent Study"')
os.system('python reg.py -t " Independent Study"')
os.system('python reg.py -t "Independent Study "')
os.system('python reg.py -t "Independent Study  "')
os.system('python reg.py -t "  Independent Study"')
os.system('python reg.py -t=-c')

