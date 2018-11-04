# Copyright (C) 2018 - Shukant Pal
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

# Autocalc is a program to simplify algebraic expressions!!! Future
# releases will include unary operators, built-in functions (like avg)
# and savable functions, etc.

__author__ = "Shukant Pal"
__copyright__ = "Copyright (C) 2018 Shukant Pal"
__license__ = "GNU General Public License v3"
__version__ = 1.0

from calcapi import *
from calcread import *

def exp(rawstr):
    pointer = 0 # current character being processed
    tlen = 0 # token length
    rlen = len(rawstr)
    
    token_chain = []
    
    while pointer < rlen:
        tokentype = parsertarget(rawstr, pointer)
        
        if tokentype == DIGITS:
            tlen = digit_length(rawstr, pointer)
            ntok = Token(TOKEN_NUMBER, convert_to_int(rawstr,pointer,pointer+tlen))
            token_chain.append(ntok)
        elif tokentype == ALPHAS:
            tlen = alpha_length(rawstr, pointer)
            
            if(tlen == 1):
                atok = Token(TOKEN_OPERATOR, rawstr[pointer])
                token_chain.append(atok)
            else:
                atok = Token(TOKEN_RESOLVER, rawstr[pointer:pointer+tlen])
                token_chain.append(atok)
        else:
            tlen = other_length(rawstr, pointer)
            
            if(tlen == 1):
                otok = Token(TOKEN_OPERATOR, rawstr[pointer])
                token_chain.append(otok)
            else:
                raise NotImplementedError("Unknown token found at " + str(pointer))
            
        pointer += tlen
    
    return token_chain

def printexp(texp):
    for tok in texp:
        print str(tok.val),
    print("")

def solve_bin_levl(texp, levl):
    pointer = 0 # dynamic pointer (index) to current element
    
    while pointer < len(texp): # len of texp will change
        if(texp[pointer].type == TOKEN_NUMBER):
            pointer += 1
            continue
        
        # First we have to identify the type of resolver, which
        # could be unary/binary operator, function, etc.
        
        if pointer == 0 and texp[1].type == TOKEN_NUMBER: # unary-op
            pointer += 1
            continue
        elif pointer == len(texp)-1:
            break # can't be a binary operator

        if texp[pointer-1].type == TOKEN_NUMBER and \
           texp[pointer+1].type == TOKEN_NUMBER: # binary operator, eval
            binop = texp[pointer].bin_op()
            
            if binop.levl() < levl:
                pointer+=1
                continue
            
            new_ptr = binop.adj(texp, pointer)
            binop.res(texp, pointer)
            printexp(texp)
            pointer = new_ptr
            continue

    return texp[0].val # result

def init():
        print("Autocalc 1.x initialized!");

def main():
        print("Autocalc 1.x");
        mexp = raw_input("Enter expression: ");
        
        tch = exp(mexp)
        
        r = solve_bin_levl(tch,1)
        r = solve_bin_levl(tch,0)
        
        print("Result: " + str(r));

if __name__ == "__main__":
        main();
else:
        print(__name__);