# An Analysis of The Split-30 Dilemma in Teamfight Tactics
Consider a game with 8 players, each of whom can choose to either **take** 10 gold or **split** 30 gold with the other players who also choose to split. Let \( n \) denote the number of players who choose to split. The payoffs for each strategy are as follows:

- **Split**: $\ \frac{30}{n}  (if \( n \geq 1 \))\$
- **Take**: $10$

The game does not reduce to a scalar in 8-dimensional space through iterated removal of dominated strategies, and there is no pure Nash Equilibrium. Consequently, players adopt mixed strategies to equate the expected payoffs of their choices, forming a Nash Equilibrium. 

Since the game is symmetric, it admits a symmetric Nash Equilibrium. Suppose each player chooses to split with probability \( p \) and to take with probability \( 1-p \). The expected payoff for choosing to take is straightforward:

$$\Pi(T) = 10$$

The expected payoff for choosing to split, however, depends on the number of other players who also choose to split. This can be expressed as:

$$\Pi(S) = \sum_{i=0}^{7} \binom{7}{i} p^i (1-p)^{7-i} \left( \frac{30}{i+1} \right)$$

To find the symmetric Nash Equilibrium, we equate the expected payoffs of the two strategies:

$$\sum_{i=0}^{7} \binom{7}{i} p^i (1-p)^{7-i} \left( \frac{30}{i+1} \right) = 10$$

Solving this equation numerically yields:

$$p \approx 0.365$$
