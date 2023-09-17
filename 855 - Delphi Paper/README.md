[Problem 855](https://projecteuler.net/problem=855): Delphi Paper
=================================================================

Given two positive integers $a,b$, Alex and Bianca play a game in $ab$ rounds.
They begin with a square piece of paper of side length $1$.

In each round Alex divides the current rectangular piece of paper into
$a \times b$ pieces using $a-1$ horizontal cuts and $b-1$ vertical ones. The
cuts do not need to be evenly spaced. Moreover, a piece can have zero
width/height when a cut coincides with another cut or the edge of the paper.
The pieces are then numbered $1, 2, ..., ab$ starting from the left top corner,
moving from left to right and starting from the left of the next row when a row
is finished.

Then Bianca chooses one of the pieces for the game to continue on. However,
Bianca must not choose a piece with a number she has already chosen during the
game.

Bianca wants to minimize the area of the final piece of paper while Alex wants
to maximize it. Let $S(a,b)$ be the area of the final piece assuming optimal
play.

For example,
$S(2,2) = 1/36$ and $S(2, 3) = 1/1800 \approx 5.5555555556\mathrm {e}{-4}$.

Find $S(5,8)$. Give your answer in scientific notation rounded to ten
significant digits after the decimal point. Use a lowercase e to separate the
mantissa and the exponent.
