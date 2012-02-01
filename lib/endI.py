#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       endI.py
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
import time
from pygame.locals import QUIT, KEYUP, K_ESCAPE, MOUSEBUTTONDOWN, \
MOUSEMOTION, MOUSEBUTTONUP #, FULLSCREEN
import objects, functions 
from colors import *

def get_res(g_st, l_v=0):
    """get_res(g_st, l_v=0) - getting result param's of end window"""
    l_v += 1
    if g_st=="wingame":
        bgif = "."+os.sep+"pic"+os.sep+"bgwingame.jpg"
        ttt = "Congratulations - You Won!!!"
        ccc = "The End"
    elif g_st=="winlvl":
        bgif = "."+os.sep+"pic"+os.sep+"bgwin.jpg"
        ttt = "Congratulations - you pass to level "+str(l_v)
        ccc = " Level Passed"
    elif g_st=="loose":
        bgif = "."+os.sep+"pic"+os.sep+"bgloose.jpg"
        ttt = "You lose at level "+str(l_v)
        ccc = "Game Over"
    return {"bg":bgif,"txt":ttt,"caption":ccc}

def mainrun(scr_params=((640,480),0,32), game_status="loose",g_score=0, g_time=0, lvl=0):
    """mainrun(scr_params=((640,480),0,32), game_status="lost",g_score=0, g_time=0, g_lvl=0) -
     screen of level ending scene in ImpactuX"""
    i_exit=functions.iExit() #button functions
    i_menu=functions.iMenu()
    
    button_press_checking=functions.Button_press_checking()
    #init vars
    f_s = 20 #font size
    b_s = 5 #border size
    
    end_res = get_res(game_status, lvl)
    
    pygame.init()
    
    screen=pygame.display.set_mode(scr_params[0], scr_params[1], scr_params[2])
    
    background=pygame.image.load(end_res["bg"]).convert()

    textbuttons = [ \
                   objects.t_button(295,430, "Continue", i_menu, f_s, b_s, BLACK, GREEN), \
                   #objects.t_button(555,430, "EXIT", i_exit, f_s, b_s, BLACK, RED) \
                   ]
    
    textbuttons = objects.WidgetsPack(510, 430, 340, True, textbuttons)

    textlabels = [objects.t_label(240, 380, end_res["txt"], i_exit, 28, 1, MAGENTA, None), \
    objects.t_label(270, 290, "ImpactuX", i_exit, 32, 1, RED, None)]
    
    if g_score>0:
        sss = objects.t_label(270, 310, "Score: "+str(g_score), i_exit, 20, 1, CYAN, None)
        textlabels.append(sss)
    textlabels = objects.WidgetsPack(30, 330, 35, False, textlabels)

    pygame.display.set_caption("ImpactuX "+end_res["caption"])
    
    clock = pygame.time.Clock()
    
    ttt = time.time()
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
        
        #for b_obj in textlabels:
        #    b_obj.show_at(screen)
    
        #pygame.display.update()
        n_ttt = time.time()
        if n_ttt-ttt>10:
            #print "+++++++"
            return 0
        
        pygame.display.flip()

if __name__ == '__main__':
    runing = True
    while runing:
        mmm=mainrun()
        runing = (mmm <>"exit")
