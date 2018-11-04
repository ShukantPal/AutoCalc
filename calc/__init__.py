# CalcAPI is used to represent mathematical expressions as a sequence
# of terms (e.g. Term objects). Special tokens (like operators and
# functions) are resolved using 'Resolver' objects. This API uses
# OOP heavily to represent resolvers.

# Future releases will include auto-loading of user-defined algebraic
# functions (maybe one day we'll use calculus-based functions too)

from resolver import *
from unop import *
from binop import *
from calcapi import *
from token import *
from solve import *
