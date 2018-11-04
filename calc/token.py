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

import calcapi

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
        return calcapi.uop_bind[self.val]
        
    def bin_op(self):
        return calcapi.bop_bind[self.val]
