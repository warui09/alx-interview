#!/usr/bin/python3
"""get input from stdin and parse it one line at a time"""

import re
from typing import Optional

def get_data(line: str) -> Optional[dict]:
    """extract status and size information from log file line"""

    p = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )

    log_format = f"{p[0]}-{p[1]}{p[2]}{p[3]}{p[4]}\\s*"

    full_match = re.fullmatch(log_format, line)

    if full_match:
        status_code = int(full_match.group('status_code'))
        file_size = int(full_match.group('file_size'))
        return {"status_code": status_code, "file_size": file_size}

    return None

def update_codes(data: dict, codes: dict) -> None:
    """update the codes dict"""

    status_code = data["status_code"]
    file_size = data["file_size"]

    codes[status_code] += 1

    # update file_size
    codes["file_size"] += file_size

def print_line(count: int, file_size: int, codes: dict) -> None:
    """print a line"""

    if count % 10 == 0:
        print(f"File_size: {file_size}")
        for code in codes:
            if code != "file_size":
                print(f"{code}: {codes[code]}")

def main() -> None:
    """run the code"""

    count = 0
    codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0, "file_size": 0}

    while True:
        count += 1
        line = input()
        data = get_data(line)
        if data:
            update_codes(data, codes)
        try:
            print_line(count, codes["file_size"], codes)
        except (KeyboardInterrupt, EOFError):
            print_line(count, codes["file_size"], codes)
            break

if __name__ == "__main__":
    main()
