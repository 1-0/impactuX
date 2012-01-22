#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       storyI.py
#       impactuX - tuX collision game
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

import pygame, os
from pygame.locals import QUIT, KEYUP, K_ESCAPE, MOUSEBUTTONDOWN, MOUSEMOTION, MOUSEBUTTONUP #, FULLSCREEN
import objects, functions 


def get_text_lvl(lvl):
    """get_text_lvl(lvl) - geting story text for lvl"""
    if lvl==0:
        ttt="Tux protects the MP3-player from the fly(Walk)man."
    elif lvl==1:
        ttt="Tux protects the smartphone from the white(Black)berry."
    elif lvl==2:
        ttt="Tux protects the tablet from the pine(apple)."
    elif lvl==3:
        ttt="Tux protects the notebook from the SM(MS)allDOS."
    elif lvl==4:
        ttt="Tux protects the desktop from the (Win)Dors."
    elif lvl==5:
        ttt="Tux protects the car from the axi(O)s(/2)."
    elif lvl==6:
        ttt="Tux protects the server from the ocsic(cisco)."
    elif lvl==7:
        ttt="Tux protects the train from the AI(X)DS."
    elif lvl==8:
        ttt="Tux protects the airplane from the moon(sol)aris."
    elif lvl==9:
        ttt="Tux protects the NPP from the bmx(qnx)."
    ttt = "Level - "+str(lvl+1)+" - "+ttt
    return ttt
        
    

def mainrun(scr_params=((640,480),0,32), lvl=0):
    """mainrun(scr_params=((640,480),0,32), lvl=0) - screen of lvl story 
    scene in ImpactuX"""
    i_exit=functions.iExit() #button functions
    i_run=functions.iRun()
    i_setup=functions.iSetup()
    
    #ending_play=functions.Ending_play()
    button_press_checking=functions.Button_press_checking()
    
    #init vars
    
    f_s = 20 #font size
    b_s = 5 #border size
    
    white = (255, 255, 255)
    red = (255, 0, 0)
    #green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    black=(0, 0, 0)
    #print lvl
    bgif="."+os.sep+"pic"+os.sep+"bg_story_"+str(lvl)+".jpg"
    
    #soif1="."+os.sep+"sounds"+os.sep+"s1.ogg"
    
    l_text = get_text_lvl(lvl)
    
    pygame.init()
    
    screen=pygame.display.set_mode(scr_params[0], scr_params[1], scr_params[2])
    
    background=pygame.image.load(bgif).convert()

    textbuttons = \
    [objects.t_button(55, 430, "Start round", i_run, f_s, b_s, black, white), \
    objects.t_button(295,430, "Cancel", i_setup, f_s, b_s, white, red), \
    objects.t_button(555,430, "EXIT", i_exit, f_s, b_s, black, red)]
    
    textbuttons = objects.WidgetsPack(30, 430, 240, True, textbuttons)

    textlabels = [objects.t_label(20, 380, l_text, i_exit, 16, 1, blue, yellow), \
    objects.t_label(270, 230, "ImpactuX", i_exit, 32, 1, red, None)]

    
    
    #font1=pygame.font.Font("."+os.sep+"fonts"+os.sep+"LiberationSans-Regular.ttf", 18)
    
    pygame.display.set_caption("ImpactuX story "+str(lvl+1))
    
    clock = pygame.time.Clock()
    
    run_now = True

####### main loop section #######
    while run_now:
        clock.tick(30) 
        #t=pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == QUIT:
                i_exit()
                #ending_play()
                return i_exit()
                
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    run_now=False
                    return i_exit()

            elif event.type == MOUSEBUTTONDOWN:
                x_n0,y_n0=event.pos
                check_tb=button_press_checking(x_n0,y_n0, textbuttons.w_list)
                if check_tb[0]:
                    check_tb[1].ch_state(event.type)
    
            elif event.type == MOUSEMOTION:
                x_n0, y_n0=event.pos
                check_tb=button_press_checking(x_n0,y_n0, textbuttons.w_list)
                if check_tb[0]:
                    check_tb[1].ch_state(event.type)

            elif event.type == MOUSEBUTTONUP:
                if int(event.button) == 1:
                    x_n0,y_n0=event.pos
                    
                    check_tb=button_press_checking(x_n0, y_n0, textbuttons.w_list)
                    if check_tb[0]:
                        check_tb[1].ch_state(event.type)
                        return check_tb[1].doing()
                       
        screen.blit(background, (0,0))
        
        #textbuttons.show_at(screen)
        
        textbuttons.show_at(screen)
        
        #textlabels.show_at(screen)
        #for b_obj in textbuttons.w_list:
            #b_obj.show_at(screen)

        for b_obj in textlabels:
            b_obj.show_at(screen)
    
        #pygame.display.update()
        pygame.display.flip()

if __name__ == '__main__':
    runing = True
    while runing:
        mainrun()
