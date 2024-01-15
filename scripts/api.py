import itertools
import sys
import math

EQUATION_GRAMMAR = """Equation Grammar:
    * Disjunctions are separated by `|`
    * Literals are numbers, negative numbers represent negated variables.
    → Example: `1 2 -3 | -2 3 4 | -1 2 -4`"""

def write_equation(path, equation, solutions=None, comment=None):
    pass

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
                output['eq'] = sys.argv[idx + 1]
            case '-f':
                file = open(sys.argv[idx + 1], 'rb')
                # TODO
                file.close()
            case '--alg':
                output['algorithm'] = sys.argv[idx + 1]
            case '-h' | '--help':
                print(
                    "============================" +
                    help
                      .replace("%c", sys.argv[0])
                      .replace("%{grammar}", EQUATION_GRAMMAR)
                    + "============================"
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

    # idx = 1

    # while idx < len(sys.argv):
    #     arg = sys.argv[idx]
    #     optargs = []

    #     if (arg.startswith('-')):
    #         while idx < len(sys.argv) and not sys.argv[idx + 1].startswith('-'):
    #             optargs.append(idx + 1)
    #             idx += 1

    #     print()

    #     idx += 1

    return output


# def random_equation(solutions, variables, disjunctions):
#     return "1 | -1"