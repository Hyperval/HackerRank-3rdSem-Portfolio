"""
HackerRank: Sparse Arrays
Topic: Hash Maps / Strings
Given a list of strings and a list of query strings, return for each query
the count of how many times it appears in the string list.

Time:  O(n + q)  — one pass to build the frequency map, one pass over queries
Space: O(n)     — the frequency map holds at most n distinct strings
"""

from collections import Counter


def matchingStrings(strings, queries):
    counts = Counter(strings)
    return [counts[q] for q in queries]


if __name__ == "__main__":
    # Test 1 (typical): HackerRank sample
    s1 = ["aba", "baba", "aba", "xzxb"]
    q1 = ["aba", "xzxb", "ab"]
    print(f"Test 1: {matchingStrings(s1, q1)} (expected [2, 1, 0])")

    # Test 2 (edge — query not present): all queries miss
    s2 = ["a", "b", "c"]
    q2 = ["d", "e"]
    print(f"Test 2: {matchingStrings(s2, q2)} (expected [0, 0])")
