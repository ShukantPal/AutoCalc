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
import parenop

__author__ = "Shukant Pal"
__copyright__ = "Copyright (C) 2018 Shukant Pal"
__license__ = "GNU General Public License v3"
__version__ = 1.0

class Function(Resolver):
    """A proper mathematical function of the syntax name(args)"""
    
    @staticmethod
    def collect_arg(exp, index):
        """Collects one arguments in the function enclosers
        
        Arguments in a function may be complex, and may require
        simplification. This method takes the first token in a
        function argument and finds the last token in it, and
        then returns the [endIndex, result]
        """

        fdepth = 1
        elen = len(exp)
        startIndex = index

        while fdepth > 0 and index < elen :
            if exp[index].type == TOKEN_OPERATOR:
                if exp[index].val == '(':
                    fdepth += 1
                elif exp[index].val == ')':
                    fdepth -= 1
                    if fdepth == 0:  # this is the last argument
                        break
                elif exp[index].val == ',' and fdepth == 1:
                    break
            index += 1

        return [index, parenop.ParenOp.eval(exp[startIndex: index])]

    @staticmethod
    def collect(exp, idx):
        """Overrides Resolver.collect() for mathematical functions
        
        Functions use '()' delimiters to enclose their argument,
        which comes in conflict with sub-expressions. Hence, as
        a rule of thumb, if a TOKEN_RESOLVER is present before
        a '(' operator, it cannot be resolved using ParenOp.res()
        
        Function arguments are simplified before being passed.

        NOTE: The last argument passed in Function.collect is the
        index of last ) closing the function arguments. This should
        be noted by the subclasses.
        """

        if exp[idx + 1].val != '(':
            raise NotImplementedError("Functions start with (")

        args = []
        pointer = idx + 1 # start of first argument

        while exp[pointer].type == TOKEN_NUMBER or \
              exp[pointer].val != ')':
                # add +1 to pointer, to skip ',' (& '(' at start)
                larg = Function.collect_arg(exp, pointer+1)
                args.append(larg[1])
                pointer = larg[0]

        args.append(pointer) 
        return args

    @staticmethod
    def eval(tlist):
        raise NotImplementedError("Function.eval undefined ")

    @classmethod
    def res(cls, exp, index):
        fargs = cls.collect(exp, index)
        fresult = cls.eval(fargs)
        Resolver._deval(exp, index, fargs[len(fargs)-1], fresult)
    
    @staticmethod
    def adj(exp, index):
        return index # result stored in function token

# Some basic built-in functions are implemented here as examples.

class Average(Function):

    @staticmethod
    def tostr(cls):
        return "avg"

    @staticmethod
    def eval(inputargs):
        argindex = 0
        argcount = len(inputargs) - 1
        argsum = 0

        while argindex < argcount:
            argsum += inputargs[argindex]
            argindex += 1

        return argsum / argcount