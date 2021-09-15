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

DATABASE_URL = 'file:reg.sqlite?mode=ro'

def main():

    parser = argparse.ArgumentParser(description="Registrar application: show overviews of classes",  allow_abbrev=False)
    parser.add_argument("-d", metavar= "dept", dest = "d", nargs= 1, help="show only those classes whose department contains dept", 
                        action="store")
    parser.add_argument("-n", metavar="num", dest = "n", nargs= 1, help="show only those classes whose course number contains num", 
                        action="store")
    parser.add_argument("-a", metavar="area", dest = "a", nargs= 1, help="show only those classes whose distrib area contains area", 
                        action="store")
    parser.add_argument("-t", metavar="title", dest = "t", nargs= 1, help="show only those classes whose course title contains title", 
                        action="store")
    args = parser.parse_args()


    try:
        with connect (DATABASE_URL, uri=True) as connection:
            with closing (connection.cursor()) as cursor:

                stmt_str = "SELECT classid, dept, coursenum, area, title FROM classes, crosslistings, courses WHERE courses.courseid = classes.courseid "
                stmt_str += "AND classes.courseid = crosslistings.courseid "

                if args.d != None:
                    stmt_str += "AND dept LIKE '%" + str(args.d[0]) + "%'"

                if args.n != None:
                    stmt_str += "AND coursenum LIKE '%" + str(args.n[0]) + "%'"

                if args.a != None:
                    stmt_str += "AND area LIKE '%" + str(args.a[0]) + "%'"

                if args.t != None:
                    stmt_str += "AND title LIKE '%" + str(args.t[0]) + "%'"

                cursor.execute(stmt_str)

                row = cursor.fetchone()

                while row is not None:
                    print('classid: ', row[0])
                    print('dept: ', row[1])
                    print('coursenum: ', row[2])
                    print('area: ', row[3])
                    print('title: ', row[4])
                    print()
                    row = cursor.fetchone()
                    

    except Exception as ex:
        print(ex, file=stderr)
        exit(1)
            




if __name__ == "__main__":
    main()
