#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       sqcheck.py
#       
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

import math


def CheckRound (xo, yo, ro, x1, y1, r1=0):
    """CheckRound (xo, yo, ro, x1, y1, r1=0) check (round o and round 1) 
    or (round and point - r1=0) for impact. x, y - center, r - radius."""
#    x**2+y**2=r**2
    xnorm=abs(x1-xo)
    ynorm=abs(y1-yo)
    rsum=ro+r1

    if xnorm>rsum:
        return False
    elif ynorm>rsum:
        return False
    elif (xnorm**2+ynorm**2)>(rsum**2):
        return False
    else:
        #print """it is in Round
         #"""
        return True

def CheckSquare (xo, yo, ro, x1, y1, r1=0):
    """CheckSquare (xo, yo, ro, x1, y1, r1=0) check (square o and square
     1) or (square and point - r1=0) for impact. x, y - center, 
     r - radius."""
#    
    xnorm=abs(x1-xo)
    ynorm=abs(y1-yo)
    rsum=ro+r1
# 
    if xnorm>rsum:
        return False
    elif ynorm>rsum:
        return False
    else:
        return True

def CheckRectangle (xo, yo, rox, roy, x1, y1, r1x=0, r1y=0):
    """CheckRectangle (xo, yo, rox, roy, x1, y1, r1x=0, r1y=0) check 
    (rectangle o and rectangle 1) or (rectangle and line - r1y=0) or 
    (rectangle and point - r1x=0, r1y=0) for impact. x, y - center, 
    r - radius."""
#    
    xnorm=abs(x1-xo)
    ynorm=abs(y1-yo)
    rsumx=rox+r1x
    rsumy=roy+r1y
# 
    if xnorm>rsumx:
        return False
    elif ynorm>rsumy:
        return False
    else:
        return True

def CheckRectPoint (xo, yo, lxo, lyo, x1, y1):
    """CheckRectPoint (xo, yo, lxo, lyo, x1, y1) check rectangle for 
    impact. x0, y0 - center, l - length with point x1 y1."""
#    
    xo_end=xo+lxo
    yo_end=yo+lyo
# 
    if xo>x1:
        return False
    elif yo>y1:
        return False
    elif x1>xo_end:
        return False
    elif y1>yo_end:
        return False
    else:
        return True

def Lenght2Point (x1,y1,x2,y2):
    """Lenght2Point (x1,y1,x2,y2) get distance from x1,y1 to x2,y2"""
    xn=x2-x1
    yn=y2-y1
    lll=math.sqrt(xn**2+yn**2)
    return lll

def SqTriangle (x1,y1,x2,y2,x3,y3):
    """SqTriangle (x1,y1,x2,y2,x3,y3) get triangle ABC squer, A(x1,y1), 
    B(x2,y2), C(x3,y3)"""
    a=Lenght2Point (x1,y1,x2,y2)
    b=Lenght2Point (x2,y2,x3,y3)
    c=Lenght2Point (x3,y3,x1,y1)
    p=(a+b+c)/2
    sss=math.sqrt(p*(p-a)*(p-b)*(p-c))
    #print sss
    return sss
    
    

def CheckQuadrangle (x1,y1,x2,y2,x3,y3,x4,y4, x0,y0):
    """CheckQuadrangle (x1,y1,x2,y2,x3,y3,x4,y4, x0,y0) check strong 
    quadrangle x1,y1,x2,y2,x3,y3,x4,y4 for impact to point x0 y0."""
    aaa=0.5
    
    points=[(x1,y1),(x2,y2),(x3,y3),(x4,y4)]
    sq1=SqTriangle (points[0][0],points[0][1],points[1][0],points[1][1],points[2][0],points[2][1])
    sq2=SqTriangle (points[0][0],points[0][1],points[3][0],points[3][1],points[2][0],points[2][1])
    sss=sq1+sq2
    
    sq_p12=SqTriangle (points[0][0],points[0][1],points[1][0],points[1][1],x0,y0)
    sq_p23=SqTriangle (x0,y0,points[1][0],points[1][1],points[2][0],points[2][1])
    sq_p34=SqTriangle (x0,y0,points[3][0],points[3][1],points[2][0],points[2][1])
    sq_p41=SqTriangle (points[0][0],points[0][1],points[3][0],points[3][1],x0,y0)
    sss_p=sq_p12+sq_p23+sq_p34+sq_p41
    
    d_sss=abs(sss-sss_p)
    
#    return (d_sss==0)
    return (d_sss<aaa)
    
def SortQuadrangle (x1,y1,x2,y2,x3,y3,x4,y4):
    """SortQuadrangle (x1,y1,x2,y2,x3,y3,x4,y4) try to sort 4 points like 
    in strong quadrangle"""
    points=[(x1,y1),(x2,y2),(x3,y3),(x4,y4)]
    
    for i in range(0,3):
        for k in range((i+1),4):
           
            if points[i]==points[k]:
                print "not good - 2 points are same"
                return False

    points.sort()

    max_not_good=True

    while max_not_good:
        max_dist=0
        max_dist_point_number=0

        for n in range(1,4):
            ddd= (points[0][0]-points[n][0])**2+(points[0][1]-points[n][1])**2
            if ddd==max_dist:
                max_not_good=True
            elif ddd>max_dist:
                max_dist=ddd
                max_dist_point_number=n
                max_not_good=False
        if max_not_good:
            points=[points[1],points[2],points[3],points[0]]
            print "points="+str(points)
                
    point2=points[2]
    points[2]=points[max_dist_point_number]
    points[max_dist_point_number]=point2
    
    return [points[0][0],points[0][1],points[1][0],points[1][1],points[2][0],points[2][1],points[3][0],points[3][1]]

    
def DirectPart (x1,y1,x2,y2,partscount):
    """DirectPart (x1,y1,x2,y2,partscount) try to find round+ part number
    in strong quadrangle, the 0-part loock direct up at screen

    315***O**45deg
       ********
       ********
    270***X***90deg
       ********
       ********
       ********
    225******135deg

    """
    xnorm=x2-x1
    ynorm=y2-y1 
    if xnorm==0:
        if ynorm>=0:
            return (partscount-1)/2 #direct up at screen
        else:
            return 0
    tan_fi=ynorm*1.0/xnorm
    if xnorm>0:
        for ppp in range(partscount/2):
            #count for every part fi
            ppptan=math.tan((1+2*ppp)*math.pi/partscount)
    #        ppptan=math.tan((1+2*ppp)*math.pi/partscount)
            if tan_fi<ppptan:
#                return ppp
                return (partscount/2)-ppp
    else:
        for ppp in range((partscount/2),partscount):
            #count for every part fi
            ppptan=math.tan((1+2*ppp)*math.pi/partscount)
    #        ppptan=math.tan((1+2*ppp)*math.pi/partscount)
            if tan_fi<ppptan:
                return (partscount/2)+partscount-ppp

         
    return 0
                    
    
    


if __name__ == '__main__':
    print 'DirectPart (2,2,6,6,360) '+str(DirectPart (2,2,6,6,360))
    print 'DirectPart (6,6,2,2,360) '+str(DirectPart (6,6,2,2,360))
    print 'DirectPart (0,0,3,4,360) '+str(DirectPart (0,0,3,4,360))

    print 'DirectPart (5,5,3,4,360) '+str(DirectPart (5,5,3,4,360))
    print 'DirectPart (5,5,6,4,360) '+str(DirectPart (5,5,6,4,360))
    print 'DirectPart (7,8,3,4,360) '+str(DirectPart (7,8,3,4,360))


    print 'DirectPart (2,2,6,6,4) '+str(DirectPart (2,2,6,6,4))
    print 'DirectPart (6,6,2,2,4) '+str(DirectPart (6,6,2,2,4))
    print 'DirectPart (5,5,3,4,4) '+str(DirectPart (5,5,3,4,4))

#    print 'CSortQuadrangle (0,5,5,0,0,-5,-5,0, 1,1) '+str(CheckQuadrangle (0,5,5,0,0,-5,-5,0, 6,6))
#    print 'CheckQuadrangle (0,1,1,0,0,-1,-1,0, 0,0) '+str(CheckQuadrangle (0,1,1,0,0,-1,-1,0, 0,0))
#    print 'CheckQuadrangle (0,1,1,0,0,-1,-1,0, 0,0.11) '+str(CheckQuadrangle (0,1,1,0,0,-1,-1,0, 0,0.11))
    
    
    #print 'CSortQuadrangle (1,1,2,3,3,3,4,4)'+str(SortQuadrangle (1,1,2,2,3,3,4,4))
    #print 'CSortQuadrangle (0,1,0,2,0,3,0,4)'+str(SortQuadrangle (0,1,0,2,0,3,0,4))
    #print 'CSortQuadrangle (0,1,0,2,0,1,0,4)'+str(SortQuadrangle (0,1,0,2,0,1,0,4))


    
    #print 'CheckRectPoint (0, 1, 2, 2, 9, 3)='+str(CheckRectPoint (0, 1, 2, 2, 9, 3))







