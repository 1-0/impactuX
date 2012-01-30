#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       .py
#       impactuX - tuX collision game
#       Copyright 2011 10 <1_0 <at> list.ru>
#       
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import functions

def mainrun(scr_params=((640,480),0,32),qqq=0,www=0,eee=0,rrr=0):
    functions.add_params()
    print "setup!!!"
    pass

if __name__ == '__main__':
    runing = True
    while runing:
        mmm=mainrun()
        runing = (mmm <>"exit")
