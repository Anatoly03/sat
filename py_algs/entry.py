import json
import math
import sys
import subprocess

algs = [
    ('bf0', 'Brute Force (Default)'),
    ('3knf-bf0', 'Reduction to 3-KNF-SAT with Brute Force (Default)'),
]

def eq_to_list(eq):
    variables = []
    out = [[]]

    for clause in eq.split('|'):
        for var in clause.split():
            variable, new = int(var), 0
            abs_var = abs(variable)

            if abs_var in variables:
                new = variables.index(abs_var) + 1
            else:
                variables.append(abs_var)
                new = len(variables)

            out[-1].append(int(math.copysign(new, variable)))

        out.append([])

    del out[-1]
    
    return out

def varcount(eq_list):
    return max([abs(v) for clauses in eq_list for v in clauses])

def print_help():
    pass

def main():
    alg = 'bf0'
    eq = '1 | 2 | 3'

    for idx in range(1, len(sys.argv)):
        arg = sys.argv[idx]
        match arg:
            case '-v':
                alg = sys.argv[idx + 1]
                if alg not in [a[0] for a in algs]:
                    print(f"Algorithm {alg} does not exist. See -h for which algorithms can be used.")
                    sys.exit(1)
            case '--':
                eq = sys.argv[idx + 1]
                # TODO sanitize
            case '-h':
                print_help()
                sys.exit(0)

    ls = eq_to_list(eq)
    print(f'> {alg}, Equation(C{len(ls)}, V{varcount(ls)})')
    subprocess.run(['python3', 'alg-' + alg + '.py', json.dumps(ls)])

if '--' in sys.argv:
    main()
else:
    pass # TODO