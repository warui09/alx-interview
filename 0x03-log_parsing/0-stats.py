#!/usr/bin/python3
"""parse and print information from logs"""

import sys
import re
from typing import Optional


def print_info(total_size: int, status_codes: dict) -> None:
    """print the information"""
    print(f"Total file size: {total_size}")
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")


def get_info(line: str) -> Optional[dict]:
    """read input from stdin and parse it to extract relevant information"""

    pattern = re.compile(
        r"\s*(?P<ip>\S+)\s*-\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]\s*"
        r'"GET /projects/260 HTTP/1.1"\s*(?P<status_code>\d+)\s*(?P<file_size>\d+)\s*'
    )

    match = pattern.match(line)

    if match:
        # extract status code and file_size
        status_code = int(match.group("status_code"))
        file_size = int(match.group("file_size"))
        return {"status_code": status_code, "file_size": file_size}
    else:
        return None


def main() -> None:
    """run the code"""
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1
            info = get_info(line)
            if info:
                total_size += info["file_size"]
                status_code = info["status_code"]
                if status_code in status_codes:
                    status_codes[status_code] += 1

            if line_count % 10 == 0:
                print_info(total_size, status_codes)

    except (KeyboardInterrupt, EOFError):
        print_info(total_size, status_codes)


if __name__ == "__main__":
    main()
