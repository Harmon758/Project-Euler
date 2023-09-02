[Problem 852](https://projecteuler.net/problem=852): Coins in a Box
===================================================================

This game has a box of $N$ unfair coins and $N$ fair coins. Fair coins have
probability 50% of landing heads while unfair coins have probability 75% of
landing heads.

The player begins with a score of 0 which may become negative during play.

At each round the player randomly picks a coin from the box and guesses its
type: fair or unfair. Before guessing they may toss the coin any number of
times; however, each toss subtracts 1 from their score. After guessing the
player's score is increased by 20 if they are right and decreased by 50 if
they are wrong. Then the coin type is revealed to the player and the coin is
discarded.

After $2N$ rounds the box will be empty and the game is over. Let $S(N)$ be the
expected score of the player at the end of the game assuming that they play
optimally in order to maximize their expected score.

You are given $S(1) = 20.558591$ rounded to 6 digits after the decimal point.

Find $S(50)$. Give your answer rounded to 6 digits after the decimal point.
