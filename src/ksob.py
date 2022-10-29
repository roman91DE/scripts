#!/usr/bin/python3

from argparse import ArgumentError
from datetime import datetime, timedelta

def main():

    start = datetime(
        year=2022,
        month=7,
        day=15,
        hour=16,
        minute=30
    )
    now = datetime.now()
    time_delta = now - start
    
    def print_unit(td: timedelta, unit:str) -> None:
        td_in_secs = time_delta.total_seconds()

        if unit == "sec":
            out = td_in_secs
        elif unit == "min":
            out = td_in_secs / 60
        elif unit == "hours":
            out = td_in_secs / (60**2)
        elif unit == "days":
            out = td_in_secs / ((60**2) * 24)
        elif unit == "weeks":
            out = td_in_secs / ((60**2) * 24 * 7)
        elif unit == "months":
            out = td_in_secs / ((60**2) * 24 * 30.5)
        elif unit == "years":
            out = td_in_secs / ((60**2) * 24 * 30.5 * 12)
        else:
            raise RuntimeError

        unitstr = unit + ":"
        print(f"- {unitstr:<16} {out:>16.4f}")
    
    print("Time elapsed in:")
    for unit in ("sec", "min", "hours", "days", "weeks", "months", "years"):
        print_unit(time_delta, unit)


if __name__ == "__main__":
    main()
