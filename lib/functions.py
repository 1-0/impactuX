#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       functions.py
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

#import sqcheck, objects
import pygame, sys, os
#from pygame.locals import FULLSCREEN
        
class iExit:
    def __call__(self):
        return "exit"
        
class iRun:
    def __call__(self):
        return "run"
        
class iRestore:
    def __call__(self):
        return "restore"

class iSetup:
    def __call__(self):
        return "setup"

class iRecord:
    def __call__(self):
        return "record"
        
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
    
def sec_to_minute(sec):
    minute = sec/60
    seconde = sec-(minute*60)
    return minute, seconde
    
def sec_to_h(sec):
    hhh = sec/3600
    minute = (sec-(hhh*3600))/60
    seconde = sec-((hhh*3600)+(minute*60))
    return hhh, minute, seconde

def get_screen_set():
    return (640,480),0,32

def save_game(g_score, g_time=None, g_lvl=None, g_balls=None, g_file=None, g_cours=None):
    import ConfigParser
    if g_file:
        f_name = g_file
    else:
        f_name = "last_game.cnf"
    
    f_name="."+os.sep+"saves"+os.sep+f_name
    
    config = ConfigParser.RawConfigParser()
    config.add_section('Last_game')
    config.set('Last_game', 'game_score', str(g_score))
    config.set('Last_game', 'game_time', str(g_time))
    config.set('Last_game', 'game_level', str(g_lvl))
    config.set('Last_game', 'balls_prop', str(g_balls))
    config.set('Last_game', 'cours_prop', str(g_cours))
    try:
        with open(f_name, 'wb') as configfile:
            sss = config.write(configfile)
        configfile.close()
        return sss
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise
    
def load_game(f_name="last_game.cnf"):
    import ConfigParser
     
    f_name="."+os.sep+"saves"+os.sep+f_name
    config = ConfigParser.RawConfigParser()
    try:
        config.read(f_name)
    
        g_score=eval(config.get('Last_game', 'game_score'))
        g_time=eval(config.get('Last_game', 'game_time'))
        g_lvl=eval(config.get('Last_game', 'game_level'))
        g_balls=eval(config.get('Last_game', 'balls_prop'))
        g_cours=eval(config.get('Last_game', 'cours_prop'))
    
        return g_score, g_time, g_lvl, g_balls, g_cours
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise
    
if __name__ == '__main__':
    #print get_screen_set()
    print sec_to_h(3667)
    #print save_game(182, 181, 1, [[33,33,1,1],[44,44,1,-1],[55,55,2,2],[77,77,-2,1],[121,121,1,-2]])
    #print load_game()
    pass

