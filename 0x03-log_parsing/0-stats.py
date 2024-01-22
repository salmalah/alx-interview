#!/usr/bin/python3
import sys

def print_statistics(total_size, codes_status):
    print("File size: {}".format(total_size))
    for c in sorted(codes_status.keys()):
        if codes_status[c] > 0:
            print("{}: {}".format(c, codes_status[c]))

def process_line(line, total_size, codes_status):
    try:
        parts = line.split()
        if len(parts) == 9:
            code_status = int(parts[7])
            file_s = int(parts[8])
            total_size += file_s

            if code_status in {200, 301, 400, 401, 403, 404, 405, 500}:
                if code_status not in codes_status:
                    codes_status[code_status] = 0
                codes_status[code_status] += 1

        return total_size, codes_status
    except ValueError:
        return total_size, codes_status

def main():
    total_size = 0
    codes_status = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            total_size, codes_status = process_line(line.strip(), total_size, codes_status)

            if i % 10 == 0:
                print_statistics(total_size, codes_status)
    except KeyboardInterrupt:
        pass

    print_statistics(total_size, codes_status)

if __name__ == "__main__":
    main()
