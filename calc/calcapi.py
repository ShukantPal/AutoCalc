# Copyright (C) 2018 - Shukant Pal
#
# This file is a part of CalcAPI
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

# CalcAPI is used to represent mathematical expressions as a sequence
# of terms (e.g. Term objects). Special tokens (like operators and
# functions) are resolved using 'Resolver' objects. This API uses
# OOP heavily to represent resolvers.

# Future releases will include auto-loading of user-defined algebraic
# functions (maybe one day we'll use calculus-based functions too)

__author__ = "Shukant Pal"
__copyright__ = "Copyright (C) 2018 Shukant Pal"
__license__ = "GNU General Public License v3"
__version__ = 1.0

from unop import UnOp
from unop import NegOp

from binop import BinOp
from binop import AddOp
from binop import SubOp
from binop import MulOp
from binop import DivOp
from binop import ModOp
from binop import ExpOp

from parenop import ParenOp

from func import Average
        
# Dictionaries for mapping (abstract) Resolver identifiers (like '+')
# to their class object (like AddOp).

# List of all loaded resolvers
all_resolvers = [
    '+', '-', '*', '/', '%', '(', '[', '{' 
]

# Unary operator bindings
uop_bind = {
    '-': NegOp
}

# Binary operator bindings
bop_bind = {
    "+": AddOp,
    "-": SubOp,
    "*": MulOp,
    "/": DivOp,
    "%": ModOp,
    '^': ExpOp
}

paren_open_bind = {
    '(', '{', '['
}

paren_close_bind = {
    ')', '}', ']'
}

rtfunc_bind = {
    "avg": Average
}