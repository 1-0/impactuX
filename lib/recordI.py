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

import pygame, os
from pygame.locals import QUIT, KEYUP, K_ESCAPE, MOUSEBUTTONDOWN, \
MOUSEMOTION, MOUSEBUTTONUP #, FULLSCREEN
import lib.objects as objects
import lib.functions as functions

from lib.colors import *

def set_labels(t_score, t_time, l_score, l_time):
    i_exit = functions.iExit()
    if l_time:
        sss = objects.t_label(270, 310, "last level time - "+str(l_time), i_exit, 16, 1, MAGENTA, WHITE)
        t_time.add_wig(sss)
    
    if l_score:
        sss = objects.t_label(270, 310, "last score - "+str(l_score), i_exit, 16, 1, RED, WHITE)
        t_score.add_wig(sss)
        
    rrr=functions.load_rec()
    
    kkk=rrr.keys()
    kkk.sort()
    
    for iii in kkk:
        vvv=rrr[iii]
        sss = objects.t_label(270, 310, str(vvv[1]), i_exit, 16, 1, MAGENTA, YELLOW)
        t_time.add_wig(sss)
        sss = objects.t_label(270, 310, str(vvv[0]), i_exit, 16, 1, YELLOW, BLUE)
        t_score.add_wig(sss)
    
def mainrun(scr_params=((640,480),0,32),last_time=None, last_score=None):
    """mainrun(scr_params=((640,480),0,32), lvl=0 g_score=0) - screen of level story 
    scene in ImpactuX"""
    i_menu=functions.iMenu()
    i_exit = functions.iExit() #button functions
    #ending_play=functions.Ending_play()
    button_press_checking=functions.Button_press_checking()
    #init vars
    f_s = 20 #font size
    b_s = 5 #border size
    bgif="."+os.sep+"pic"+os.sep+"bgrec.jpg"

    pygame.init()
    
    pygame.display.set_caption("ImpactuX Records")
    screen=pygame.display.set_mode(scr_params[0], scr_params[1], scr_params[2])
    background=pygame.image.load(bgif).convert()
    textbuttons = \
    [\
    objects.t_button(295,430, "Continue", i_menu, f_s, b_s, BLACK, GREEN), \
    ]
    textbuttons = objects.WidgetsPack(30, 430, 240, True, textbuttons)
    textlabels = [\
                  objects.t_label(20, 20, "ImpactuX Best Score", i_exit, 32, 1, RED, None), \
                  ]
    textlabels = objects.WidgetsPack(150, 20, 240, True, textlabels)
    text_score = [\
                  objects.t_label(200, 20, "Score:", i_exit, 28, 1, GREEN, None), \
                  ]
    text_score = objects.WidgetsPack(170, 60, 30, False, text_score)
    text_time = [\
                  objects.t_label(200, 20, "Time:", i_exit, 28, 1, GREEN, None), \
                  ]
    text_time = objects.WidgetsPack(350, 60, 30, False, text_time)
    set_labels(text_score, text_time, last_time, last_score)

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
        textlabels.show_at(screen)
        text_score.show_at(screen)
        text_time.show_at(screen)
    
        #pygame.display.update()
        pygame.display.flip()

if __name__ == '__main__':
    runing = True
    while runing:
        mmm=mainrun()
        runing = (mmm!="exit")
