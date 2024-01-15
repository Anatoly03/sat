from collections.abc import Iterable
import itertools
import math

class Equation:
    #
    # Static Methods
    #

    # TODO

    #
    # Variables
    #

    eq: list[list[int]] = [[]]
    sols: list[list[int]] = []

    #
    # Methods
    #

    def __init__(self, eq_string: str):
        variables = []
        self.eq = [[]]
        self.sols = []

        if (eq_string is ''):
            return

        for clause in eq_string.split("|"):
            for var in clause.split():
                variable, new = int(var), 0
                abs_var = abs(variable)

                if abs_var in variables:
                    new = variables.index(abs_var) + 1
                else:
                    variables.append(abs_var)
                    new = len(variables)

                self.eq[-1].append(int(math.copysign(new, variable)))

            self.eq.append([])

        del self.eq[-1]

    #
    # The amount of disjunctions
    # 
    def disjunctions(self) -> Iterable[list[int]]:
        return iter(self.eq)

    #
    # Create an iterable over all solutions
    # 
    def brute_force(self) -> Iterable[list[int]]:
        return map(
            lambda x: [(idy + 1) * y for idy, y in enumerate(x)],
            itertools.product((-1, +1), repeat=self.varcount()),
        )

    #
    # Amount of Variables
    # 
    def varcount(self) -> int:
        return max([abs(v) for clauses in self.eq for v in clauses])
    
    #
    # Iterate over Variables
    # 
    def var_iter(self) -> Iterable[int]:
        return range(1, self.varcount() + 1)

    #
    # Occurences of a variable (left neutral, right negated)
    # 
    def occurences(self, var) -> (int, int):
        return (
            sum([1 if var in x else 0 for x in self.eq]),
            - sum([1 if -var in x else 0 for x in self.eq]),
        )
    
    #
    # Given an interpretation, get the grid of truthy disjunctions
    #
    def truthy_disjunctions(self, sol) -> list[bool]:
        return [any([i in sol for i in d]) for d in self.eq]
    
    # 
    # Does an interpretation satisfy the equation?
    # If yes, we also add it to the solutions.
    # 
    def solves(self, sol) -> bool:
        s = all(self.truthy_disjunctions(sol))
        if s and sol not in self.sols:
            self.sols.append(sol)
        return s
    
    #
    # Create a new equation assuming a certain variable to be truthy
    #
    def assume(self, val):
        out = Equation('')

        # This filters out all val's, as they are true.
        # out.eq = [d for d in filter(lambda d: val not in d, self.eq)]
        
        out.eq = [list(filter(lambda x: x != -val, d)) for d in filter(lambda d: val not in d, self.eq)]


        # out.eq = [list(filter(lambda x: -val == x, d)) for d in filter(lambda d: val not in d, self.eq)]
        # self.sols = [] # TODO

        return out

    # def __len__(self) -> int:
    #     """Amount of disjunctions."""
    #     return len(self.eq)

    #
    # Convert the equation and currently known solutions to a file format
    #
    def __bytes__(self, comment: str = None) -> [bytes, str]:
        # TODO

        """Convert the equation to a encoded format"""
        out = bytes()

        # TODO use these
        VAR_DISJUNCT = max(math.ceil(math.log(self.disjunctions(), 256)), 1)
        VAR_BYTES = math.ceil(math.log(2 * self.varcount(), 256))

        if VAR_DISJUNCT > 4:
            return [out, "There is a disjunction in the equation that\s too long."]

        if VAR_BYTES > 8:
            return [out, "Too many variables."]

        #
        # 'CNF\n' magic header
        #

        out += b"CNF\n"

        #
        # Comments
        #

        if comment is not None:
            for i in comment.splitlines():
                out += b"# " + i.encode() + b"\n"

        #
        # Magic Bytes
        #

        out += VAR_DISJUNCT.to_bytes() + VAR_BYTES.to_bytes()

        #
        # Solutions
        #

        for sol in self.sols:
            sb = ""
            print(sol)  # TODO remove
            for bit in sol:
                if bit > 0:
                    sb += "1"
                else:
                    sb += "0"
            print(sb)  # TODO remove
            pass

        # TODO

        #
        # Equation
        #

        for disjunction in self.equation:
            # TODO use VAR_DISJUNCT
            out += len(disjunction).to_bytes()

            for variable in disjunction:
                vbytes = abs(variable).to_bytes().zfill(VAR_BYTES)

                # print(vbytes[0], vbytes[0] | int('10000000', 2), bin(vbytes[0] | int('10000000', 2)), (vbytes[0] | int('10000000', 2)).to_bytes())

                if variable > 0:
                    out += vbytes[0].to_bytes()
                elif variable < 0:
                    out += (vbytes[0] | int("10000000", 2)).to_bytes()

                if len(vbytes) > 1:
                    out += vbytes[1:]

        out += b"\0" * VAR_DISJUNCT

        #
        # EOF
        #

        return out

    # def __hash__(self):
    #     """The equation is the only consistent part of the equation."""
    #     return hash(self.eq)

    # https://medium.com/@ayeshasidhikha188/a-journey-through-pythons-magic-methods-a35c79b856c7#:~:text=The%20__divmod__method,of%20their%20quotient%20and%20remainder.

    # __abs__
    # __mod__
    # __neg__
    # __pos__
    # __pow__

    def __str__(self):
        return ' | '.join([' '.join(map(str, d)) for d in self.eq])

    def __or__(self, other):
        pass  # disjunction of two equations

    def __add__(self, other):
        pass  # disjunction of two equations

    def __iadd__(self, other):
        pass  # +=

    def __and__(self, other):
        pass  # conjunction of two equations

    def __mul__(self, other):
        pass  # conjunction of two equations

    # __invert__ invert equation?

    def __imul__(self, other):
        pass  # *=

    def __contains__(self, other):
        pass

    def __delattr__(self, other):
        pass

    def __eq__(self, other):
        pass  # equivalence of two sats

    def __ne__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __format__(self, format):
        pass  # format sat

    def __getitem__(self, item):
        pass  # eq['something']

    # __hash__

    def __iter__(self):
        pass  # eq['something']

    def __reduce__(self):
        pass  # reduce

    # __reduce_ex__?

    def __reduce__(self):
        pass  # reduce

    # TODO
    # 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

class Solver:
    eq: Equation

    def __init__(self, eq_string: Equation):
        self.eq = eq_string

    