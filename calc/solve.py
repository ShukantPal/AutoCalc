from resolver import *
from token import *

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
        
