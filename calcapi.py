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

TOKEN_NUMBER = 324
TOKEN_OPERATOR = 353
TOKEN_RESOLVER = 3253

class Resolver:
    """Mathematical function taking an unknown number of inputs
    
    Resolver should be overridden/implemented to create new ways
    of simplifying a collection of terms (e.g. like AddOp). There
    are three built-in Resolver types, namely - UnOp, BinOp, and
    ParenOp.
    """
    
    @staticmethod
    def tostr():
        raise NotImplementedError("Resolver.tostr() unimplemented!!!")
    
    @staticmethod
    def _deval(exp, stidx, enidx, result):
        """"Devalutes the sub-expression from stidx to enidx
        
        Simply replaces the sub-expression (holding the tokens in the
        range [stidx, enidx] with the result.
        """

        del exp[stidx + 1 : enidx + 1]
        exp[stidx].type = TOKEN_NUMBER
        exp[stidx].val = result
            
    @staticmethod
    def collect(exp, index):
        """Returns the arguments from the tokenized expression
        
        Resolver implementations must override this method to collect
        their arguments from the token list, given their identifier's
        position. This will be passed to eval() which will actually
        do the operation (on those arguments).
        """
        raise NotImplementedError("Resolver.collect() unimplemented!")
    
    @staticmethod
    def eval(tlist):
        raise NotImplementedError("Resolver.eval() unimplemented!")
        
    @classmethod
    def res(cls, exp, index):
        """Injects the evaluated result into the expression
        
        Resolves the sub-expression handled by this object. Combines
        all of _deval(), collect(), and eval() to do everything! Must
        be implemented by subclasses (to pass required args to _deval())
        
        Generally implemented as:
        Resolver._deval(exp, unknown*, unknown*, eval(collect(exp,index)))
        where unknown* is implementation dependent
        """
        raise NotImplementedError("Resolver.res() unimplemented!!")
    
    @staticmethod
    def adj(exp, index):
        """Returns the value of the pointer after evaluating at index
        
        Once res() is called, some tokens are deleted and the new index
        must be found. This is done invoking adj(exp, pointer). This
        adjustment may be static (like pointer - 1) or dynamic.
        """
        raise NotImplementedError("Resolver.adj() unimplemented!!")

class UnOp(Resolver):
    """Unary operator object"""
    
    @staticmethod
    def eval(tlist):
        assert len(tlist) == 1, "UnOp accepts only 1 term"

class NegOp(UnOp):
    """Negation operator object"""
    
    @staticmethod
    def eval(tlist):
        UnOp.eval(tlist)
        return -1 * tlist[0]

class BinOp(Resolver):
    """Binary operator (takes two inputs) object"""

    @classmethod
    def levl(cls):
        """Level of the binary operator (precedence level)"""
        assert cls != BinOp
        return cls.levl()

    @staticmethod
    def collect(exp, index):
        """Overrides Resolver.collect() for binary operator
        
        Collects the tokens before and after the operator token and
        returns them as a list. This shouldn't be overriden by
        subclasses (for obvious reasons).
        """
        
        return [exp[index - 1].val, exp[index + 1].val]
        
    @staticmethod
    def eval(tlist):
        assert len(tlist) == 2, "BinOp accepts only 2 terms"
        
    @classmethod
    def res(cls, exp, index):
        Resolver._deval(exp, index-1, index+1, cls.eval(cls.collect(exp,index)))

    @staticmethod
    def adj(exp, index):
        return index # at index - 1, result is stored, hence index

class AddOp(BinOp):
    """Addition operator object"""
    
    @staticmethod
    def tostr():
        return '+'
    
    @classmethod
    def levl(cls):
        return 0
    
    @classmethod
    def eval(cls, tlist):
        BinOp.eval(tlist)
        return tlist[0] + tlist[1]
        
class SubOp(BinOp):
    """Subtraction operator object"""
    
    @staticmethod
    def tostr():
        return '-'
    
    @classmethod
    def levl(cls):
        return 0
    
    @classmethod
    def eval(cls, tlist):
        BinOp.eval(tlist)
        return tlist[0] - tlist[1]
        
class MulOp(BinOp):
    """Multiplication operator object"""
    
    @staticmethod
    def tostr():
        return '*'
    
    @classmethod
    def levl(cls):
        return 1
    
    @classmethod
    def eval(cls, tlist):
        BinOp.eval(tlist)
        return tlist[0] * tlist[1]

class DivOp(BinOp):
    """Division operator object"""
    
    @staticmethod
    def tostr():
        return '/'
    
    @classmethod
    def levl(cls):
        return 1
    
    @classmethod
    def eval(cls, tlist):
        BinOp.eval(tlist)
        return tlist[0] / tlist[1]

class ModOp(BinOp):
    """Modulo operator object"""
    
    @staticmethod
    def tostr():
            return '%'
    
    @classmethod
    def levl(cls):
        return 1
    
    @classmethod
    def eval(cls, tlist):
        BinOp.eval(tlist)
        return tlist[0] % tlist[1]
        
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
    "%": ModOp
}

# TOKEN_OPERATOR tokens have values as a character but
# TOKEN_RESOLVER tokens have values as a string

class Token:
    """Represents a token placed in the expression
    
    Tokens represent separated entities in a mathematical expression
    which include operators and numbers.
    """
    
    def __init__(self, type, val):
        self.type = type;
        self.val = val;
    
    def un_op(self):
        return uop_bind[self.val]
        
    def bin_op(self):
        return bop_bind[self.val]
        