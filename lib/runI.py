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
import random
import os
import time
import objects, functions
from pygame.locals import QUIT, KEYUP, K_ESCAPE, MOUSEBUTTONDOWN, \
MOUSEMOTION, MOUSEBUTTONUP #, FULLSCREEN
from colors import *

def mainrun(scr_params=((640,480),0,32), lvl=0, balls_pos=None, g_time=0, g_score=0, n_balls=55):
    """mainrun(scr_params=((640,480),0,32), lvl=0, balls_pos=None, g_time=0, g_score=0) -
    screen of level play scene in ImpactuX"""
    pygame.init()
    
    i_exit=functions.iExit() #button functions
    i_run=functions.iRun()
    i_setup=functions.iSetup()
    
    #ending_play=functions.Ending_play()
    button_press_checking=functions.Button_press_checking()
    
    #init vars
    
    f_s = 20 #font size
    b_s = 5 #border size
    
    bgif="."+os.sep+"pic"+os.sep+"bgplay.jpg"
    
    #soif1="."+os.sep+"sounds"+os.sep+"s1.ogg"
    
    pygame.init()
    
    screen=pygame.display.set_mode(scr_params[0], scr_params[1], scr_params[2])
    
    background=pygame.image.load(bgif).convert()
    
    time_in_game = g_time
    m_time = functions.sec_to_minute(g_time)

    pngs = objects.LoadedObj("."+os.sep+"pic")
    
    bbb=[]
    x_min,y_min,x_max,y_max=10,10,525,470
    dx_min,dy_min,dx_max,dy_max=1,1,10,10
    dxy=30
    if balls_pos:
        n_balls=len(balls_pos)
        for iii in balls_pos:
            bbb.append(objects.AnimationObj(pngs, iii[0], \
                                            iii[1], \
                                            iii[2], \
                                            iii[3], 1, 0,\
                                            iii[4], "rock", 0, \
                                            (x_min, y_min, x_max, y_max), True))
    else:
        for iii in range(n_balls):
            bbb.append(objects.AnimationObj(pngs, random.choice(range(x_min+dxy,x_max-dxy)), \
                                            random.choice(range(y_min+dxy,y_max-dxy)), \
                                            random.choice(range(dx_min,dx_max)), \
                                            random.choice(range(dy_min,dy_max)), 1, 0,\
                                            random.choice(range(-1,1)), "rock", 0, \
                                            (x_min, y_min, x_max, y_max), True))
    
    textlabels = [objects.t_label(530, 10, "ImpactuX", i_exit, 22, 1, RED, None), \
    objects.t_label(540, 40, "Paused", i_exit, 16, 1, MAGENTA, None, "status"), \
    objects.t_label(540, 40, "Level: "+str(lvl+1), i_exit, 16, 1, BLUE, WHITE), \
    objects.t_label(540, 40, "Score: "+str(g_score), i_exit, 16, 1, BLUE, WHITE, "score"), \
    objects.t_label(540, 40, "Time: "+str(m_time[0])+":"+str(m_time[1]), i_exit, 16, 1, BLUE, WHITE, "time"), \
    objects.t_label(540, 40, "Balls: "+str(n_balls), i_exit, 16, 1, BLUE, WHITE, "balls")]
    
    textlabels = objects.WidgetsPack(540, 20, 30, False, textlabels)

    textbuttons = \
    [objects.t_button(55, 430, "Run", i_run, f_s, b_s, MAGENTA, GREEN, "run"), \
    objects.t_button(295,430, "Stop", i_setup, f_s, b_s, BLUE, YELLOW, ), \
    objects.t_button(555,430, "EXIT", i_exit, f_s, b_s, BLACK, RED)]
    
    #t_y=textlabels.height+textlabels.pos_y+100
    t_y=345
    
    textbuttons = objects.WidgetsPack(560, t_y, 45, False, textbuttons)
    
    #font1=pygame.font.Font("."+os.sep+"fonts"+os.sep+"LiberationSans-Regular.ttf", 18)
    allSprites = pygame.sprite.Group(bbb)
    print allSprites
    
    pygame.display.set_caption("ImpactuX run. Level "+str(lvl+1))
    clock = pygame.time.Clock()
    run_now = True
    start_runing = False
    last_time = time.time()

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
                        ddd = check_tb[1].doing()
                        if ddd == "run":
                            start_runing=not(start_runing)
                            if start_runing:
                                textbuttons.set_named_obj_str("run", "Pause")
                                textlabels.set_named_obj_str("status", "Running")
                                for o_b in bbb:
                                    o_b.stopped=False
                            else:
                                textbuttons.set_named_obj_str("run", "Run")
                                textlabels.set_named_obj_str("status", "Paused")
                                for o_b in bbb:
                                    o_b.stopped=True
                            last_time = time.clock()
                            #print start_runing
                        else:
                            return ddd
        if start_runing:
            n_time = time.time()
            d_time = n_time-last_time
            if d_time>=1:
                last_time = n_time+(d_time- int(d_time))
                time_in_game += 1
                g_score += 1
                m_time = functions.sec_to_minute(time_in_game)
                textlabels.set_named_obj_str("score", "Score: "+str(g_score))
                textlabels.set_named_obj_str("time", "Time: "+str(m_time[0])+":"+str(m_time[1]))
        
        #showing objects at screen
        screen.blit(background, (0,0))
        
        allSprites.update()
        allSprites.draw(screen)
        
        textbuttons.show_at(screen)
        textlabels.show_at(screen)

        
        #pygame.display.update()
        pygame.display.flip()


if __name__ == '__main__':
    runing = True
    while runing:
        mainrun()
