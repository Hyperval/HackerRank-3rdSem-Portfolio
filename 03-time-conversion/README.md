## Time Conversion

**Topic:** Strings & Logic
**Difficulty:** Easy
**HackerRank link:** https://www.hackerrank.com/challenges/time-conversion/problem

### Approach
Slice the AM/PM suffix off the string, split the rest on `:` to isolate hours/minutes/seconds, and apply two special-case rules:
- `12` AM becomes `00` (midnight).
- `12` PM stays `12` (noon).
- Any other PM value gets `+12`.

Re-emit with `HH:MM:SS` where the hour is zero-padded to two digits.

### Complexity
- **Time:** O(1) — the input is a fixed 10-character string.
- **Space:** O(1) — no auxiliary data structures.

### Notes
Both edge cases (12 AM and 12 PM) trip a straight `+12` formula, which is why they are handled explicitly. Minutes and seconds pass through untouched.
