import api
from lib import Equation

api.help("""
--- BruteForce SatSolver ---

Solves a CNF SAT equation with 'Brute Force'
    Usage: %c -- 'Equation' [OPTIONS]

%{grammar}

Options:
    -o Output File (Will Write if Specified)
    -c Write Output to Console
""")

args = api.read_args() # "--:eq;-o:str;-c:bool"

EQUATION = Equation(args['eq'])

for verify in EQUATION.brute_force(): EQUATION.solves(verify)

print(f'The equation has {len(EQUATION.sols)} solutions.')

if 'c' in args['flags']:
    print('\n'.join(map(lambda x: str(x), EQUATION.sols)))