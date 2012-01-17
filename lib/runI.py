#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       runI.py
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

import pygame
import os
import objects

def mainrun(scr_params=((640,480),0,32), lvl=0, balls_pos=None, g_time=0, g_score=0):
    """mainrun(scr_params=((640,480),0,32), lvl=0, balls_pos=None, g_time=0, g_score=0) -
    screen of lvl play scene in ImpactuX"""
    pygame.init()
    pngs=objects.LoadedObj("."+os.sep+"pic")
    screen = pygame.display.set_mode(scr_params[0], scr_params[1], scr_params[2])
    #take background
    bgif="."+os.sep+"pic"+os.sep+"bgplay.jpg"
    background=pygame.image.load(bgif).convert()
    #take coursor - device img
    moif1="."+os.sep+"pic"+os.sep+"ball1.png"
    mouse_c1=pygame.image.load(moif1).convert_alpha()

    exit_var = {"exit":True}
    
    clock = pygame.time.Clock()
    run_now = True
    # main loop
    while run_now:
        clock.tick(30) 
        #t=pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == QUIT:
                run_now = False
                #ending_play()
                pygame.mouse.set_visible(True)
                return exit_var
                
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    run_now = False
                    #ending_play()
                    return exit_var
                    pygame.mouse.set_visible(True)
    
            elif event.type == MOUSEBUTTONUP:
                if int(event.button) == 1:
                    x_n0,y_n0=event.pos
                    x_n = x_n0 - deltax(coursore_type)
                    y_n = y_n0 - deltay(coursore_type)
####                    
                    check_tb=button_press_checking(x_n0, y_n0, textbuttons)
                    
                    if check_tb[0]:
                        #print 111
                        check_tb[1].doing(points)
        
                    elif x_n0>r_border:
                        if y_n0<d_new:
                            check_b=button_press_checking(x_n0,y_n0, buttons)
            
                            if check_b[0]:
                                coursore_type=check_b[1].picture
                                pygame.mouse.set_visible(False)
                                pygame.mixer.music.load(soif2)
                                pygame.mixer.music.play(0, 0.0)
        
                            else:
                                coursore_type=mouse_c0
                                pygame.mouse.set_visible(True)
                                pygame.mixer.music.load(soif5)
                                pygame.mixer.music.play(0, 0.0)
                        else:
                            pygame.mixer.music.load(soif3)
                            pygame.mixer.music.play(0, 0.0)
    #                        pygame.mixer.music.play(points.__len__(), 0.0)
                            
                            points=[]
                            money_sum=50
    
                            
                            coursore_type=mouse_c0
                            pygame.mouse.set_visible(True)
        
                    elif coursore_type<>mouse_c0:
                        if not(let_addin_press_checking(x_n, y_n, points, coursore_type, mouse_c0)):
                            points.append(objects.tow_o((x_n,y_n),coursore_type))
                            
                            pygame.mixer.music.load(soif1)
                            pygame.mixer.music.play(0, 0.0)
                            money_sum-=1
                         
        screen.blit(background, (0,0))



if __name__ == '__main__':
    runing = True
    while runing:
        mainrun()
