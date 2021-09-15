#!/usr/bin env python

#---------------------------------------------------------------------------------
# reg.py
# Authors: Camila Vasquez & Tanzila Morshed
#---------------------------------------------------------------------------------

from sys import argv, stderr, exit
from contextlib import closing
from sqlite3 import connect
import argparse
#---------------------------------------------------------------------------------

DATABASE_URL = 'file: reg.sqlite?mode=ro'

def main():

    parser = argparse.ArgumentParser(description="Registrar application: show overviews of classes",  allow_abbrev=False)
    parser.add_argument("-d", metavar= "dept", dest = "d", help="show only those classes whose department contains dept", 
                        action="store", default=42)
    parser.add_argument("-n", metavar="num", dest = "n", help="show only those classes whose course number contains num", 
                        action="store", default=42)
    parser.add_argument("-a", metavar="area", dest = "a", help="show only those classes whose distrib area contains area", 
                        action="store", default=42)
    parser.add_argument("-t", metavar="title", dest = "t",  help="show only those classes whose course title contains title", 
                        action="store", default=42)
    args = parser.parse_args()

    try:
        with connect (DATABASE_URL, uri=True) as connection:
            with closing (connection.cursor()) as cursor:

                stmt_str = ""

                if args.d != None:
                    stmt_str += "SELECT crosslistings.dept " 
                    stmt_str += "FROM crosslistings "
                    stmt_str += "WHERE crosslistings.dept = ' " + args.d + "'"
            
                cursor.execute(stmt_str)

                row = cursor.fetchone()
                while row is not None:
                    print(row)

    except Exception as ex:
        print(ex, file=stderr)
        exit(1)
        












if __name__ == "__main__":
    main()
