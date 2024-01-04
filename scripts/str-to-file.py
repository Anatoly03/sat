import api
import math
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
    -o Output File
    -c Add Equation Comment
============================""")

EQUATION = args['eq']

if EQUATION is None:
    print('no equation')
    sys.exit(1)

# print(EQUATION)

# TODO use these
VAR_DISJUNCT = max(math.ceil(math.log(args['eq-disjuncts'], 256)), 1)
VAR_BYTES = math.ceil(math.log(2 * args['eq-variables'], 256))

if VAR_DISJUNCT > 4:
    print('There is a disjunction in the equation that\s too long.')
    sys.exit(1)

if VAR_BYTES > 8:
    print('Too many variables.')
    sys.exit(1)

file = open(args['output'], "wb")

file.write(b'CNF\n')
if 'c' in args['flags']:
    file.write(b'# ' + (' | '.join([' '.join(map(str, disjunct)) for disjunct in EQUATION])).encode() + b'\n')
file.write(VAR_DISJUNCT.to_bytes() + b' ' + VAR_BYTES.to_bytes() + b'\n')

for disjunction in EQUATION:
    # TODO use VAR_DISJUNCT
    file.write(len(disjunction).to_bytes())
    for variable in disjunction:
        vbytes = abs(variable).to_bytes().zfill(VAR_BYTES)

        # print(vbytes[0], vbytes[0] | int('10000000', 2), bin(vbytes[0] | int('10000000', 2)), (vbytes[0] | int('10000000', 2)).to_bytes())

        if variable > 0:
            file.write(vbytes[0].to_bytes())
        elif variable < 0:
            file.write((vbytes[0] | int('10000000', 2)).to_bytes())

        if len(vbytes) > 1:
            file.write(vbytes[1:])

    # print()

file.close()

print(f'Success Write to `{args["output"]}`')
