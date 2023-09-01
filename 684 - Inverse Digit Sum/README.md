[Problem 684](https://projecteuler.net/problem=684): Inverse Digit Sum
======================================================================

Define $s(n)$ to be the smallest number that has a digit sum of $n$. For
example $s(10) = 19$.

Let $\displaystyle S(k) = \sum_{n=1}^k s(n)$. You are given $S(20) = 1074$.

Further let $f_i$ be the Fibonacci sequence defined by $f_0=0, f_1=1$ and
$f_i=f_{i-2}+f_{i-1}$ for all $i \ge 2$.

Find $\displaystyle \sum_{i=2}^{90} S(f_i)$. Give your answer modulo
$`1\,000\,000\,007`$.
