#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       impact.py
#       
#       Copyright 2011 10 <1_0 <at> list.ru>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.



import math as mmm

#def pointsImpact(v1x, v1y, v2x, v2y):
def pointsImpact(v1x, v1y, v2x, v2y):

    """pointsImpact(v1x, v1y, v2x, v2y) very easy points impact"""
    return v2x, v2y, v1x, v1y
    
def sqImpact(x1, y1, v1x, v1y, x2, y2, v2x, v2y):

    """pointsImpact(v1x, v1y, v2x, v2y) very easy points impact"""
    return v2x, v2y, v1x, v1y
    
#def sqImpact(x1, y1, v1x, v1y, x2, y2, v2x, v2y):
def sqImpact2(x1, y1, v1x, v1y, x2, y2, v2x, v2y):
    """bsqImpact(x1, y1, v1x, v1y, x2, y2, v2x, v2y) 
    easy sq impact"""
    if v1x==0 or v2x==0:
        if v1x>v2x:
            v1x = v1x/2
            v2x = v1x
        else:
            v2x = v2x/2
            v1x = v2x

    if v1y==0 or v2y==0:
        if v1y>v2y:
            v1y = v1y/2
            v2y= v1y
        else:
            v2y = v2y/2
            v1y = v2y
            
    return v2x, v2y, v1x, v1y
    
def ballsImpact(x1, y1, r1, v1x, v1y, x2, y2, r2, v2x, v2y):
    """ballsImpact(x1, y1, r1, v1x, v1y, x2, y2, r2, v2x, v2y) 
    hard bals impact"""
    pass
    
def getLong(x, y):
    lll=mmm.sqrt(x**2+y**2)
    #print lll
    return lll

def ball1Impact(x1, y1, vx, vy, x2, y2):
    """ball1Impact(x1, y1, r1, v1x, v1y, x2, y2) very easy balls impact 
    2-nd ball is same mass, radius and 0 speed"""
    v=getLong(vx, vy)
    dx=x2-x1
    dy=y2-y1
    l=getLong(dx, dy)
    av=mmm.acos(vx/v)
    print av
    ac=mmm.acos(dx/l)
    print ac
    a=ac+av
    print a
    vnx=v*mmm.cos(a)
    print vnx
    vny=v*mmm.sin(a)
    print vny
    
    vn1x=vnx*mmm.cos(ac)
    vn1y=vnx*mmm.sin(ac)
    
    an=mmm.pi/4-ac
    
    vn2x=vnx*mmm.cos(an)
    vn2y=vnx*mmm.sin(an)
    
    
#    vn1x=int(round(vnx*mmm.cos(ac)))
#    vn1y=int(round(vnx*mmm.sin(ac)))
#    
#    an=mmm.pi/4-ac
#    
#    vn2x=int(round(vnx*mmm.cos(an)))
#    vn2y=int(round(vnx*mmm.sin(an)))
#    
    
    return vn1x, vn1y, vn2x, vn2y
    
if __name__ == '__main__':
    print "pointsImpact(1, 2, 3, 4) --- ", 
    print pointsImpact(1, 2, 3, 4)
    
    print "sqImpact(0, 2, 4, 5, 0, 3, 0, -3) --- " 
    print sqImpact(0, 2, 4, 5, 0, 3, -1, -3)
    
    
    
