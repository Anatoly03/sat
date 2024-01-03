
import json
import sys
import math

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

def read_args():
    output = {
        'algorithm' : None,
        'benchmark' : False,
        'eq' : None,
        'help' : False,
        'input' : None,
        'output' : 'output',
        'test' : False,
    }

    for idx in range(1, len(sys.argv)):
        arg = sys.argv[idx]
        match arg:
            case '--':
                # if sys.argv[idx + 1] == 'rand':
                #     output['eq'] = random_equation(int(sys.argv[idx + 2], 10), int(sys.argv[idx + 3], 10), int(sys.argv[idx + 4], 10))
                # else:
                output['eq'] = eq_to_list(sys.argv[idx + 1])
            case '--alg':
                output['algorithm'] = sys.argv[idx + 1]
            case '-h' | '--help':
                output['help'] = True
                return output
            case '-B':
                output['benchmark'] = True
            case '-i' | '--input':
                output['input'] = sys.argv[idx + 1]
            case '-o' | '--output':
                output['output'] = sys.argv[idx + 1]
            case '-t' | '--test':
                output['test'] = sys.argv[idx + 1]
            
    return output

# def random_equation(solutions, variables, disjunctions):
#     return "1 | -1"