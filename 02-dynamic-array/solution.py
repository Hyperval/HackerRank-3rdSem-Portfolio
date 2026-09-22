"""
HackerRank: Dynamic Array
Topic: Data Structures / Vectors
Simulate a set of dynamic arrays with two query types (append, print).
Uses bitwise XOR to derive the target index without division.

Time:  O(n + q)  — one operation per query
Space: O(n)     — total elements stored across all inner arrays
"""


def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    last_answer = 0
    results = []
    for q in queries:
        query_type, x, y = q
        idx = (x ^ last_answer) % n
        if query_type == 1:
            arr[idx].append(y)
        else:  # query_type == 2
            last_answer = arr[idx][y % len(arr[idx])]
            results.append(last_answer)
    return results


if __name__ == "__main__":
    # Test 1 (HackerRank sample): n=2, queries -> [7, 3]
    n1 = 2
    q1 = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]
    print(f"Test 1: {dynamicArray(n1, q1)} (expected [7, 3])")

    # Test 2 (edge — single inner array): n=1, all appends then one read
    n2 = 1
    q2 = [[1, 0, 42], [1, 0, 99], [2, 0, 1]]
    print(f"Test 2: {dynamicArray(n2, q2)} (expected [99])")
