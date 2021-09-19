#!/usr/bin env python

#---------------------------------------------------------------------------------
# reg.py
# Authors: Camila Vasquez & Tanzila Morshed
#---------------------------------------------------------------------------------

from sys import argv, stderr, exit
from contextlib import closing
from sqlite3 import connect
import argparse, re, textwrap
#---------------------------------------------------------------------------------

DATABASE_URL = 'file:reg.sqlite?mode=ro'

def main():
    
    parser = argparse.ArgumentParser(description="Registrar application: show overviews of classes",  allow_abbrev=False)
    parser.add_argument("-d", metavar= "dept", dest = "d", help="show only those classes whose department contains dept", 
                        action="store")
    parser.add_argument("-n", metavar="num", dest = "n", help="show only those classes whose course number contains num", 
                        action="store")
    parser.add_argument("-a", metavar="area", dest = "a", help="show only those classes whose distrib area contains area", 
                        action="store")
    parser.add_argument("-t", metavar="title", dest = "t", help="show only those classes whose course title contains title", 
                        action="store")
    args = parser.parse_args()


    try:
        with connect (DATABASE_URL, uri=True) as connection:
            with closing (connection.cursor()) as cursor:

                stmt_str = "SELECT classid, dept, coursenum, area, title FROM classes, crosslistings, courses WHERE (courses.courseid = classes.courseid) "
                stmt_str += "AND (classes.courseid = crosslistings.courseid) " 
                stmt_str += r"AND (dept LIKE ? ESCAPE '\') "
                stmt_str += r"AND (coursenum LIKE ? ESCAPE '\') " 
                stmt_str += r"AND (area LIKE ? ESCAPE '\') " 
                stmt_str += r"AND (title LIKE ? ESCAPE '\')"

                dept= "%%"
                num = "%%"
                area = "%%"
                title = "%%"

                if args.d != None:
                    if '%' in str(args.d):
                        dep = args.d.replace("%", r"\%")
                        dept = "%" + dep + "%"
                    elif '_' in str(args.d):
                        dep = args.d.replace("_", r"\_")
                        dept = "%" + dep + "%"

                    else:
                        dept = '%' + str(args.d) + '%'

                if args.n != None:
                    num = '%' + str(args.n) + '%'
 

                if args.a != None:
                    if '%' in str(args.a):
                        ar = args.a.replace("%", r"\%")
                        area = "%" + ar + "%"
                    elif '_' in str(args.d):
                        ar = args.a.replace("_", r"\_")
                        area = "%" + ar + "%"
                    else:
                        area = '%' + str(args.a) + '%'
                    # escape character ifs
        #replace for underscore as well
        # do replace for other queries as well
        # hardcode sql statement, set each var initially to "%%", change in if statements

                if args.t != None:
                    if '%' in str(args.t):
                        tit = args.t.replace("%", r"\%")
                        title = "%" + tit + "%"
                    elif '_' in str(args.t):
                        tit = args.t.replace("_", r"\_")
                        title = "%" + tit + "%"
                    else:
                        title = '%' + str(args.t) + '%'
                    print(stmt_str)
                
                print(title)

                cursor.execute(stmt_str, [dept, num, area, title])

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
