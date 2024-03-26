#!/usr/bin/python3
""" read from stdin line by line and parse the input """

import fileinput
import signal

count = 0
codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
file_size = 0

for line in fileinput.input():
    # increment counter for every iteration
    count += 1

    # get status code from line and increase counter
    code = int(line.split()[-2])
    if code in codes:
        codes[code] += 1

    # get and update file_size
    file_size += int(line.split()[-1])

    # print filesize and status code count every 10 lines and/or sigint
    # implement sigint after all code is working fine
    if count % 10 == 0 or signal.SIGINT:
        print(f"File size: {file_size}")
        for code in codes:
            print(f"{code}: {codes[code]}")
