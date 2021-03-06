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
        
class iMenu:
    def __call__(self):
        return "menu"
        
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
        print('Added points: ')
        for p in points:
            print(str(p[0]))
            
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
    minute = int(sec/60)
    seconde = int(sec-(minute*60))
    return minute, seconde
    
def sec_to_h(sec):
    hhh = int(sec/3600)
    minute = int((sec-(hhh*3600))/60)
    seconde = int(sec-((hhh*3600)+(minute*60)))
    return hhh, minute, seconde

def get_screen_set():
    from pygame.locals import FULLSCREEN
    sss=get_param(["screen_width", "screen_height", "screen_flags", "screen_depth"], "screen", "conf_game.ini")
    if sss[2]=="fullscreen":
        sss[2]=FULLSCREEN
    return (sss[0],sss[1]),sss[2],sss[3]
    #return (640,480),0,32

def get_param(p_names, g_section="screen", g_file="conf_game.ini"):
    from configparser import ConfigParser
    f_name="."+os.sep+"saves"+os.sep+g_file
    # config = ConfigParser.RawConfigParser()
    config = ConfigParser()
    try:
        config.read(f_name)
        rrr=[]
        for ppp in p_names:
            nnn = eval(config.get(g_section, ppp))
            rrr.append(nnn)
        return rrr
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

def set_check_rec(new_result, g_file="rec_game.ini", g_section="best_games", count_rec=10):
    rrr=load_rec(count_rec=10)
    kkk=rrr.keys()
    kkk.sort()
    ccc=False
    for nnn in kkk:
        r_1=rrr[nnn]
        if r_1[0]<new_result[0]:
            ccc=True
            rrr[nnn],new_result = new_result,rrr[nnn]
    if ccc:
        save_rec(rrr)
        return True
    return False                                                                                                                                                                                                                        

def load_rec(g_file="rec_game.ini", g_section="best_games", count_rec=10):
    import ConfigParser
    f_name="."+os.sep+"saves"+os.sep+g_file
    config = ConfigParser.RawConfigParser()
    rrr={}
    try:
        config.read(f_name)
        for kkk in range(count_rec):
            rrr[str(kkk)] = eval(config.get(g_section, str(kkk)))
        return rrr
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

def save_set(game_dict, g_file="rec_game.ini", g_section="best_games"):
    import ConfigParser
    f_name="."+os.sep+"saves"+os.sep+g_file
    config = ConfigParser.RawConfigParser()
    config.add_section(g_section)
    for kkk in game_dict.keys():
        config.set(g_section, str(kkk), str(game_dict[str(kkk)]))
    try:
        with open(f_name, 'wb') as configfile:
            sss=config.write(configfile)
        configfile.close()
        return sss
    except:
        print("Unexpected error:", sys.exc_info()[0])

def save_rec(game_dict, g_file="rec_game.ini", g_section="best_games", count_rec=10):
    import ConfigParser
    f_name="."+os.sep+"saves"+os.sep+g_file
    config = ConfigParser.RawConfigParser()
    config.add_section(g_section)
    for kkk in range(count_rec):
        config.set(g_section, str(kkk), str(game_dict[str(kkk)]))
    try:
        with open(f_name, 'wb') as configfile:
            sss=config.write(configfile)
        configfile.close()
        return sss
    except:
        print("Unexpected error:", sys.exc_info()[0])

def save_game(g_score, g_time=None, g_lvl=None, g_balls=None, g_cours=None, g_file="last_game.ini", g_section="Last_game", count_rec=6):
    """save_game - save game state to gzip-ini file"""
    from configparser import ConfigParser
    # import gzip
    print(str([g_score, g_time, g_lvl, g_balls, g_cours, g_file, g_section, count_rec]))
    f_name="."+os.sep+"saves"+os.sep+g_file
    
    config = ConfigParser()
    config.add_section('Last_game')
    config.set(g_section, 'game_score', str(g_score))
    config.set(g_section, 'game_time', str(g_time))
    config.set(g_section, 'game_level', str(g_lvl))
    config.set(g_section, 'balls_prop', str(g_balls))
    config.set(g_section, 'cours_prop', str(g_cours))
    try:
        load_new = True
        num_rec = 0
        # configfile = gzip.open(g_file, 'wb')
        configfile = open(g_file, 'w')
        while load_new:
            try:
                config.write(configfile)
                if num_rec<count_rec:
                    load_new = False
                else:
                    num_rec += 1
            except:
                load_new = ()
        configfile.close()
        return
    except:
        print("Unexpected error:", sys.exc_info()[0])
        configfile.close()
        raise
    
def load_game(f_name="last_game.ini", g_section="Last_game"):
    """load_game - load saved game state from gzip-ini file"""
    import lib.RawConfigParserGZ as RawConfigParserGZ
     
    f_name="."+os.sep+"saves"+os.sep+f_name
    config = RawConfigParserGZ.RawConfigParserGZ()
    try:
        config.read(f_name)
    
        g_score=eval(config.get(g_section, 'game_score'))
        g_time=eval(config.get(g_section, 'game_time'))
        g_lvl=eval(config.get(g_section, 'game_level'))
        g_balls=eval(config.get(g_section, 'balls_prop'))
        g_cours=eval(config.get(g_section, 'cours_prop'))
        #print(config.sections())
    
        #print({"score":g_score, "time":g_time, "level":g_lvl, "balls":g_balls, "coursor":g_cours})
        return {"score":g_score, "time":g_time, "level":g_lvl, "balls":g_balls, "coursor":g_cours}
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    
def add_params(p_name=0, g_section="screen", g_file="conf_game.ini"):
    #import ConfigParser
    pass
    
if __name__ == '__main__':
    #print(get_screen_set())
    #print(sec_to_h(3667))
    #print(save_game(182, 181, 1, [[33,33,1,1],[44,44,1,-1],[55,55,2,2],[77,77,-2,1],[222,222,1,-2],[133,33,1,1],[144,44,1,-1],[155,55,2,2],[177,77,-2,1],[122,222,1,-2]]))
    #print(save_rec({"9":[1,1],"8":[2,2],"7":[3,3],"6":[4,4],"5":[5,5],\
    #                "4":[11,11],"3":[12,12],"2":[13,13],"1":[14,14],"0":[15,15]}))
    #print(set_check_rec([56,56],))
    print(load_rec())
    #print(save_game(182, 181, 1, [[33,33,1,2],[44,44,1,-1],[55,55,2,2],[77,77,-2,1],[222,222,1,-2]]))
    #print(load_game())

