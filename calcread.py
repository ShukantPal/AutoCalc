# Copyright (C) 2018 - Shukant Pal
#
# This file is a part of AutoCalc
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

# Used by AutoCalc to parse raw string inputs into CalcAPI-based
# token lists.

__author__ = "Shukant Pal"
__copyright__ = "Copyright (C) 2018 Shukant Pal"
__license__ = "GNU General Public License v3"
__version__ = 1.0

DIGITS = 1
ALPHAS = 2
UNKNOWN = 0

def parsertarget(raw_exp, cidx):
    """Identifies the type of token placed at the given location
    
    Reads nearby areas of the expression at the given location in
    the string and identifies the type of token placed there. This
    may be DIGITS or ALPHAS (which means a number or resolver)
    """
    
    if raw_exp[cidx] >= '0' and raw_exp[cidx] <= '9':
        return DIGITS
    elif raw_exp[cidx] >= 'a' and raw_exp[cidx] <= 'z':
        return ALPHAS
    else:
        return UNKNOWN

def digit_length(raw_exp, cindex):
    digits_counted = 0;
    while cindex < len(raw_exp):
        if raw_exp[cindex] >= '0' and raw_exp[cindex] <= '9':
            digits_counted += 1
            cindex += 1
        else:
            return digits_counted
    return digits_counted

def alpha_length(raw_exp, cindex):
    alphas_counted = 0;
    while cindex < len(raw_exp):
        if raw_exp[cindex] >= 'a' and raw_exp[cindex] <= 'z':
            alphas_counted += 1
            cindex += 1
        else:
            return alphas_counted
    return alphas_counted

def other_length(raw_exp, cidx):
    others_counted = 0
    while cidx < len(raw_exp):
        if (raw_exp[cidx] < 'a' or raw_exp[cidx] > 'z') \
           and (raw_exp[cidx] < '0' or raw_exp[cidx] > '9'):
            others_counted += 1
            cidx += 1
        else:
            return others_counted
    return others_counted
    
ord_1 = ord('1')

def _digofch(ch):
    """Returns the numeric value for the character given"""
    return 1 + ord(ch) - ord_1

def convert_to_int(raw_exp, cidx, dlim):
    """Returns the numeric value for the substring given"""
    num = 0.;
    while(cidx < dlim):
        num = 10 * num + _digofch(raw_exp[cidx]);
        cidx += 1
    return num