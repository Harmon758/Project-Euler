[Problem 506](https://projecteuler.net/problem=506): Clock Sequence
===================================================================

Consider the infinite repeating sequence of digits:  
1234321234321234321...

Amazingly, you can break this sequence of digits into a sequence of integers
such that the sum of the digits in the $n$-th value is $n$.

The sequence goes as follows:  
1, 2, 3, 4, 32, 123, 43, 2123, 432, 1234, 32123, ...

Let $v_n$ be the $n$-th value in this sequence. For example, $v_2=2$, $v_5=32$
and $v_{11}=32123$.

Let $S(n)$ be $v_1+v_2+\cdots+v_n$. For example, $S(11)=36120$, and
$S(1000)\bmod 123454321=18232686$.

Find $S(10^{14})\bmod 123454321$.
