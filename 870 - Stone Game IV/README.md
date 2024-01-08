[Problem 870](https://projecteuler.net/problem=870): Stone Game IV
==================================================================

Two players play a game with a single pile of stones of initial size $n$. They
take stones from the pile in turn, according to the following rules which
depend on a fixed real number $r \gt 0$:

- In the first turn, the first player may take $k$ stones with $1 \le k \lt n$.
- If a player takes $m$ stones in a turn, then in the next turn the opponent
  may take $k$ stones with $1 \le k \le \lfloor r \cdot m \rfloor$.

Whoever cannot make a legal move loses the game.

Let $L(r)$ be the set of initial pile sizes $n$ for which the second player has
a winning strategy. For example,
$`L(0.5) = \{1\}`$, $`L(1) = \{1, 2, 4, 8, 16, \dots\}`$,
$`L(2) = \{1, 2, 3, 5, 8, \dots\}`$.

A real number $q \gt 0$ is a *transition value* if $L(s)$ is different from
$L(t)$ for all $s \lt q \lt t$.  
Let $T(i)$ be the $i$-th transition value. For example, $T(1) = 1$, $T(2) = 2$,
$T(22) \approx 6.3043478261$.

Find $T(123456)$ and give your answer rounded to $10$ digits after the decimal
point.
