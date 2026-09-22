## Diagonal Difference

**Topic:** 2D Arrays / Matrices
**Difficulty:** Easy
**HackerRank link:** https://www.hackerrank.com/challenges/diagonal-difference/problem

### Approach
Walk the matrix once with a single loop from `0` to `n-1`. The primary diagonal element on row `i` sits at column `i`; the secondary at column `n-1-i`. Sum both diagonals in the same pass and return the absolute difference.

### Complexity
- **Time:** O(n) — one linear scan over the diagonals (n additions each), not O(n²) since only 2n elements are touched.
- **Space:** O(1) — only two accumulator variables.

### Notes
Edge cases:
- A 1×1 matrix returns 0 (both diagonals are the same single element).
- Negative values are handled — the sums can go negative but `abs()` normalises.
