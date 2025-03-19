from scipy.optimize import fsolve
from scipy.special import comb

def expected_split(p):
    total = 0
    for n in range(8):
        total += (30 / (n + 1)) * comb(7, n) * (p ** n) * ((1 - p) ** (7 - n))
    return total

def equation(p):
    return expected_split(p) - 10

p_star = fsolve(equation, 0.5)[0] 
print(f"The critical probability is about p = {p_star:.4f}")
