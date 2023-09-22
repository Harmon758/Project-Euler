[Problem 822](https://projecteuler.net/problem=822): Square the Smallest
========================================================================

A list initially contains the numbers $2, 3, \dots, n$.  
At each round, the smallest number in the list is replaced by its square. If
there is more than one such number, then only one of them is replaced.

For example, below are the first three rounds for $n = 5$:

```math
[2, 3, 4, 5] \xrightarrow{(1)} [4, 3, 4, 5] \xrightarrow{(2)} [4, 9, 4, 5]
\xrightarrow{(3)} [16, 9, 4, 5].
```

Let $S(n, m)$ be the sum of all numbers in the list after $m$ rounds.

For example, $S(5, 3) = 16 + 9 + 4 + 5 = 34$. Also
$S(10, 100) \equiv 845339386 \pmod{1234567891}$.

Find $S(10^4, 10^{16})$. Give your answer modulo $1234567891$.
