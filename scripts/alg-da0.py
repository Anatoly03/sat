import api
from lib import Equation

api.name("Disjunctive SatSolver")

api.usage(
    """
Solve a CNF SAT equation with 'Disjunctive Absorption'
    Usage: %c -- 'Equation' [OPTIONS]
    """
)

api.options(
    """
Options:
    -o Output File (Will Write if Specified)
    -c Write Output to Console
"""
)

args = api.read_args()  # "--:eq;-o:str;-c:bool"

################################################################
#                   DISJUNCTIVE ABSORPTION                     #
################################################################

EQUATION = Equation(args["eq"])

print()
print(EQUATION)
print("####")


def pick_best(eq: Equation) -> int:
    order = [(x,) + eq.occurences(x) for x in eq.var_iter()]
    order.sort(key=lambda x: max(abs(x[1]), abs(x[2])), reverse=True)

    if abs(order[0][1]) >= abs(order[0][2]):
        return order[0][0]
    return -order[0][0]


def trivial_pick(eq: Equation) -> list[int] | None:
    x = list(filter(lambda x: len(x) < 2, eq.disjunctions()))
    if len(x) == 0:
        return None
    return x


k = EQUATION.assume(pick_best(EQUATION))
print(k)
print("####")
