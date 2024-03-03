[Problem 876](https://projecteuler.net/problem=876): Triplet Tricks
===================================================================

Starting with three numbers $a, b, c$, at each step do one of the three
operations:

- change $a$ to $2(b + c) - a$;
- change $b$ to $2(c + a) - b$;
- change $c$ to $2(a + b) - c$;

Define $f(a, b, c)$ to be the minimum number of steps required for one number
to become zero. If this is not possible then $f(a, b, c) = 0$.

For example, $f(6, 10, 35) = 3$:

```math
(6, 10, 35) \to (6, 10, -3) \to (8, 10, -3) \to (8, 0, -3).
```

However, $f(6, 10, 36) = 0$ as no series of operations leads to a zero number.

Also define $\displaystyle F(a, b) = \sum_{c=1}^\infty f(a, b, c)$.
You are given $F(6, 10) = 17$ and $F(36, 100) = 179$.

Find $\displaystyle \sum_{k=1}^{18} F(6^k, 10^k)$.
