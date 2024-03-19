[Problem 882](https://projecteuler.net/problem=882): Removing Bits
==================================================================

Dr. One and Dr. Zero are playing the following partisan game.  
The game begins with one $1$, two $2$'s, three $3$'s, ..., $n$ $n$'s. Starting
with Dr. One, they make moves in turn.  
Dr. One chooses a number and changes it by removing a $1$ from its binary
expansion.  
Dr. Zero chooses a number and changes it by removing a $0$ from its binary
expansion.  
The player that is unable to move loses.  
Note that leading zeros are not allowed in any binary expansion; in particular
nobody can make a move on the number $0$.

They soon realize that Dr. Zero can never win the game. In order to make it
more interesting, Dr. Zero is allowed to "skip the turn" several times, i.e.
passing the turn back to Dr. One without making a move.

For example, when $n = 2$, Dr. Zero can win the game if allowed to skip $2$
turns. A sample game:

```math
[1, 2, 2]\xrightarrow{\textrm{Dr. One}}
[1, 0, 2]\xrightarrow{\textrm{Dr. Zero}}
[1, 0, 1]\xrightarrow{\textrm{Dr. One}}
[1, 0, 0]\xrightarrow[\textrm{skip}]{\textrm{Dr. Zero}}
[1, 0, 0]\xrightarrow{\textrm{Dr. One}}
[0, 0, 0]\xrightarrow[\textrm{skip}]{\textrm{Dr. Zero}}
[0, 0, 0].
```

Let $S(n)$ be the minimal number of skips needed so that Dr. Zero has a winning
strategy.  
For example, $S(2) = 2$, $S(5) = 17$, $S(10) = 64$.

Find $S(10^5)$.
