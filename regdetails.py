#!/usr/bin env python

#-----------------------------------------------------------------------
# regdetails.py
# Authors: Camila Vasquez & Tanzila Morshed
#-----------------------------------------------------------------------

from sys import stderr, exit
from contextlib import closing
from sqlite3 import connect
import argparse
import sys
import textwrap
#-----------------------------------------------------------------------
DATABASE_URL = 'file:reg.sqlite?mode=ro'

def main():
    # build an arg parser object, add args, and parse input
    parser = argparse.ArgumentParser(description="Registrar \
        application: show details about a class",  allow_abbrev=False)
    parser.add_argument("classid", type = int, help="the id of the \
        class whose details should be shown")
    args = parser.parse_args()

    try:
        with connect (DATABASE_URL, uri=True) as connection:
            with closing (connection.cursor()) as cursor:
                # build sql statement strings for cursor     
                if args.classid  != None:
                    class_stmt = "SELECT classes.courseid, days, \
                        starttime, endtime, bldg, roomnum FROM \
                        classes, courses WHERE (courses.courseid \
                        = classes.courseid) AND classid LIKE ?"

                    cross_stmt = "SELECT dept, coursenum FROM \
                        crosslistings, courses, classes WHERE \
                        (courses.courseid = crosslistings.courseid) \
                        AND (courses.courseid = classes.courseid) \
                        AND classid LIKE ? ORDER BY dept, \
                        coursenum ASC"

                    course_stmt = "SELECT area, title, descrip, \
                        prereqs FROM courses, classes \
                        WHERE (courses.courseid = classes.courseid) \
                        AND classid LIKE ?"

                    profs_stmt = "SELECT profname FROM profs, \
                        coursesprofs, classes WHERE \
                        (coursesprofs.courseid = classes.courseid) AND \
                        (profs.profid = coursesprofs.profid) AND \
                        classid LIKE ? ORDER BY profname ASC" 
                # run sql request with given argument
                cursor.execute(class_stmt,[args.classid])
                row = cursor.fetchone()

                # throw exception if no such class exists
                if row is None:
                    raise RuntimeError

                # print details
                print("Course Id:", row[0])
                print()
                print("Days:", row[1])
                print("Start time:", row[2])
                print("End time:", row[3])
                print("Building:", row[4])
                print("Room:", row[5])
                print()

                # run sql request for crosslistings and print 
                cursor.execute(cross_stmt,[args.classid])
                row = cursor.fetchone()
                while row is not None:
                    print("Dept and Number:", row[0],  row[1])
                    row = cursor.fetchone()

                # run sql statement for courses and print
                cursor.execute(course_stmt,[args.classid])
                row = cursor.fetchone()
                print()
                print("Area:", row[0])
                print()
                title = "Title: " + row[1]
                print(textwrap.fill(title, width = 72))
                print()
                descrip = "Description: " + row[2]
                print(textwrap.fill(descrip, width = 72))
                print()
                prereq = "Prerequisites: " + row[3]
                print(textwrap.fill(prereq, width = 72))
                print()

                # run sql request for professors and print
                cursor.execute(profs_stmt,[args.classid])
                row = cursor.fetchone()
                while row is not None:
                    print("Professor:", row[0])
                    row = cursor.fetchone()
    # catch errors
    except RuntimeError as ex:
        print(sys.argv[0] + ":", "no class with classid", 
            args.classid, "exists", file=stderr)
    except Exception as ex:
        print(ex, file=stderr)
        exit(1)


if __name__ == "__main__":
    main()
