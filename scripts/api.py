import itertools
import sys
import math

EQUATION_GRAMMAR = """Equation Grammar:
    * Disjunctions are separated by `|`
    * Literals are numbers, negative numbers represent negated variables.
    → Example: `1 2 -3 | -2 3 4 | -1 2 -4`"""

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

def varcount(eq):
    return max([abs(v) for clauses in eq for v in clauses])

def disjunctions(eq):
    return max([len(x) for x in eq])

def write_equation(path, equation, solutions=None, comment=None):
    # TODO use these
    VAR_DISJUNCT = max(math.ceil(math.log(disjunctions(equation), 256)), 1)
    VAR_BYTES = math.ceil(math.log(2 * varcount(equation), 256))

    if VAR_DISJUNCT > 4:
        print('There is a disjunction in the equation that\s too long.')
        sys.exit(1)

    if VAR_BYTES > 8:
        print('Too many variables.')
        sys.exit(1)

    #
    # 'CNF\n' magic header
    #

    file = open(path, "wb")
    file.write(b'CNF\n')

    #
    # Comments
    #
    
    if comment is not None:
        for i in comment.splitlines():
            file.write(b"# " + i.encode() + b"\n")

    #
    # Magic Bytes
    #
    
    file.write(VAR_DISJUNCT.to_bytes() + VAR_BYTES.to_bytes())

    #
    # Solutions
    #

    for sol in solutions:
        sb = ''
        print(sol)
        for bit in sol:
            if bit > 0:
                sb += '1'
            else:
                sb += '0'
        print(sb)
        pass

    # TODO

    

    #
    # Equation
    #

    for disjunction in equation:
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

    file.write(b"\0" * VAR_DISJUNCT)

    #
    # EOF
    #

    file.close()

def solve_equation(eq):
    SOLUTIONS = []

    def solve(EQC, verify, mode):
        if isinstance(EQC, int):
            return EQC * verify[abs(EQC) - 1] > 0
        
        return mode([solve(clause, verify, any) for clause in EQC])

    for verify in itertools.product((-1, +1), repeat=varcount(eq)):
        if solve(eq, verify, all):
            SOLUTIONS.append([(idx + 1) * x for idx, x in enumerate(verify)])

    return SOLUTIONS

def read_args(help):
    output = {
        'algorithm' : None,
        'benchmark' : False,
        'eq' : None,
        'input' : None,
        'number' : 8,
        'minimum' : 4,
        'maximum' : 64,
        'output' : 'output',
        'test' : False,
        'flags': []
    }

    for idx in range(1, len(sys.argv)):
        arg = sys.argv[idx]
        match arg:
            case '--':
                # if sys.argv[idx + 1] == 'rand':
                #     output['eq'] = random_equation(int(sys.argv[idx + 2], 10), int(sys.argv[idx + 3], 10), int(sys.argv[idx + 4], 10))
                # else:
                output['eq'] = eq_to_list(sys.argv[idx + 1])
            case '-f':
                file = open(sys.argv[idx + 1], 'rb')
                # TODO
                file.close()
            case '--alg':
                output['algorithm'] = sys.argv[idx + 1]
            case '-h' | '--help':
                print(help
                      .replace("%c", sys.argv[0])
                      .replace("%{grammar}", EQUATION_GRAMMAR)
                      )
                sys.exit(0)
            case '-B':
                output['benchmark'] = True
            case '-i' | '--input':
                output['input'] = sys.argv[idx + 1]
            case '-o' | '--output':
                output['output'] = sys.argv[idx + 1]
            case '-t' | '--test':
                output['test'] = sys.argv[idx + 1]
            case '-n':
                output['number'] = int(sys.argv[idx + 1], 10)
            case '--min':
                output['minimum'] = int(sys.argv[idx + 1], 10)
            case '--max':
                output['maximum'] = int(sys.argv[idx + 1], 10)
            case _:
                if arg.startswith('-'):
                    output['flags'].append(arg[1:])
                elif arg.startswith('--'):
                    output['flags'].append(arg[2:])

    return output

# def random_equation(solutions, variables, disjunctions):
#     return "1 | -1"