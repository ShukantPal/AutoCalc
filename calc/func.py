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

class Function(Resolver):
    """A proper mathematical function of the syntax name(args)"""
    
    @staticmethod
    def collect(exp, idx)
        """Overrides Resolver.collect() for mathematical functions
        
        Functions use '()' delimiters to enclose their argument,
        which comes in conflict with sub-expressions. Hence, as
        a rule of thumb, if a TOKEN_RESOLVER is present before
        a '(' operator, it cannot be resolved using ParenOp.res()
        """
        
        
