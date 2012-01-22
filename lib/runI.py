#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       runI.py
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

import pygame
import os
import objects, functions
from pygame.locals import QUIT, KEYUP, K_ESCAPE, MOUSEBUTTONDOWN, \
MOUSEMOTION, MOUSEBUTTONUP #, FULLSCREEN
from colors import *

def mainrun(scr_params=((640,480),0,32), lvl=0, balls_pos=None, g_time=0, g_score=0):
    """mainrun(scr_params=((640,480),0,32), lvl=0, balls_pos=None, g_time=0, g_score=0) -
    screen of level play scene in ImpactuX"""
    pygame.init()
    
    i_exit=functions.iExit() #button functions
    i_run=functions.iRun()
    i_pause=functions.iPause()
    
    #ending_play=functions.Ending_play()
    button_press_checking=functions.Button_press_checking()
    
    #init vars
    
    f_s = 20 #font size
    b_s = 5 #border size
    
    # white = (255, 255, 255)
    # red = (255, 0, 0)
    # green = (0, 255, 0)
    # blue = (0, 0, 255)
    # yellow = (255, 255, 0)
    # cyan = (0, 255, 255)
    # magenta = (255, 0, 255)
    # black=(0, 0, 0)
    #print lvl
    bgif="."+os.sep+"pic"+os.sep+"bgplay.jpg"
    
    #soif1="."+os.sep+"sounds"+os.sep+"s1.ogg"
    
    pygame.init()
    
    screen=pygame.display.set_mode(scr_params[0], scr_params[1], scr_params[2])
    
    background=pygame.image.load(bgif).convert()


    textlabels = [objects.t_label(530, 10, "ImpactuX", i_exit, 22, 1, RED, None), \
    objects.t_label(540, 40, "Stopped", i_exit, 16, 1, MAGENTA, None), \
    objects.t_label(540, 40, "Score: 0000", i_exit, 16, 1, BLUE, WHITE), \
    objects.t_label(540, 40, "Time: 00:00", i_exit, 16, 1, BLUE, WHITE), \
    objects.t_label(540, 40, "Balls: 00", i_exit, 16, 1, BLUE, WHITE)]
    
    textlabels = objects.WidgetsPack(540, 20, 30, False, textlabels)

    textbuttons = \
    [objects.t_button(55, 430, "Run", i_run, f_s, b_s, MAGENTA, GREEN), \
    objects.t_button(295,430, "Pause", i_pause, f_s, b_s, BLUE, YELLOW), \
    objects.t_button(555,430, "EXIT", i_exit, f_s, b_s, BLACK, RED)]
    
    #t_y=textlabels.height+textlabels.pos_y+100
    t_y=345
    
    textbuttons = objects.WidgetsPack(550, t_y, 45, False, textbuttons)
   
    
    #font1=pygame.font.Font("."+os.sep+"fonts"+os.sep+"LiberationSans-Regular.ttf", 18)
    
    pygame.display.set_caption("ImpactuX run. Level "+str(lvl+1))
    
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
        
        textbuttons.show_at(screen)
        
        textlabels.show_at(screen)

#        for b_obj in textlabels:
#            b_obj.show_at(screen)
    
        #pygame.display.update()
        pygame.display.flip()


if __name__ == '__main__':
    runing = True
    while runing:
        mainrun()
