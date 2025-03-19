# An Analysis of The Split-30 Dilemma in Teamfight Tactics
Consider a game with 8 players where each player tries to maximize their gold (not the case in an actual game of Teamfight Tactics; the utility of gold is not linear and there is additional utility in minimizing other players' gold), each of whom can choose to either **take** 10 gold or **split** 30 gold with the other players who also choose to split. Let $n$ denote the number of players who choose to split. The payoffs for each strategy are as follows:

- **Split**: $\ \frac{30}{n}   (if \( n \geq 1 \))\$
- **Take**: $10$

The game does not reduce to a scalar in 8-dimensional space through iterated removal of dominated strategies, thus there is no pure Nash Equilibrium. Consequently, players adopt mixed strategies to equate the expected payoffs of their choices, forming a Nash Equilibrium. 

Since the game is evidently symmetric, it admits a symmetric Nash Equilibrium. Suppose each player chooses to split with probability $p$ and to take with probability $\( 1-p \)$. The expected payoff for choosing to take is straightforward:

$$\Pi(T) = 10$$

The expected payoff for choosing to split, however, depends on the number of other players who also choose to split. This can be expressed as:

$$ \Pi(S) = \sum_{i=0}^{7} \binom{7}{i} p^i (1-p)^{7-i} \left( \frac{30}{i+1} \right) $$

For clarity:
- $\binom{7}{i}$ is the number of ways $i$ players out of the 7 others can choose to split
- $(p^i)(1-p)^{7-i}$ is the probability that a specific set of $i$ players split
- $\frac{30}{i+1}$ is the payoff when the player splits and $i$ other players split

To find the symmetric Nash Equilibrium, we equate the expected payoffs of the two strategies:

$$\sum_{i=0}^{7} \binom{7}{i} p^i (1-p)^{7-i} \left( \frac{30}{i+1} \right) = 10$$

[Solving](numericalsolution.py) this equation yields:

$$p \approx 0.365$$

This means that, on average, about 36.5% of the players will choose to split, while the remaining 63.5% will choose to take. 

## Evolutionary Stability

In layman’s terms, evolutionary stability is a strategy's ability to resist being replaced by alternative strategies in a population. This strategy is evolutionarily stable. If fewer people start splitting and $p<0.365$; then the expected payoff for splitting will increase and exceed that of taking, making more people start splitting. If more people start splitting and $p>0.365$; then the expected payoff for splitting will drop and the payoff for taking will exceed that of splitting, making more people start taking.

Let us verify whether this mixed strategy $d$ satisfies the two formal mathematical conditions of an evolutionarily stable strategy:

1. $d$ is a symmetric Nash equilibrium.
2. For every pure strategy that is the best response to $d$, its expected value is lower in response to itself

### 1. Symmetric Nash Equilibrium

As previously established, since the game is symmetric, it admits a symmetric Nash Equilibrium

### 2. Stability Against Mutations

Evaluating the two pure strategies of taking every time and splitting every time.

$d$ against taking every time:

$$0.365 \times (30) + (1 - 0.365) \times 10 = 17.3$$

Taking every time against itself: 

$$10$$

It is better than taking every time

$$17.3 > 10$$

$d$ against splitting every time:

$$0.365 \times (30/8) + (1 - 0.365) \times 10 = 7.72$$

Splitting every time against itself:

$$8/3 = 2.67$$ 

It is better than splitting every time

$$7.72 > 2.67$$

Thus, the solution to the split-30 dilemma is evolutionarily stable. 
