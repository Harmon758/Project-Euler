[Problem 69](https://projecteuler.net/problem=69) /
[Challenge #69](https://www.hackerrank.com/contests/projecteuler/challenges/euler069/problem):
Totient Maximum
===============

Euler's totient function, $\phi(n)$ [sometimes called the phi function], is
defined as the number of positive integers not exceeding $n$ which are
relatively prime to $n$. For example, as $1$, $2$, $4$, $5$, $7$, and $8$, are
all less than or equal to nine and relatively prime to nine, $\phi(9)=6$.

<div align="center">

| **$n$** | **Relatively Prime** | **$\phi(n)$** | **$n/\phi(n)$** |
| :-----: | :------------------: | :-----------: | :-------------: |
|    2    |          1           |       1       |        2        |
|    3    |         1,2          |       2       |       1.5       |
|    4    |         1,3          |       2       |        2        |
|    5    |       1,2,3,4        |       4       |      1.25       |
|    6    |         1,5          |       2       |        3        |
|    7    |     1,2,3,4,5,6      |       6       |    1.1666...    |
|    8    |       1,3,5,7        |       4       |        2        |
|    9    |     1,2,4,5,7,8      |       6       |       1.5       |
|   10    |       1,3,7,9        |       4       |       2.5       |

</div>

It can be seen that $n = 6$ produces a maximum $n/\phi(n)$ for $n\leq 10$.

Find the value of $n\leq 1\,000\,000$ for which $n/\phi(n)$ is a maximum.

[ProjectEuler+ Problem Statement](ProjectEuler%2B%20Challenge%20%2369%20Problem%20Statement.pdf)

The Project Euler problem is equivalent to the ProjectEuler+ challenge with
$T = 1$, $`N = 1\,000\,001`$, and `N_UPPER_BOUND = 1_000_001`.
