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
import lib.sqcheck as sqcheck
import lib.objects as objects
import lib.functions as functions
from pygame.locals import QUIT, KEYUP, K_ESCAPE, MOUSEBUTTONDOWN, \
MOUSEMOTION, MOUSEBUTTONUP, K_p, K_PAUSE, FULLSCREEN
from lib.colors import *

class game_runing:
    """game_runing - class of running game scene for playing"""
    def __init__(self, scr_params=((640,480),0,32),\
                 lvl=0, balls_pos=None, g_time=0,\
                 g_score=0, n_balls=5):
        self.start_inits()
        self.score = g_score
        self.time = g_time
        self.level = lvl
        #screen start param's i.e. size, modee
        scr_size=scr_params[0]
        self.height = scr_size[1]
        self.width = scr_size[0]
        self.flags = scr_params[1]
        self.depth = scr_params[2]
        self.screen = pygame.display.set_mode(scr_params[0], \
                                              scr_params[1], \
                                              scr_params[2])
        #ball start param's i.e. position range, speed range
        self.x_min = 20
        self.y_min = 20
        self.x_max = 510
        self.y_max = 455
        self.dd_min = 1
        self.dd_max = lvl+2
        self.dxy = 60
        self.balls = []
        self.balls_count = 0
        self.pictures = objects.LoadedObj("."+os.sep+"pic")
        self.sounds = objects.LoadedSounds(("."+os.sep+"sounds"), "ogg")
        self.set_balls(balls_pos, n_balls)
        
        self.init_labels()
        self.init_buttons()
        self.end_inits()
        
    def start_inits(self, bg_name="bgplay.jpg"):
        pygame.init()
        pygame.mouse.set_visible(False)
        bgif="."+os.sep+"pic"+os.sep+bg_name
        self.background=pygame.image.load(bgif).convert()
        
    def end_inits(self):
        pass

    def init_labels(self):
        i_exit=None
        m_time = functions.sec_to_minute(self.time)
        textlabels = [objects.t_label(530, 10, "ImpactuX", i_exit, 22, 1, RED, None), \
            objects.t_label(540, 40, "Paused", i_exit, 16, 1, MAGENTA, None, "status"), \
            objects.t_label(540, 40, "Level: "+str(self.level+1), i_exit, 16, 1, BLUE, WHITE), \
            objects.t_label(540, 40, "Score: "+str(self.score), i_exit, 16, 1, BLUE, WHITE, "score"), \
            objects.t_label(540, 40, "Time: "+str(m_time[0])+":"+str(m_time[1]), i_exit, 16, 1, BLUE, WHITE, "time"), \
            objects.t_label(540, 40, "Balls: "+str(self.balls_count), i_exit, 16, 1, BLUE, WHITE, "balls")]
    
        self.labels = objects.WidgetsPack(540, 20, 30, False, textlabels)
    
    def init_buttons(self):
        i_exit=functions.iExit() #button functions
        i_run=functions.iRun()
        i_menu=functions.iMenu()
        f_s = 20 #font size
        b_s = 5 #border size
        textbuttons = [objects.t_button(55, 430, "Run", i_run, f_s, b_s, MAGENTA, GREEN, "run"), \
            objects.t_button(295,430, "Stop", i_menu, f_s, b_s, BLUE, YELLOW, ), \
            objects.t_button(555,430, "EXIT", i_exit, f_s, b_s, BLACK, RED)]
        #t_y=textlabels.height+textlabels.pos_y+100
        t_y=345
        self.buttons = objects.WidgetsPack(560, t_y, 45, False, textbuttons)
    
    def set_balls(self, b_params, num_balls):
        """set_balls(self, b_params, new_balls) - 
                 adding start balls to balls list"""
        if b_params:
            for iii in b_params:
                self.add_ball(ball_params=iii)
        else:
            for iii in range(num_balls):
                self.add_random_ball()

    def add_ball(self, ball_params, ball_name="rock", \
                 is_stopped=True, \
                 sound_name="impactuX_click1"):
        """add_ball(self, ball_params, ball_name="rock", \
                 is_stopped=True, \
                 sound_name="impactuX_click1") - 
                 adding 1 ball to balls list"""
        n_ball = objects.AnimationObj(self.pictures, \
                                ball_params[0], \
                                ball_params[1], \
                                ball_params[2], \
                                ball_params[3], 1, 0,\
                                objects.dsign(ball_params[2]), "rock", 0, \
                                (self.x_min, self.y_min, \
                                 self.x_max, self.y_max), \
                                is_stopped, \
                                sound_name, self.sounds)
        self.balls.append(n_ball)
        self.balls_count += 1
        self.allSprites = pygame.sprite.Group(self.balls)

        
    def add_random_ball(self, num_balls, ball_name="rock", \
                 is_stopped=True, \
                 sound_name="impactuX_click1"):
        """add_random_ball(self, num_balls, ball_name="rock", \
                 is_stopped=True, \
                 sound_name="impactuX_click1") - 
                 adding 1 random ball to balls list"""
        new_rand_params=(random.choice(range(self.x_min+self.dxy,self.x_max-self.dxy)), \
                                    random.choice(range(self.y_min+self.dxy,self.y_max-self.dxy)), \
                                    random.choice([-1,1])*random.choice(range(self.dd_min,self.dd_max)), \
                                    random.choice([-1,1])*random.choice(range(self.dd_min,self.dd_max)))
        self.add_ball(new_rand_params, \
                      objects.dsign(new_rand_params[2]), "rock", 0, \
                                (self.x_min, self.y_min, \
                                 self.x_max, self.y_max), \
                                is_stopped, \
                                sound_name, self.sounds)
        
def return_vars(score_g, time_g=0, balls_g=None, loose_g=False, win_g=False, exit_g=False, winlvl_g=False, level_g=0):
    #return {"loose":False, "time":time_in_game, "score":g_score, "win":False, "exit":True}
    all_ball=[]
    if balls_g:
        for b_1 in balls_g:
            all_ball.append([b_1.pos_x, b_1.pos_y, b_1.dx, b_1.dy])
    else:
        all_ball=None
        
    return {"loose":loose_g, "time":time_g, "score":score_g, \
            "wingame":win_g, "exit":exit_g, "balls":all_ball, \
            "winlvl":winlvl_g, "level":level_g}

def mainrun(scr_params=((640,480),0,32), lvl=0, balls_pos=None, g_time=0, g_score=0, n_balls=5):
    """mainrun(scr_params=((640,480),0,32), lvl=0, balls_pos=None, g_time=0, g_score=0) -
    screen of level play scene in ImpactuX"""
    pygame.init()
    
    i_exit=functions.iExit() #button functions
    i_run=functions.iRun()
    i_menu=functions.iMenu()
    
    #ending_play=functions.Ending_play()
    button_press_checking=functions.Button_press_checking()
    
    #init vars
    
    f_s = 20 #font size
    b_s = 5 #border size
    
    bgif="."+os.sep+"pic"+os.sep+"bgplay.jpg"
    #pygame.init()
    snd = objects.LoadedSounds(("."+os.sep+"sounds"), "ogg")
    #soif1="."+os.sep+"sounds"+os.sep+"s1.ogg"
    soif1="impactuX_click1"
    soif2="impactuX_click2"
    
    screen=pygame.display.set_mode(scr_params[0], scr_params[1], scr_params[2])
    
    pygame.mouse.set_visible(False)
    
    moif0="."+os.sep+"pic"+os.sep+"impactuX1.png"
    moif1="."+os.sep+"pic"+os.sep+"coursorI.png"
    mouse_c0=pygame.image.load(moif0).convert_alpha()
    mouse_c1=pygame.image.load(moif1).convert_alpha()
    coursore_type = mouse_c0
    coursore_t2 = mouse_c1
    c_t2 = True
    #soif1="."+os.sep+"sounds"+os.sep+"s1.ogg"
    
    background=pygame.image.load(bgif).convert()
    
    time_in_game = g_time
    m_time = functions.sec_to_minute(g_time)

    pngs = objects.LoadedObj("."+os.sep+"pic")
    
    bbb=[]
    x_min, y_min, x_max, y_max = 20, 20, 510, 455
    dx_min, dy_min, dx_max, dy_max = 1, 1, 2+lvl, lvl+2
    dxy = 60
    if balls_pos:
        n_balls=len(balls_pos)
        for iii in balls_pos:
            bbb.append(objects.AnimationObj(pngs, iii[0], \
                                            iii[1], \
                                            iii[2], \
                                            iii[3], 1, 0,\
                                            objects.dsign(iii[2]), "rock", 0, \
                                            (x_min, y_min, x_max, y_max), True, soif1, snd))
    else:
        for iii in range(n_balls):
            corrupted_b = True
            sign_dx=random.choice([-1,1])
            while corrupted_b:
                bbb1=objects.AnimationObj(pngs, random.choice(range(x_min+dxy,x_max-dxy)), \
                                            random.choice(range(y_min+dxy,y_max-dxy)), \
                                            sign_dx*random.choice(range(dx_min,dx_max)), \
                                            random.choice([-1,1])*random.choice(range(dy_min,dy_max)), \
                                            1, 0, sign_dx, "rock", 0, \
                                            (x_min, y_min, x_max, y_max), True, soif1, snd)
                corrupted_b = bbb1.is_impacted_list(bbb)
            
            bbb.append(bbb1)
    
    textlabels = [objects.t_label(530, 10, "ImpactuX", i_exit, 22, 1, RED, None), \
    objects.t_label(540, 40, "Paused", i_exit, 16, 1, MAGENTA, None, "status"), \
    objects.t_label(540, 40, "Level: "+str(lvl+1), i_exit, 16, 1, BLUE, WHITE), \
    objects.t_label(540, 40, "Score: "+str(g_score), i_exit, 16, 1, BLUE, WHITE, "score"), \
    objects.t_label(540, 40, "Time: "+str(m_time[0])+":"+str(m_time[1]), i_exit, 16, 1, BLUE, WHITE, "time"), \
    objects.t_label(540, 40, "Balls: "+str(n_balls), i_exit, 16, 1, BLUE, WHITE, "balls")]
    
    textlabels = objects.WidgetsPack(540, 20, 30, False, textlabels)

    textbuttons = \
    [objects.t_button(55, 430, "Run", i_run, f_s, b_s, MAGENTA, GREEN, "run"), \
    objects.t_button(295,430, "Stop", i_menu, f_s, b_s, BLUE, YELLOW, ), \
    objects.t_button(555,430, "EXIT", i_exit, f_s, b_s, BLACK, RED)]
    
    #t_y=textlabels.height+textlabels.pos_y+100
    t_y=345
    
    textbuttons = objects.WidgetsPack(560, t_y, 45, False, textbuttons)
    
    #font1=pygame.font.Font("."+os.sep+"fonts"+os.sep+"LiberationSans-Regular.ttf", 18)
    allSprites = pygame.sprite.Group(bbb)
    #print allSprites
    
    pygame.display.set_caption("ImpactuX run. Level "+str(lvl+1))
    clock = pygame.time.Clock()
    run_now = True
    start_runing = False
    last_time = time.time()
    c_xxx, c_yyy = x_max/2, y_max/2
    x_n0, y_n0 = c_xxx, c_yyy
#    c_rrr = coursore_type.get_height()/2
    c_rrr0 = coursore_type.get_height()
    c_rrr = coursore_type.get_height()/2
    #c_xxx, c_yyy = 0, 0

####### main loop section #######
    while run_now:
        clock.tick(50) 
        #t=pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == QUIT:
                #i_exit()
                #ending_play()
                #return i_exit()
                pygame.mouse.set_visible(True)
                return "exit"
                #return return_vars(score_g=g_score, time_g=time_in_game, balls_g=bbb, exit_g=True)
                
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.mouse.set_visible(True)
                    return return_vars(score_g=g_score, time_g=time_in_game, balls_g=bbb, exit_g=True)
                    #return {"loose":False, "time":time_in_game, "score":g_score, "win":False, "exit":True}
                elif event.key==K_p or event.key==K_PAUSE:
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
                    last_time = time.perf_counter()

            elif event.type == MOUSEBUTTONDOWN:
                x_n0,y_n0=event.pos
                check_tb=button_press_checking(x_n0,y_n0, textbuttons.w_list)
                if check_tb[0]:
                    check_tb[1].ch_state(event.type)
    
            elif event.type == MOUSEMOTION:
                
                #c_xxx, c_yyy = event.pos
                #x_n0, y_n0=c_xxx, c_yyy
                x_n0, y_n0=event.pos
                if x_n0>x_max - c_rrr0+20:
                    c_t2=True
                    
                else:
                    c_t2=False
                    
                check_tb=button_press_checking(x_n0,y_n0, textbuttons.w_list)
                if check_tb[0]:
                    check_tb[1].ch_state(event.type)
                if x_n0<(x_max-c_rrr0+20):
                    if 2<x_n0:
                        c_xxx = x_n0
                    else:
                        c_xxx = 2
                else:
                    c_xxx = x_max-c_rrr0+20
                    c_t2=True
                if y_n0<(y_max-mouse_c0.get_height()+20):
                    if 2<y_n0:
                        c_yyy = y_n0
                    else:
                        c_yyy = 2
                else:
                    c_yyy = y_max-mouse_c0.get_height()+20

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
                            last_time = time.perf_counter()
                            #print start_runing
                        elif ddd == "exit":
                            #print "Exit"
                            pygame.mouse.set_visible(True)
                            return return_vars(score_g=g_score, time_g=time_in_game, balls_g=bbb, exit_g=True, level_g=lvl)
                        elif ddd == "menu":
                            #print "Setup"
                            pygame.mouse.set_visible(True)
                            return return_vars(score_g=g_score, time_g=time_in_game, balls_g=bbb, level_g=lvl)
        if start_runing:
            n_time = time.time()
            d_time = n_time-last_time
            if d_time>=1:
                last_time = n_time+(d_time- int(d_time))
                time_in_game += 1
                g_score += (1+lvl)
                m_time = functions.sec_to_minute(time_in_game)
                textlabels.set_named_obj_str("score", "Score: "+str(g_score))
                textlabels.set_named_obj_str("time", "Time: "+str(m_time[0])+":"+str(m_time[1]))
                if ((time_in_game/30.0)-int(time_in_game/30))==0:
                    if n_balls>9:
                        pygame.mouse.set_visible(True)
                        return return_vars(score_g=g_score, time_g=time_in_game, balls_g=bbb, win_g=(lvl==9), winlvl_g=True, level_g=lvl)
                    sign_dx=random.choice([-1,1])
                    bbb1=objects.AnimationObj(pngs, random.choice(range(x_min+dxy,x_max-dxy)), \
                                            random.choice(range(y_min+dxy,y_max-dxy)), \
                                            sign_dx*random.choice(range(dx_min,dx_max)), \
                                            random.choice([-1,1])*random.choice(range(dy_min,dy_max)), \
                                            .1, 0, sign_dx, "rock", 300, \
                                            (x_min, y_min, x_max, y_max), False, soif1, snd)
                    bbb.append(bbb1)
                    n_balls = len(bbb)
                    textlabels.set_named_obj_str("balls", "Balls: "+str(n_balls))
                    allSprites = pygame.sprite.Group(bbb)
                    
        if start_runing:
            for b_1 in bbb:
                ch_loste = sqcheck.CheckRound(c_xxx+c_rrr, c_yyy+c_rrr, c_rrr, b_1.pos_x, b_1.pos_y, b_1.radius)
                ch_loste = (ch_loste and b_1.runing)
                if ch_loste:
                    snd.playsnd(soif2)
                    #pygame.mixer.quit()
                    pygame.mouse.set_visible(True)
                    return return_vars(score_g=g_score, time_g=time_in_game, balls_g=bbb, loose_g=True, level_g=lvl)
        #showing objects at screen
        screen.blit(background, (0,0))
        
        allSprites.update()
        allSprites.draw(screen)
        
        textbuttons.show_at(screen)
        textlabels.show_at(screen)

        screen.blit(coursore_type,(c_xxx, c_yyy))
        if c_t2:
            screen.blit(coursore_t2,(x_n0, y_n0))
        #pygame.display.update()
        pygame.display.flip()


if __name__ == '__main__':
    runing = True
    while runing:
        mmm=mainrun()
        runing = (mmm!="exit")
