[Problem 851](https://projecteuler.net/problem=851): SOP and POS
================================================================

Let $n$ be a positive integer and let $E_n$ be the set of $n$-tuples of
strictly positive integers.

For $u = (u_1, \cdots, u_n)$ and $v = (v_1, \cdots, v_n)$ two elements of
$E_n$, we define:

- the *Sum Of Products* of $u$ and $v$, denoted by
  $\langle u, v \rangle$, as the sum $\displaystyle \sum_{i = 1}^n u_i v_i$;
- the *Product Of Sums* of $u$ and $v$, denoted by $u \star v$, as the
  product $\displaystyle \prod_{i = 1}^n (u_i + v_i)$.

Let $R_n(M)$ be the sum of $u \star v$ over all ordered pairs $(u, v)$ in $E_n$
such that $\langle u, v \rangle = M$.  
For example: $R_1(10) = 36$, $R_2(100) = 1873044$,
$R_2(100!) \equiv 446575636 \bmod 10^9 + 7$.

Find $R_6(10000!)$. Give your answer modulo $10^9 + 7$.
