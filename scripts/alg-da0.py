import api
from lib import Equation

args = api.read_args("""
--- Disjunctive SatSolver ---

Solve a CNF SAT equation with 'Disjunctive Absorption'
    Usage: %c -- 'Equation' [OPTIONS]

%{grammar}

Options:
    -o Output File (Will Write if Specified)
    -c Write Output to Console
""")

EQUATION = Equation(args['eq'])

print()
print(EQUATION)
print('####')

order = [(x,) + EQUATION.occurences(x) for x in EQUATION.var_iter()]
order.sort(key = lambda x: max(abs(x[1]), abs(x[2])), reverse=True)

tr = 1 if abs(order[0][1]) >= abs(order[0][2]) else -1

k = EQUATION.assume(order[0][0] * tr)
print(k)
print('####')
