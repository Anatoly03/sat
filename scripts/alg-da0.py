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

def pick_best(eq):
    order = [(x,) + eq.occurences(x) for x in eq.var_iter()]
    order.sort(key = lambda x: max(abs(x[1]), abs(x[2])), reverse=True)
    
    if abs(order[0][1]) >= abs(order[0][2]):
        return order[0][0]
    return - order[0][0]

k = EQUATION.assume(pick_best(EQUATION))
print(k)
print('####')
