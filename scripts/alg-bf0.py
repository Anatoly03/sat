import api
import itertools

args = api.read_args("""============================
--- BruteForce SatSolver ---

Solves a CNF SAT equation with 'Brute Force'
    Usage: %c -- 'Equation' [OPTIONS]

%{grammar}

Options:
    -o Output File (Will Write if Specified)
    -c Write Output to Console
============================""")

SOLUTIONS = api.solve_equation(args['eq'])

# SOLUTIONS = []

# def solve(EQC, verify, mode):
#     if isinstance(EQC, int):
#         return EQC * verify[abs(EQC) - 1] > 0
    
#     return mode([solve(clause, verify, any) for clause in EQC])

# for verify in itertools.product((-1, +1), repeat=args['eq-variables']):
#     if solve(args['eq'], verify, all):
#         SOLUTIONS.append(' '.join([str((idx + 1) * x) for idx, x in enumerate(verify)]))

print(f'The equation has {len(SOLUTIONS)} solutions.')
if 'c' in args['flags']:
    print('\n'.join(map(lambda x: str(x) ,SOLUTIONS)))