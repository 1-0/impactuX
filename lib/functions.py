#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       functions.py
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

#import sqcheck, objects
import pygame, sys
#from pygame.locals import FULLSCREEN
        
class iPause:
    def __call__(self):
        return "pause"
        
class iExit:
    def __call__(self):
        return "exit"
        
class iRun:
    def __call__(self):
        return "run_game"
        
class iRestore:
    def __call__(self):
        return "restore_game"

class iSetup:
    def __call__(self):
        return "setup_game"

class iRecord:
    def __call__(self):
        return "record_game"
        
class Deltax:
    def __call__(self, pic_obj):
        return pic_obj.get_width()/2
        
class Deltay:
    def __call__(self, pic_obj):
        return pic_obj.get_height()/2
        
class Ending_play:
    def __call__(self, points=[]):
        print 'Added points: '
        for p in points:
            print str(p[0])
            
        pygame.mouse.set_visible(True)
        pygame.quit()
        sys.exit()
        
class Button_press_checking:
    def __call__(self, cour_x, cour_y, buttons):
        for b_obj in buttons:
            if b_obj.check_in(cour_x, cour_y):
                return (True, b_obj)
        return (False, 0)
        
class Let_addin_press_checking:
    def __call__(self, cour_x, cour_y, points, coursore_type, mouse_c0):
        deltax=Deltax()
        if coursore_type==mouse_c0:
            return False
        for p_obj in points:
            delt_r=deltax(coursore_type)
            if p_obj.check_in(cour_x+delt_r, cour_y+delt_r, delt_r):
                return True 
        return False

def get_screen_set():
    return (640,480),0,32

