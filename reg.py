#!/usr/bin env python

#-----------------------------------------------------------------------
# reg.py
# Authors: Camila Vasquez & Tanzila Morshed
#-----------------------------------------------------------------------

from sys import stderr, exit
from contextlib import closing
from sqlite3 import connect
import argparse
import textwrap
#-----------------------------------------------------------------------

DATABASE_URL = 'file:reg.sqlite?mode=ro'

def main():
    # using argseparse to manage the potential arugemnts for this 
    # program, explaining each argument's function
    parser = argparse.ArgumentParser(description="Registrar \
        application: show overviews of classes",  allow_abbrev=False)
    parser.add_argument("-d", metavar= "dept", dest = "d", help="show \
        only those classes whose department contains dept", \
        action="store")
    parser.add_argument("-n", metavar="num", dest = "n", help="show \
        only those classes whose course number contains num", \
        action="store")
    parser.add_argument("-a", metavar="area", dest = "a", help="show \
        only those classes whose distrib area contains area", 
        action="store")
    parser.add_argument("-t", metavar="title", dest = "t", help="show \
        only those classes whose course title contains title",
        action="store")
    args = parser.parse_args()


    try:
         # connecting to the database, if fails closes and throws 
         # exception
        with connect (DATABASE_URL, uri=True) as connection:
            with closing (connection.cursor()) as cursor:
                
                # populating the statement to pass into the cursor 
                # and search through the database
                stmt_str = "SELECT classid, dept, coursenum, area, \
                    title FROM classes, crosslistings, courses \
                        WHERE (courses.courseid = classes.courseid) "
                stmt_str += "AND (classes.courseid = \
                    crosslistings.courseid) " 
                stmt_str += r"AND (dept LIKE ? ESCAPE '\') "
                stmt_str += r"AND (coursenum LIKE ? ESCAPE '\') " 
                stmt_str += r"AND (area LIKE ? ESCAPE '\') " 
                stmt_str += r"AND (title LIKE ? ESCAPE '\')"
                stmt_str += "ORDER BY dept, coursenum, classid ASC"

                dept= "%%"
                num = "%%"
                area = "%%"
                title = "%%"

                # initialize variables, dept, num, area, and title 
                # based on given arguments accounting for escape 
                # characters potentially passed in through arguments 
                if args.d is not None:
                    if '%' in str(args.d):
                        dept = "%" + args.d.replace("%", r"\%") + "%"
                    elif '_' in str(args.d):
                        dept = "%" + args.d.replace("_", r"\_") + "%"

                    else:
                        dept = '%' + str(args.d) + '%'

                if args.n is not None:
                    num = '%' + str(args.n) + '%'

                if args.a is not None:
                    if '%' in str(args.a):
                        area = "%" + args.a.replace("%", r"\%") + "%"
                    elif '_' in str(args.d):
                        area = "%" + args.a.replace("_", r"\_") + "%"
                    else:
                        area = '%' + str(args.a) + '%'

                if args.t is not None:
                    if '%' in str(args.t):
                        title = "%" + args.t.replace("%", r"\%") + "%"
                    elif '_' in str(args.t):
                        title = "%" + args.t.replace("_", r"\_") + "%"
                    else:
                        title = '%' + str(args.t) + '%'
                   
                # cursor executes the prepared statement to search 
                # through the database
                cursor.execute(stmt_str, [dept, num, area, title])

                # first row from database
                row = cursor.fetchone()

                # printing to output using requested formatting
                print("ClsId Dept CrsNum Area Title")
                print("----- ---- ------ ---- -----")

                # traverse through all the rows returned from the 
                # cursor execution
                while row is not None:
                    # using textwrap to populate text in requested 
                    # format
                    text = ""
                    text += textwrap.fill(str(row[0]), 
                        initial_indent = ' ' * (5-len(str(row[0]))))
                    text += textwrap.fill(str(row[1]), 
                        initial_indent = ' ' * (5-len(str(row[1]))))
                    text += textwrap.fill(str(row[2]), 
                        initial_indent = ' ' * (7-len(str(row[2]))))
                    text += textwrap.fill(str(row[3]), 
                        initial_indent = ' ' * (5-len(str(row[3]))))
                    if row[3] != "":
                        text += textwrap.fill(str(row[4]), 
                            initial_indent = ' ')
                    else:
                        text += textwrap.fill(str(row[4]), 
                            initial_indent = ' ' * 6)
                    print(textwrap.fill(text, 
                        subsequent_indent= ' ' * 23, width = 72))
                    # fetch the next row we want from the database
                    row = cursor.fetchone()

    # catch an exceptions raised in the program
    except Exception as ex:
        print(ex, file=stderr)
        exit(1)
            

if __name__ == "__main__":
    main()
