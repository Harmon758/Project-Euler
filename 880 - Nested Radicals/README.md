[Problem 880](https://projecteuler.net/problem=880): Nested Radicals
====================================================================

$(x, y)$ is called a *nested radical pair* if $x$ and $y$ are non-zero integers
such that $\dfrac{x}{y}$ is not a cube of a rational number, and there exist
integers $a$, $b$ and $c$ such that:

```math
\sqrt{\sqrt[3]{x} + \sqrt[3]{y}} = \sqrt[3]{a} + \sqrt[3]{b} + \sqrt[3]{c}
```

For example, both $(-4, 125)$ and $(5, 5324)$ are nested radical pairs:

```math
\begin{align*}
\begin{split}
\sqrt{\sqrt[3]{-4} + \sqrt[3]{125}} &= \sqrt[3]{-1} + \sqrt[3]{2} +
\sqrt[3]{4} \\
\sqrt{\sqrt[3]{5} + \sqrt[3]{5324}} &= \sqrt[3]{-2} + \sqrt[3]{20} +
\sqrt[3]{25} \\
\end{split}
\end{align*}
```

Let $H(N)$ be the sum of $|x| + |y|$ for all the nested radical pairs $(x, y)$
where $|x| \leq |y| \leq N$.  
For example, $H(10^3) = 2535$.

Find $H(10^{15})$. Give your answer modulo $1031^3 + 2$.
