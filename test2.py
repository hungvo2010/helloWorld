import math
def maximumSum(a, m):
    n = len(a)
    if n == 0:
        return 0
    # build the potential phi in [0, m-1]
    phi = [(a[0] % m, 0)]
    # current max sum
    max_sum = phi[0][0]
    for i in range(1, n):
        pot = (phi[-1][0] + a[i]) % m
        phi.append((pot, i))
        if pot > max_sum:
             max_sum = pot
 
    # we now need to look for negative cases
    phi.sort()
    candidate=0
    for j in range(n-1, 0, -1):
        pot, pos = phi[j]
        pot_prev, pos_prev = phi[j-1]
        # we must have pos_prev > pos
        if pos_prev > pos:
            candidate = (pot_prev - pot) % m
        if candidate > max_sum:
            max_sum = candidate
    return max_sum
a=[int(x) for x in input().split()]
m=int(input())
print(maximumSum(a,m))