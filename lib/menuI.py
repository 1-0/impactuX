#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       menuI.py
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
import objects, functions 
from colors import *

####### init section #######
def mainrun(scr_params=((640,480),0,32)):
    """mainrun(scr_params=((640,480),0,32)) - screen of main menu ImpactuX"""
    i_exit = functions.iExit() #button functions
    i_run = functions.iRun()
    i_setup = functions.iSetup()
    i_record = functions.iRecord()
    i_restore = functions.iRestore()
    
    #ending_play=functions.Ending_play()
    button_press_checking=functions.Button_press_checking()
    
    #init vars
    
    f_s = 20 #font size
    b_s = 5 #border size
    
    bgif="."+os.sep+"pic"+os.sep+"bgstart.jpg"
    i_icon="."+os.sep+"pic"+os.sep+"impactuX.png"
    
    #soif1="."+os.sep+"sounds"+os.sep+"s1.ogg"
    
    pygame.init()
    
    screen=pygame.display.set_mode(scr_params[0], scr_params[1], scr_params[2])
    
    background=pygame.image.load(bgif).convert()
    m_icon=pygame.image.load(i_icon).convert_alpha()
    #m_icon=pygame.image.load(i_icon).convert()
    
    textbuttons = \
    [objects.t_button(285, 40, "Start game", i_run, f_s, b_s, BLACK, WHITE), \
    objects.t_button(270,90, "Continue game", i_restore, f_s, b_s, BLACK, GREEN), \
    objects.t_button(295,140, "Options", i_setup, f_s, b_s, BLACK, WHITE), \
    objects.t_button(300,190, "Score", i_record, f_s, b_s, BLACK, GREEN), \
    objects.t_button(305,240, "EXIT", i_exit, f_s, b_s, BLACK, RED)]
    
    textbuttons = objects.WidgetsPack(250, 70, 65, False, textbuttons)
    
    
    #textlabels = [objects.t_label(270, 390, "ImpactuX", i_exit, 32, 1, RED, None),]
    textbuttons.add_wig(objects.t_label(270, 390, "ImpactuX", i_exit, 32, 1, RED, None))
    #objects.t_button(315,240, "EXIT", ending_play, 20, 5, BLACK, red)]

    #font1=pygame.font.Font("."+os.sep+"fonts"+os.sep+"LiberationSans-Regular.ttf", 18)
    
    pygame.display.set_caption("ImpactuX Menu")
    pygame.display.set_icon(m_icon)
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
                check_tb=button_press_checking(x_n0, y_n0, textbuttons.w_list)
                if check_tb[0]:
                    check_tb[1].ch_state(event.type)
    
            elif event.type == MOUSEMOTION:
                x_n0,y_n0=event.pos
                check_tb=button_press_checking(x_n0, y_n0, textbuttons.w_list)
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
        #for b_obj in textbuttons.w_list:
        #    b_obj.show_at(screen)

        #for b_obj in textlabels:
        #    b_obj.show_at(screen)
    
        #pygame.display.update()
        pygame.display.flip()
       
if __name__ == '__main__':
    print mainrun()


