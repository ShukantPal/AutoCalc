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

from resolver import *

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
        
class ExpOp(BinOp):
    """Exponent operator object"""
    
    @staticmethod
    def tostr():
        return '^'
    
    @classmethod
    def levl(cls):
        return 2
    
    @classmethod
    def eval(cls, tlist):
        BinOp.eval(tlist)
        return pow(tlist[0], tlist[1])
