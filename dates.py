# -*- coding: utf-8 -*-

"""
Tested with python3.4

This script serves for creating a list of dates in with some fixed interval.

Currently there is no command line interface. Just edit the source

Example output (interval=14): 

2017-01-05
2017-01-19
2017-02-02
2017-02-16
2017-03-02
...

"""

import datetime as dt
import sys

wrn_msg = """
Warning: Selecting the result of this script via mouse for copying
via clipboard you may accidentally select a lot of unwanted space
characters at the line endings. Better use

 python3 dates.py >> result.txt

and copy from that file.
"""


#start = dt.date(2017, 1, 5)

start = dt.date(2017, 1, 5)
end = dt.date.today()

interval = dt.timedelta(14)

reverse_flag = True

prefix="fsfw-dd-"
date_format = prefix + r"%Y%m%d"

def date_iterator():
    
    thedate = start
    while True:
        yield thedate
        
        thedate +=interval
        if thedate > end:
            raise StopIteration()


results = [d.strftime(date_format) for d in date_iterator()]

if reverse_flag:
    results.reverse()

print("\n".join(results))


print(wrn_msg, file=sys.stderr)
