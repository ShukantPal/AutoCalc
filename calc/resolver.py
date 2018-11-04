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
