## Compare the Triplets

**Topic:** Basic Implementation
**Difficulty:** Easy
**HackerRank link:** https://www.hackerrank.com/challenges/compare-the-triplets/problem

### Approach
Pair the two triplets element-wise with `zip()` and award a point to whichever side is strictly greater. Ties give no points to either side.

### Complexity
- **Time:** O(1) — exactly three pairwise comparisons.
- **Space:** O(1) — two integer accumulators.

### Notes
The problem is fixed-size (n = 3), so the O(1) label is exact, not an amortised claim. Ties are common — worth an explicit test case.
