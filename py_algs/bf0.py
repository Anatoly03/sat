import math
import itertools
import sys

from entry import eq_to_list, varcount
EQ = eq_to_list(sys.argv[1:][0])

SOLUTIONS = 0

def solve(EQC, verify, mode):
    if isinstance(EQC, int):
        return EQC * verify[abs(EQC) - 1] > 0
    
    return mode([solve(clause, verify, any) for clause in EQC])

for verify in itertools.product((-1, +1), repeat=varcount(EQ)):
    if solve(EQ.copy(), verify, all):
        if SOLUTIONS == 0:
            print(f'Solution: {verify}')
        SOLUTIONS += 1

print(f'The equation has {SOLUTIONS} solutions.')