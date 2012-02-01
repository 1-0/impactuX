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
import objects, functions 

from colors import *

def mainrun(scr_params=((640,480),0,32)):
    """mainrun(scr_params=((640,480),0,32), lvl=0 g_score=0) - screen of level story 
    scene in ImpactuX"""
    i_exit=functions.iExit() #button functions
    i_run=functions.iRun()
    i_setup=functions.iSetup()
    i_restore=functions.iRestore()
    i_record=functions.iRecord()

    
    #ending_play=functions.Ending_play()
    button_press_checking=functions.Button_press_checking()
    
    #init vars
    f_s = 20 #font size
    b_s = 5 #border size
    
    bgif="."+os.sep+"pic"+os.sep+"bgset.jpg"

    pygame.init()
    
    screen=pygame.display.set_mode(scr_params[0], scr_params[1], scr_params[2])
    
    background=pygame.image.load(bgif).convert()

    
    m_list=pygame.display.list_modes()
    m_list.sort()
    m_index=m_list.index(scr_params[0])


    textbuttons = \
    [objects.t_button(55, 430, "Save", i_run, f_s, b_s, BLACK, GREEN), \
    objects.t_button(295,430, "Cancel", i_setup, f_s, b_s, WHITE, RED), \
    objects.t_button(555,430, "EXIT", i_exit, f_s, b_s, BLACK, RED)]
    
    textbuttons = objects.WidgetsPack(30, 430, 250, True, textbuttons)
    if scr_params[1]==0:
        b1_l="Set Fullscreen"
    else:
        b1_l="Set Windowed"
        
    if m_index>=(len(m_list)-1):
        m_next=0
    else:
        m_next=m_index+1
    
    buttons_sets = \
    [\
     objects.t_button(55, 430, b1_l, i_restore, f_s, b_s, BLACK, CYAN,"mode"), \
     objects.t_button(57, 430, "Set: "+str(m_list[m_next]), i_record, f_s, b_s, BLACK, CYAN,"resolution"), \
     ]
    buttons_sets = objects.WidgetsPack(250, 150, 50, False, buttons_sets)

    textlabels = [objects.t_label(270, 230, "ImpactuX", i_exit, 32, 1, RED, None),\
                  objects.t_label(20, 380, "Options", i_exit, 22, 1, GREEN, None)\
                  ]
    textlabels = objects.WidgetsPack(250, 30, 30, False, textlabels)
        #font1=pygame.font.Font("."+os.sep+"fonts"+os.sep+"LiberationSans-Regular.ttf", 18)
    pygame.display.set_caption("ImpactuX settings")
    clock = pygame.time.Clock()
    run_now = True
    n_scr_param=scr_params[1]
    n_scr_res=scr_params[0]

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
                check_tb=button_press_checking(x_n0,y_n0, buttons_sets.w_list)
                if check_tb[0]:
                    check_tb[1].ch_state(event.type)
    
            elif event.type == MOUSEMOTION:
                x_n0, y_n0=event.pos
                check_tb=button_press_checking(x_n0,y_n0, textbuttons.w_list)
                if check_tb[0]:
                    check_tb[1].ch_state(event.type)
                check_tb=button_press_checking(x_n0,y_n0, buttons_sets.w_list)
                if check_tb[0]:
                    check_tb[1].ch_state(event.type)

            elif event.type == MOUSEBUTTONUP:
                if int(event.button) == 1:
                    x_n0,y_n0=event.pos
                    
                    check_tb=button_press_checking(x_n0, y_n0, textbuttons.w_list)
                    if check_tb[0]:
                        check_tb[1].ch_state(event.type)
                        ddd = check_tb[1].doing()
                        if ddd == "run":
                            functions.save_set(game_dict={"screen_width":n_scr_res[0],\
                                                          "screen_height":n_scr_res[1],\
                                                          "screen_flags":n_scr_param,\
                                                          "screen_depth":scr_params[2]}, \
                                               g_file="conf_game.ini", \
                                               g_section="screen")
                        return ddd
                    check_tb=button_press_checking(x_n0,y_n0, buttons_sets.w_list)
                    if check_tb[0]:
                        check_tb[1].ch_state(event.type)
                        ddd = check_tb[1].doing()
                        if ddd == "restore":
                            if n_scr_param==0:
                                buttons_sets.set_named_obj_str("mode", "Set Windowed")
                                n_scr_param='"fullscreen"'
                                
                            else:
                                buttons_sets.set_named_obj_str("mode", "Set Fullscreen")
                                n_scr_param=0
                        elif ddd=="record":
                            m_index=m_next
                            n_scr_res=m_list[m_index]
                            if m_index>=(len(m_list)-1):
                                m_next=0
                            else:
                                m_next=m_index+1
                            buttons_sets.set_named_obj_str("resolution", "Set: "+str(m_list[m_next]))

        screen.blit(background, (0,0))
        textbuttons.show_at(screen)
        textlabels.show_at(screen)
        buttons_sets.show_at(screen)
    
        pygame.display.flip()

if __name__ == '__main__':
    runing = True
    while runing:
        mmm=mainrun()
        runing = (mmm <>"exit")
