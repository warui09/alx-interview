#!/usr/bin/python3
"""read input and parse line by line"""

import sys


def print_line(codes: dict, file_size: int) -> None:
    """print status code and value"""

    print(f"File size: {file_size}")
    for key, value in sorted(codes.items()):
        if value != 0:
            print(f"{key}: {value}")


def main() -> None:
    """run the code"""

    count = 0
    codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    file_size = 0

    try:
        for line in sys.stdin:
            count += 1
            parsed_line = line.split()
            status_code = int(parsed_line[-2]) if parsed_line[-2].isdigit() else None
            file_size = int(parsed_line[-1]) if parsed_line[-1].isdigit() else None

            # update codes dict
            if status_code in codes.keys():
                codes[status_code] += 1

            if count % 10 == 0:
                print_line(codes, file_size)
    finally:
        print_line(codes, file_size)


if __name__ == "__main__":
    main()
