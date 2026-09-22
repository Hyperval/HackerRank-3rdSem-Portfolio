"""
HackerRank: Time Conversion
Topic: Strings & Logic
Convert a 12-hour AM/PM timestamp (e.g. "07:05:45PM") to 24-hour military
format ("19:05:45"). Input string is guaranteed to be well-formed.

Time:  O(1)  — fixed-length string, constant work
Space: O(1)
"""


def timeConversion(s):
    period = s[-2:]         # "AM" or "PM"
    hh, mm, ss = s[:-2].split(":")
    hour = int(hh)

    if period == "AM":
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12

    return f"{hour:02d}:{mm}:{ss}"


if __name__ == "__main__":
    # Test 1 (typical PM): "07:05:45PM" -> "19:05:45"
    print(f"Test 1: {timeConversion('07:05:45PM')} (expected '19:05:45')")

    # Test 2 (edge — midnight AM): "12:00:00AM" -> "00:00:00"
    print(f"Test 2: {timeConversion('12:00:00AM')} (expected '00:00:00')")
