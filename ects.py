#!/usr/bin/env python

import argparse
import pathlib
import sys

import pandas


# Keep script name in global constant (for error messages).
SCRIPT_NAME = pathlib.Path(__file__).name


def parse_args() -> argparse.Namespace:
    """Returns a namespace of parsed command-line arguments"""
    parser = argparse.ArgumentParser(
        description=(
            "Calculate a number of ECTS points of subjects given a csv file with "
            "subject names and number of their ects points. This file should also "
            "contain columns specifying a term, subject group and course if you want to "
            "take advantage of options for grouping ECTS sums. Columns "
            "need to be in a specific order: name, ects, course, group, term."
        )
    )
    parser.add_argument("file", type=str, help="input csv file")
    parser.add_argument(
        "-t", "--term", action="store_true", help="Group ECTS sums by semesters/terms"
    )
    parser.add_argument(
        "-g", "--group", action="store_true", help="Group ECTS sums by subject group"
    )
    parser.add_argument(
        "-c", "--course", action="store_true", help="Group ECTS sums by course"
    )
    parser.add_argument(
        "-s",
        "--just-sort",
        action="store_true",
        help="Don't sum ECTS just print soreted csv contents (works with other options, sorts alphabetically by default)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    file = pathlib.Path(args.file)

    # Check if the input file exists and exit with and error if it doesn't.
    if not file.exists():
        print(f"{SCRIPT_NAME}: error: [Errrno 2] No such file or directory '{file}'")
        return 2

    # Try to parse the input csv file.
    df: pandas.DataFrame = pandas.read_csv(
        file, sep=",\s+", encoding="utf-8", skipinitialspace=True, engine="python"
    )

    # Create a list of columns by which data should be grouped or sorted later.
    groups_to_sum_by = []
    if args.term:
        groups_to_sum_by.append(df.columns[4])
    if args.course:
        groups_to_sum_by.append(df.columns[2])
    if args.group:
        groups_to_sum_by.append(df.columns[3])

    if args.just_sort:
        # Print data frame sorted by given keys.
        print(df.sort_values(groups_to_sum_by + [df.columns[0]]))
    elif args.term or args.course or args.group:
        # Print ects sums grouped by given keys.
        print(df.groupby(groups_to_sum_by)[df.columns[1]].sum(numeric_only=True))
    else:
        # Just sum all ects.
        print(sum(df[df.columns[1]]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
