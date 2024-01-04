import api

args = api.read_args("""============================
---- Sat2File Converter ----

Generates a CNF SAT equation procedurally and writes it to a file
    Usage: %c -n VARIABLES [OPTIONS]

Options:
    -o    | Output File
    --min | Minimal Amount of Solutions
    --max | Maximal Amount of Solutions
============================""")

VARIABLES = args['number']
MIN_SOLUTIONS = args['minimum']
MAX_SOLUTIONS = args['maximum']
EQUATION = []

# TODO