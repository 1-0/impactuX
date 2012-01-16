#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       menuI.py
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

import pygame, sys, os
from pygame.locals import *
import objects, functions 

####### init section #######
def mainrun(scr_params=((640,480),0,32)):
    
    i_exit=functions.iExit()
    i_run=functions.iRun()
    i_setup=functions.iSetup()
    i_record=functions.iRecord()
    
    ending_play=functions.Ending_play()
    button_press_checking=functions.Button_press_checking()
    
    #r_size=10
    #r_delta=2
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    black=(0, 0, 0)
    
    bgif="."+os.sep+"pic"+os.sep+"bgstart.jpg"
    
    soif1="."+os.sep+"sounds"+os.sep+"s1.ogg"
    
    pygame.init()
    #(640,480),0,32
    sss=scr_params[0]
    mmm=scr_params[1]
    ddd=scr_params[2]
    
    screen=pygame.display.set_mode(sss,mmm,ddd)
    
    background=pygame.image.load(bgif).convert()

    textbuttons=[objects.t_button(285, 40, "Start game", i_run, 20, 5, black, white), \
    objects.t_button(270,90, "Continue game", i_run, 20, 5, black, green), \
    objects.t_button(295,140, "Options", i_setup, 20, 5, black, white), \
    objects.t_button(295,190, "Records", i_record, 20, 5, black, green), \
    objects.t_button(315,240, "EXIT", i_exit, 20, 5, black, red)]
#    objects.t_button(315,240, "EXIT", ending_play, 20, 5, black, red)]
    font1=pygame.font.Font("."+os.sep+"fonts"+os.sep+"LiberationSans-Regular.ttf", 18)
    
    pygame.display.set_caption("ImpactuX Menu")
    
    clock = pygame.time.Clock()
    
    run_now = True

####### main loop section #######
    while run_now:
        clock.tick(30) 
        #t=pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == QUIT:
                ending_play()
                return 0
                
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    run_now=False
                    return 0

            elif event.type == MOUSEBUTTONDOWN:
                x_n0,y_n0=event.pos
                check_tb=button_press_checking(x_n0,y_n0, textbuttons)
                if check_tb[0]:
                    check_tb[1].ch_state(event.type)
    
            elif event.type == MOUSEMOTION:
                x_n0,y_n0=event.pos
                check_tb=button_press_checking(x_n0,y_n0, textbuttons)
                if check_tb[0]:
                    check_tb[1].ch_state(event.type)

            elif event.type == MOUSEBUTTONUP:
                if int(event.button) == 1:
                    x_n0,y_n0=event.pos
                    
                    check_tb=button_press_checking(x_n0,y_n0, textbuttons)
                    if check_tb[0]:
                        check_tb[1].ch_state(event.type)
                        return check_tb[1].doing()
                       
        screen.blit(background, (0,0))
        
        for b_obj in textbuttons:
            b_obj.show_at(screen)
    
        #pygame.display.update()
        pygame.display.flip()
       
if __name__ == '__main__':
    print mainrun()


