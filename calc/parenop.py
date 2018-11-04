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
from solve import *
import calcapi

class ParenOp(Resolver):
    """Parenthesis/Brackets/Curly-Braces Resolver Object
    
    Parenthesis operator (.i.e '(', '[', '{') is used to delimit
    higher priority sub-expressions (solved before the rest). This
    operator evaluates the expression using a recursive measure.
    
    Infact, this evaluation technique is so powerful that the front-end
    can use it invoking ParenOp.eval(tokenized_expression)
    """
    
    @staticmethod
    def tostr():
        return '(' # [ and { are lost (work under progress :)
    
    @classmethod
    def levl(cls):
        return 100
    
    @staticmethod
    def collect(exp, start_index):
        """Overrides Resolver.collect() for sub-expression in (...)
        
        Sub-expressions contained within parenthesis are extracted
        by ripping out the '(' and ')' (sub-list of tokens)
        """ 
        
        end_index = start_index + 1
        elen = len(exp)
        edepth = 1
        
        while end_index < elen:
            if exp[end_index].type == TOKEN_OPERATOR:
                if exp[end_index].val == '(':
                    edepth += 1
                elif exp[end_index].val == ')':
                    edepth -= 1
                    if edepth == 0:
                        break
            end_index += 1
            
        print "Solving",
        printexp(exp[start_index : end_index + 1])
        return exp[start_index + 1: end_index] # without ( and )
    
    @staticmethod
    def eval(tlist):
        ridx = 0
        rlen = len(tlist)
        
        while ridx < rlen:
            if tlist[ridx].type == TOKEN_OPERATOR and \
               tlist[ridx].val in calcapi.paren_open_bind:
               ParenOp.res(tlist, ridx) # adj keep ridx same!
               rlen = len(tlist)
            else:
                ridx += 1
    
        solve_bin_levl(tlist, 1)
        return solve_bin_levl(tlist, 0)
           
    @classmethod
    def res(cls, exp, sindex):
        subexp = cls.collect(exp, sindex)
        eindex = sindex + len(subexp) + 1
        result = cls.eval(subexp)
        
        print("partial finish")
        Resolver._deval(exp, sindex, eindex, result)
        
    @staticmethod
    def adj(exp, index):
        return index    # at index-1 result can be stored (replace '(')
    
    
