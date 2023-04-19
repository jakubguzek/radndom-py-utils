#!/usr/bin/env python
import argparse
import random
import sys

CALENDAR = {
    "Rixiam": 41,
    "Mudún": 38,
    "Faerún": 39,
    "Sirdún": 40,
    "Drakadún": 39,
    "Panthram": 39,
    "Oorn": 40,
    "Avant'hin": 39
}

ERAS = [4132, 2201, 5984, 703]

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year", type=int, help="get random date with random year from N-th era")
    parser.add_argument("-b", "--batch", type=int, default=1, help="generate N random dates")
    return parser.parse_args()

def random_date(calendar: dict[str, int]):
    month = random.choice(list(calendar.keys()))
    return (month, random.randint(1,calendar[month]))

def main() -> int:
    args = parse_args()
    for _ in range(args.batch):
        year: str = ""
        month, day = random_date(CALENDAR)
        if args.year:
            year = str(random.randint(1, ERAS[args.year - 1]))
        print(f"{day} {month} {year}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
