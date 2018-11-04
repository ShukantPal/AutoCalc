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

from calc import *
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
            nptr = pointer
            
            while nptr < tlen + pointer:
                otok = Token(TOKEN_OPERATOR, rawstr[nptr])
                token_chain.append(otok)
                nptr += 1
            
        pointer += tlen
    
    return token_chain

def init():
        print("Autocalc 1.x initialized!");

def main():
        print("Autocalc 1.x");
        mexp = raw_input("Enter expression: ");
        
        tch = exp(mexp)
        
        r = ParenOp.eval(tch)
        
        print("Result: " + str(r));

if __name__ == "__main__":
        main();
else:
        print(__name__);
