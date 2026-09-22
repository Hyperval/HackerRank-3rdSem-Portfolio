# HackerRank — 3rd Semester Portfolio

Algorithmic problem-solving portfolio for the course *Portfolio Building for Engineering Students (B25GE0101)*.

**Author:** Akhil Sathish Kumar (Reg No: R25EF019)
**GitHub:** [Hyperval](https://github.com/Hyperval)
**HackerRank profile:** *[paste your public HackerRank profile URL here]*
**Language:** Python 3

## Problem Set

| # | Problem                                                                 | Topic                    | Difficulty  | Time       | Space     |
|---|--------------------------------------------------------------------------|--------------------------|-------------|------------|-----------|
| 1 | [Diagonal Difference](./01-diagonal-difference/)                        | 2D Arrays / Matrices     | Easy        | O(n)       | O(1)      |
| 2 | [Dynamic Array](./02-dynamic-array/)                                    | Data Structures / Vectors| Easy        | O(n + q)   | O(n)      |
| 3 | [Time Conversion](./03-time-conversion/)                                | Strings & Logic          | Easy        | O(1)       | O(1)      |
| 4 | [Compare the Triplets](./04-compare-triplets/)                          | Basic Implementation     | Easy        | O(1)       | O(1)      |
| 5 | [Sparse Arrays](./05-sparse-arrays/)                                    | Hash Maps / Strings      | Easy-Medium | O(n + q)   | O(n)      |

Each folder contains a `solution.py`, a per-problem `README.md` with approach + complexity notes, and a screenshot of the Accepted HackerRank submission (`result.png`).

## How to Run a Solution Locally

```bash
python 01-diagonal-difference/solution.py
```

Each file contains a `main` block with 2 test cases (one typical, one edge). Output is printed to stdout with the expected answer next to it.

## Reflection: Algorithmic Optimisation Techniques Learned

Working through these five HackerRank problems reinforced a simple but important habit: **think about complexity before writing the loop**. The clearest example was *Sparse Arrays*, where a nested `for` loop would give O(n·q) and time out on the larger test cases, while a `collections.Counter` builds the frequency table once in O(n) and turns every query into an O(1) hash lookup. Same idea, drastically different runtime.

The other big lesson was recognising **fixed-size vs input-scaled work**. *Compare the Triplets* and *Time Conversion* are O(1) not because the code is trivial, but because the inputs are bounded — three integers and a 10-character string. Once I stopped counting statements and started counting how the work scales with input size, the complexity annotations for each solution became easier to reason about.

Finally, *Diagonal Difference* and *Dynamic Array* taught me to look for algebraic shortcuts. Instead of two full matrix scans, one loop with two indexed reads (`arr[i][i]` and `arr[i][n-1-i]`) handles both diagonals in a single pass. And instead of scanning to find the target inner list every query, the XOR-mod-n formula gives it directly. Choosing the right data structure and the right index expression usually matters more than clever code inside the loop.
