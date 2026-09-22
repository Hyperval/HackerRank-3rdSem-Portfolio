## Sparse Arrays

**Topic:** Hash Maps / Strings
**Difficulty:** Easy-Medium
**HackerRank link:** https://www.hackerrank.com/challenges/sparse-arrays/problem

### Approach
Build a frequency table (`collections.Counter`) over the input strings in a single pass. Each query then becomes an O(1) hash lookup. Missing queries return 0 automatically because `Counter` defaults to 0 for unseen keys.

### Complexity
- **Time:** O(n + q) — n to construct the frequency map, q to answer all queries.
- **Space:** O(n) — at most n distinct strings in the map.

### Notes
A naive nested loop would be O(n·q) which becomes unacceptable on the larger HackerRank test cases (constraints up to n, q ≤ 1000). The hash-map approach is the intended optimisation and the difference the problem is designed to teach.
