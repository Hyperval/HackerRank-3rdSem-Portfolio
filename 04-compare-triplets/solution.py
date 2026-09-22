"""
HackerRank: Compare the Triplets
Topic: Basic Implementation
Given two triplets (a and b), award 1 point to whichever side has the higher
value at each index. Return [alice_score, bob_score].

Time:  O(1)  — always exactly 3 comparisons
Space: O(1)
"""


def compareTriplets(a, b):
    alice = bob = 0
    for x, y in zip(a, b):
        if x > y:
            alice += 1
        elif x < y:
            bob += 1
    return [alice, bob]


if __name__ == "__main__":
    # Test 1 (typical): a=[5,6,7], b=[3,6,10] -> [1, 1]
    print(f"Test 1: {compareTriplets([5, 6, 7], [3, 6, 10])} (expected [1, 1])")

    # Test 2 (edge — full tie): a=[1,2,3], b=[1,2,3] -> [0, 0]
    print(f"Test 2: {compareTriplets([1, 2, 3], [1, 2, 3])} (expected [0, 0])")
