from resolver import *
from token import *

import func
import calcapi

def printexp(texp):
    for tok in texp:
        print str(tok.val),
    print("")

def solveallfuncs(texp):
    """Solves all functions in the highest scope
    
    Before sub-expressions, all functions are resolved, which
    paradoxically means that functions in sub-expressions won't
    be resolved first. This method just resolves functions that
    are not enclosed in parenthesis.
    """

    pointer = 0
    tlen = len(texp)
    sdepth = 0

    while pointer < tlen:
        if sdepth == 0 and texp[pointer].type == TOKEN_RESOLVER:
            calcapi.rtfunc_bind[texp[pointer].val].res(texp, pointer) # no need for adj (we already know)
            tlen = len(texp)
            pointer += 1
            continue
        
        if texp[pointer].type == TOKEN_OPERATOR:
            if texp[pointer].val in calcapi.paren_open_bind:
                sdepth += 1
            elif texp[pointer].val in calcapi.paren_close_bind:
                sdepth -= 1
        
        pointer += 1
                

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
        
