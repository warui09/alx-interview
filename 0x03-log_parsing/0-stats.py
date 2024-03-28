#!/usr/bin/python3
""" read from stdin line by line and parse the input """

import fileinput
import re
import signal
import sys


# define signal handler
def handler(signum, frame):
    """handle SIGINT signal"""
    print("\n^C")


# register signal handler
signal.signal(signal.SIGINT, handler)


def print_stats():
    """print stats"""

    count = 0
    total_size = 0
    codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    regex = r'\b(?:(?:2(?:[0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9])\.){3}(?:(?:2([0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9]))\b - \[\d{2}/[A-Za-z]+/\d{4} [0-9]+:[0-9]+:[0-9]+\] "GET /projects/260 HTTP/1.1" [0-9]+ [0-9]+'

    try:
        for line in fileinput.input():
            # increment counter for every iteration
            count += 1

            if not re.match(regex, line):
                pass

            # get status code and file size from line and update counters
            try:
                code = int(line.split()[-2])
                if code in codes:
                    codes[code] += 1
            except ValueError:
                pass

            try:
                file_size = int(line.split()[-1])
                total_size += file_size
            except ValueError:
                pass

            # print stats every 10 lines and/or SIGINT
            if count % 10 == 0:
                print(f"Total file size: {total_size}")
                for code, count in sorted(codes.items()):
                    if count > 0:
                        print(f"{code}: {count}")

    except KeyboardInterrupt:
        print_stats()


try:
    print_stats()
except KeyboardInterrupt:
    pass
