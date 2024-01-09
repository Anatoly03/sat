import api
import sys

args = api.read_args("""============================
---- Sat2File Converter ----

Converts a CNF SAT equation to a compressed file.
    Usage: %c -- 'Equation' [OPTIONS]

Equation Grammar:
    * Disjunctions are separated by `|`
    * Literals are numbers, negative numbers represent negated variables.
    → Example: `1 2 -3 | -2 3 4 | -1 2 -4`

Options:
    -o   | Output File
    -c   | Add Equation Comment
============================""")

EQUATION = args['eq']

if EQUATION is None:
    print('no equation')
    sys.exit(1)

EQUATION_STRING_COMMENT = ''
if 'c' in args['flags']:
    EQUATION_STRING_COMMENT = ' | '.join([' '.join(map(str, disjunct)) for disjunct in EQUATION])

api.write_equation(args["output"], EQUATION, api.solve_equation(EQUATION), EQUATION_STRING_COMMENT)

print(f'Success Write to `{args["output"]}`')
