#!/usr/bin/python3
""" read from stdin line by line and parse the input """

import fileinput
import re
import signal

# define signal handler
def handler(signum, frame):
    """handle SIGINT signal"""
    print("\n^C")

# register signal handler
signal.signal(signal.SIGINT, handler)

def print_stats():
    """print stats"""

    count = 0
    codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    file_size = 0
    regex = r'\b(?:(?:2(?:[0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9])\.){3}(?:(?:2([0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9]))\b - \[\d{2}/[A-Za-z]+/\d{4} [0-9]+:[0-9]+:[0-9]+\] "[A-Za-z]+ /[A-Za-z]+/260 [A-Za-z]+/1\.1" [0-9]+ [0-9]+'

    try:
        for line in fileinput.input():
            # increment counter for every iteration
            count += 1

            if not re.match(regex, line):
                pass

            # get status code from line and increase counter
            code = int(line.split()[-2])
            if code in codes:
                codes[code] += 1

            # get and update file_size
            file_size += int(line.split()[-1])

            # print filesize and status code count every 10 lines and/or sigint
            if count % 10 == 0:
                print(f"File size: {file_size}")
                for code, count in codes.items():
                    print(f"{code}: {count}")
    except KeyboardInterrupt:
        print_stats()

print_stats()
