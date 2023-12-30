import sys
import subprocess

algs = [
    ('bf0', 'Brute Force (Default)')
]

def eq_to_list(eq):
    return []

def main():
    alg = 'bf0'
    eq = '1 | 2 | 3'

    for idx in range(1, len(sys.argv)):
        arg = sys.argv[idx]
        match arg:
            case '-v':
                alg = sys.argv[idx + 1]

                break
            case '--':
                eq = sys.argv[idx + 1]
                break
            case '-h':
                print('TODO Help Message') # TODO
                sys.exit(0)
            
    subprocess.run(['python3', alg + '.py', eq])

if '--' in sys.argv:
    main()
else:
    pass # TODO