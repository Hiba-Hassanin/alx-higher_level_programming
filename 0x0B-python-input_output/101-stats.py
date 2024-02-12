#!/usr/bin/python3


import sys


def print_stats(total_size, status_codes):
    """
    Prints the statistics.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary contain status counts.
    """

    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def parse_line(line):
    """
    Parses a line of input.

    Args:
        line (str): The line to parse.

    Returns:
        tuple: tuple containing the status and file size.
    """

    parts = line.split()
    return int(parts[-2]), int(parts[-1])

def main():
    """
    Main function to process input and compute statistics.
    """

    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0,
            401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            status_code, file_size = parse_line(line)
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()
