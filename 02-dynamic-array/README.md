## Dynamic Array

**Topic:** Data Structures / Vectors
**Difficulty:** Easy
**HackerRank link:** https://www.hackerrank.com/challenges/dynamic-array/problem

### Approach
Maintain a list of `n` inner lists. For each query, compute the target index as `(x XOR last_answer) mod n`. Type 1 queries append; type 2 queries read and update `last_answer`. The XOR trick avoids storing a running sum and matches HackerRank's expected formula exactly.

### Complexity
- **Time:** O(n + q) — one constant-time operation per query (append or index lookup); the leading `n` accounts for the initial list allocation.
- **Space:** O(n + total appended elements) — the outer list is size `n`, and inner lists grow as append queries arrive.

### Notes
- Every read index (`y % len(arr[idx])`) is taken modulo the current inner-list length, which HackerRank guarantees is non-empty at read time. Assuming the input is well-formed avoids an unnecessary bounds check.
- `last_answer` starts at 0 by definition.
