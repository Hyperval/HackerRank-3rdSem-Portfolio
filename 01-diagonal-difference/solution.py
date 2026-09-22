"""
HackerRank: Diagonal Difference
Topic: 2D Arrays / Matrices
Given a square matrix, return the absolute difference between the sums
of its primary and secondary diagonals.

Time:  O(n)
Space: O(1)
"""


def diagonalDifference(arr):
    n = len(arr)
    primary = sum(arr[i][i] for i in range(n))
    secondary = sum(arr[i][n - 1 - i] for i in range(n))
    return abs(primary - secondary)


if __name__ == "__main__":
    # Test 1 (typical): 3x3 matrix, primary=1+5+9=15, secondary=3+5+7=15, diff=0
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Test 1: {diagonalDifference(m1)} (expected 0)")

    # Test 2 (typical): HackerRank sample, expected 15
    m2 = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    print(f"Test 2: {diagonalDifference(m2)} (expected 15)")
