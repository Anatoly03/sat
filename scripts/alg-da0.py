import api

args = api.read_args("""
--- Disjunctive SatSolver ---

Solve a CNF SAT equation with 'Disjunctive Absorption'
    Usage: %c -- 'Equation' [OPTIONS]

%{grammar}

Options:
    -o Output File (Will Write if Specified)
    -c Write Output to Console
""")

EQUATION = args['eq']

def trivial():
    pass

print()

for i in range(0, api.varcount(EQUATION)):
    print(i, api.occurences(EQUATION, i))
