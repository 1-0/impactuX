#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       objects.py
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

#import copy
#import math
import time
import pygame, os
import sqcheck
import impact
#import functions 
from pygame.locals import QUIT, KEYUP, K_ESCAPE, MOUSEBUTTONDOWN, \
MOUSEMOTION, MOUSEBUTTONUP, KEYDOWN #, FULLSCREEN

def dsign(x):
    if x >= 0: 
        return 1
    else: 
        return -1

class RectObjSet():
    """RectObjSet() - class to use rectongle set of objects to check events and update"""
    def __init__(self, pos_x, pos_y, size_x, size_y, picname="rock", start_obj_list=[]):
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.size_x=size_x
        self.size_y=size_y

        self.obj_list=start_obj_list
        
        self.animation=AnimationO(start_obj_list, pos_x, pos_y, dx=10,dy=5, delay=1, fff=0, direct=1, picname="rock")

    def add_obj(self, new_obj):
        if self.check_in(new_obj.pos_x, new_obj.pos_y):
            self.obj_list.append(new_obj)
            return True
        else:
            return False


    def update(self):
        self.animation.update()
        for ooo in self.obj_list:
            ooo.update
                
    def check_in(self, p_x, p_y):
        n_x = p_x - self.pos_x
        n_y = p_y - self.pos_y
        
        if (((n_x>=0) and (n_x<=self.size_x)) and ((n_y>=0) and (n_y<=self.size_y))):
            return True
        else:
            return False
            
    def check_run(self, p_x, p_y, event=[]):
        for ooo in self.obj_list:
            if ooo.check_in(p_x, p_y):
                ooo.run(event)

class AnimationObj(pygame.sprite.Sprite):
    """AnimationObj() - class to use animated objects on sprites"""
    def __init__(self, listpng, pos_x=111, pos_y=111, dx=10, dy=5,\
                  delay=1, fff=0, direct=1, picname="rock", \
                  starting_time=0, borders=(25,25,615,455), stopped = True,
                  climb_sound_file=None, s_hip=None):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.time_to_start = starting_time
        self.stopped = stopped
        self.init_time = time.time()
        if starting_time==0:
            self.runing = True
        else:
            self.runing = False

        self.picname=picname
        self.loadImages(listpng)
        self.image = self.imageStand
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.frame = fff
        # increase delay value to slow down animation even more
        self.delay = delay
        self.pause = 0
        
        self.xmin=borders[0]
        self.ymin=borders[1]
        self.xmax=borders[2]
        self.ymax=borders[3]
        self.pos_x=pos_x
        self.dx=dx
        self.pos_y=pos_y
        self.dy = dy
        self.new_dx = None
        self.new_dy = None

#        self.direct = direct
        self.direct = dsign(self.dx)
        self.impacts = 0
        
        if climb_sound_file:
            self.set_sound(climb_sound_file, s_hip)
            
    def set_sound (self, s_file, son_hip):
        self.sound_name=s_file
        self.sound_hip=son_hip
        
    def play_sound(self):
        if self.sound_name:
            sss=self.sound_hip
            sss.playsnd(self.sound_name)
            #pygame.mixer.music.load(self.sound_name)
            #pygame.mixer.music.play(0, 0.0)
        
    def o_move(self, obj_list=None):
        xxx=self.pos_x+self.dx
        yyy=self.pos_y+self.dy
        is_wall = self.check_wall(xxx, yyy)
        if not(is_wall):
            self.pos_x=xxx
            self.pos_y=yyy
            
    def check_wall(self, xxx, yyy):
        impact_wall = False
        if xxx>self.xmax or xxx<self.xmin:
            self.dx= -self.dx
            self.direct = -self.direct
            impact_wall = True
        if yyy>self.ymax or yyy<self.ymin:
            self.dy= -self.dy
            impact_wall = True
        if impact_wall:
            self.play_sound()
        return impact_wall
        
    def check_runing(self):
        ttt=time.time()
        self.time_to_start = self.time_to_start-(ttt-self.init_time)
        if self.time_to_start<=0:
            self.runing = True

    def update(self, o_list=None):
        if not(self.stopped):
            if not(self.runing):
                self.check_runing()
            self.pause += 1
            if self.pause >= self.delay:
                #reset pause and advance animation
                self.pause = 0
                self.frame += self.direct
                if abs(self.frame) >= len(self.setImages):
                    self.frame = 0
                self.image = self.setImages[self.frame]
            
            #######start move
                if self.runing:
                    self.o_move(o_list)
                    self.rect.center = (self.pos_x, self.pos_y)
        else:
            pass
        
    def loadImages(self, pnglistname):
        self.setImages = pnglistname.getadd(self.picname, 10)
        self.imageStand = self.setImages[0]
        self.radius = self.imageStand.get_height()/2

    def impact(self, a_sprites):
        """impact(self, a_sprites) eval new speed - dx dy movo1+m2vo2
        +...=m1vn1+m2vn2+... all m=1"""
        if self.run and not(self.stopped):
            for bbb in a_sprites:
                if bbb<>self and (not(self.new_dx)):
                    if sqcheck.CheckRound (bbb.pos_x, bbb.pos_y, bbb.radius, self.pos_x, self.pos_y, self.radius):
                        #self.nnnx,self.nnny=bbb.pos_x,bbb.pos_y
                        self.new_dx,self.new_dy,bbb.new_dx,bbb.new_dy=impact.sqImpact(self.pos_x, self.pos_y, self.dx, self.dy, bbb.pos_x, bbb.pos_y, bbb.dx, bbb.dy)

    def new_speed(self):
        if self.new_dx:
            #self.pos_x,self.pos_y = self.nnnx,self.nnny

#            self.dx = -self.dx/2
#            self.dy = -self.dy/2
#            self.o_move()
#
            self.dx, self.dy = self.new_dx, self.new_dy
            self.new_dx, self.new_dy = None, None
            self.direct = dsign(self.dx)

    def coords(self):
        return self.pos_x, self.pos_y
    
    def is_impacted_list(self, ob_list):
        for o_ob in ob_list:
            iii = sqcheck.CheckRound(self.pos_x, self.pos_y, self.radius,o_ob.pos_x, o_ob.pos_y, o_ob.radius)
            if iii:
                return True
        return False

class AnimationO(AnimationObj):
    """AnimationObj() - class to use animated objects on sprites"""
    def o_move(self):
        pass

    def o_set_pos(self, n_x, n_y):
        self.pos_x, self.pos_y = n_x, n_y

class LoadedObj():
    """LoadedObj() - class to control loaded media objects"""
    def __init__(self, basepath=".", baseext="png", startname=False, startcount=1):
        self.path=basepath+os.sep
        self.ext=baseext
        self.objdict={}
        self.startinit()
        if startname:
            self.addobj(startname, startcount)
            
    def startinit(self):
        pass
    
    def addobj(self, filesname, nuberfiles):
        newImages = []
        for i in range(nuberfiles-1):
            imgName = self.path + filesname+"%d." % i
            imgName += self.ext
            tmpImage = pygame.image.load(imgName).convert_alpha()
            newImages.append(tmpImage)
            
        self.objdict.update({filesname: newImages})
        
    def getadd(self, filesname, nuberfiles=1):
        if not (filesname in self.objdict):
            self.addobj(filesname, nuberfiles)
        
        return self.objdict[filesname]

class LoadedSounds(LoadedObj):
    """LoadadSounds(LoadedObj) - class to control loaded sound objects"""
    def addobj(self, s_file, nnn=None):
        filename=self.path + s_file + "."+self.ext
        #print filename
        n_snd=pygame.mixer.Sound(filename)
        self.objdict.update({s_file: n_snd})
    
    def startinit(self):
        pygame.mixer.init()
        self.stopped=False
        #pygame.mixer.set_num_channels(16)
    
    def set_stopped(self, s_stop=True):
        if s_stop:
            self.stopped=True
    
    def playsnd(self, s_name):
        if not(self.stopped):
            sss=self.getadd(s_name)
            s_ch=pygame.mixer.find_channel()
            s_ch.play(sss)
            return s_ch

class button_o:
    def __init__ (self, b_coord, pict_t, type_b=0):
        self.pos_x=b_coord[0]
        self.pos_y=b_coord[1]
        self.coord=b_coord
        self.picture=pict_t
        self.radius=pict_t.get_width()/2
        self.xradius=pict_t.get_width()/2
        self.yradius=pict_t.get_height()/2
        self.typenum=type_b
        
    def __getitem__(self,x):
        return self.coord, 1
            
    def check_in(self, c_coordx, c_coordy, c_size=[0, 0]):
        return sqcheck.CheckRectangle(self.pos_x+self.xradius, self.pos_y+self.yradius, self.xradius, self.yradius, c_coordx, c_coordy, c_size[0], c_size[1])

    def show_at(self, plato):
        plato.blit(self.picture, self.coord)

class tow_o:
    def __init__ (self, b_coord, pict_t, type_b=0):
        self.pos_x=b_coord[0]
        self.pos_y=b_coord[1]
        self.coord=b_coord
        self.picture=pict_t
        self.radius=pict_t.get_width()/2
        self.typenum=type_b
        
    def __getitem__(self,x):
        return self.coord, 2
            
    def check_in(self, c_coordx, c_coordy, c_size=0):
        return sqcheck.CheckRound(self.pos_x+self.radius, self.pos_y+self.radius, self.radius, c_coordx, c_coordy, c_size)

    def show_at(self, plato):
        plato.blit(self.picture, self.coord)
        
class t_button:
    """text_button - text button with border size"""
    def __init__ (self, pos_x, pos_y, b_text, b_event, f_height=18, \
    border_size=1, f_color=(0, 0, 0), b_color=(255, 255, 255), t_name=None, \
    f_name="."+os.sep+"fonts"+os.sep+"LiberationSans-Regular.ttf"):
        self.t_name = t_name
        self.state = 0
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.border_size = border_size
        self.coord = pos_x, pos_y
        self.color = b_color
        self.font=pygame.font.Font(f_name, f_height)
        self.fontcolor=f_color
        
        self.set_text(b_text)
        
        self.doing=b_event
        
    def set_text(self, n_text):
        self.text=n_text
        self.font_pic=self.font.render(self.text, True, self.fontcolor)
        self.width = self.font_pic.get_width()+2*self.border_size
        self.height = self.font_pic.get_height()+2*self.border_size

    def show_at(self, plato):
        if self.color:
            pygame.draw.rect(plato, self.color, (self.pos_x, self.pos_y, self.width, self.height), 0)
            
        if self.state==0:
            plato.blit(self.font_pic, (self.pos_x+self.border_size, self.pos_y+self.border_size))
        elif self.state==1:
            plato.blit(self.font_pic, (self.pos_x+self.border_size, self.pos_y))
        elif self.state==2:
            plato.blit(self.font_pic, (self.pos_x, self.pos_y+self.border_size))
        
    def check_in(self, c_coordx, c_coordy):
        self.mouse_in=sqcheck.CheckRectPoint(self.pos_x, self.pos_y, self.width, self.height, c_coordx, c_coordy)
        if not(self.mouse_in):
            self.state = 0
        return self.mouse_in
        
    def ch_state(self, event_type):
        if event_type==MOUSEMOTION:
            if self.mouse_in and (self.state <> 2):
                self.state=1
        elif event_type==MOUSEBUTTONDOWN:
            self.state=2
        elif event_type==MOUSEBUTTONUP:
            self.state=0
        return self.state

class t_label(t_button):
    """t_label - simpley text label"""
    # (may be it is not correct to set parrent class t_button)
    def show_at(self, plato):
        if self.color:
            pygame.draw.rect(plato, self.color, (self.pos_x, self.pos_y, self.width, self.height), 0)
        plato.blit(self.font_pic, (self.pos_x+self.border_size, self.pos_y+self.border_size))
        
    
    def check_in(self, c_coordx, c_coordy):
        pass
        
    def ch_state(self, event_type):
        pass
                
class Game(object):
    def __init__(self, g_mode = (800, 600), g_caption = "defenderuX"):
        pygame.init()
        self.window = pygame.display.set_mode(g_mode)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(g_caption)
        pygame.event.set_allowed([QUIT, KEYUP, MOUSEBUTTONUP])   
    def run(self):
        print 'defenderuX Starting Event Loop'
        running = True
        while running:
            self.clock.tick()
            running = self.handleEvents()
            pygame.display.set_caption('defenderuX  %d fps' % self.clock.get_fps())
            pygame.display.flip()
        print 'Quitting. Thanks for playing defenderuX'
    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return False
        return True

class WidgetsPack():
    def __init__(self, pos_x=0, pos_y=0, w_size=5, h_alignment=True, start_list=[]):
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.width=0
        self.height=0
        self.w_size=w_size#size betwin 2 objects centers
        self.h_alignment=h_alignment
        self.w_list=[]
        
        self.add_list(start_list)
        
    def __len__(self):
        return len(self.w_list)
        
    def __getitem__(self, nnn):
        if self.w_list<>[]:
            return self.w_list(nnn)

    def set_new_pos(self, pos_x, pos_y):
        if pos_x:
            self.pos_x = pos_x
        if pos_y:
            self.pos_y = pos_y
        for ooo in self.w_list:
            if self.h_alignment:
                self.y_centrize_list()
            else:
                self.x_centrize_list()

    def set_named_obj_str(self, o_name, new_str):
        for ooo in self.w_list:
            if ooo.t_name == o_name:
                ooo.set_text(new_str)
                if self.h_alignment:
                    self.y_centrize_list()
                else:
                    self.x_centrize_list()
                return True
        return False
        
    def add_list(self, list_w):
        lll=len(list_w)
        if  lll>0:
            if len(self.w_list)==0:
                self.height=list_w[0].height
                self.width=list_w[0].width
                list_w[0].pos_x=self.pos_x
                list_w[0].pos_y=self.pos_y
                self.w_list.append(list_w.pop(0))
                #list_w=list_w[1:]
            
            for wig in list_w:
                self.add_wig(wig)

    def add_wig(self, n_wig):
        if self.h_alignment:
            n_wig.pos_x = self.w_list[-1].pos_x+(self.w_list[-1].width)/2+self.w_size-(n_wig.width)/2
            self.width = n_wig.pos_x + n_wig.width - self.pos_x
            if n_wig.height>self.height:
                n_wig.pos_y=self.pos_y
                self.height=n_wig.height
                self.y_centrize_list()
            else:
                self.centrize_y(n_wig)
        else:
            n_wig.pos_y = self.w_list[-1].pos_y+(self.w_list[-1].height)/2+self.w_size-(n_wig.height)/2
            #n_wig.pos_y = self.pos_y+self.height+self.w_size
            self.height = n_wig.pos_y + n_wig.height - self.pos_y
            if n_wig.width>self.width:
                n_wig.pos_x=self.pos_x
                self.width=n_wig.width
                self.x_centrize_list()
            else:
                self.centrize_x(n_wig)
        self.w_list.append(n_wig)
            
    def y_centrize_list(self):
        for wig in self.w_list:
            self.centrize_y(wig)
            
    def centrize_y(self, c_wig):
        dy = (self.height-c_wig.height)/2
        c_wig.pos_y=self.pos_y+dy
        #print "y - "+str(c_wig.pos_y)

    def x_centrize_list(self):
        for wig in self.w_list:
            self.centrize_x(wig)
            
    def centrize_x(self, c_wig):
        dx = (self.width-c_wig.width)/2
        c_wig.pos_x=self.pos_x+dx
        #print "x - "+str(c_wig.pos_x)
        
    def show_at(self, plato):
        for wig in self.w_list:
            wig.show_at(plato)
            
    def check_in(self, c_coordx, c_coordy):
        for wig in self.w_list:
            wig.check_in(c_coordx, c_coordy)
            
    def ch_state(self, event_type):
        for wig in self.w_list:
            wig.ch_state(event_type)

if __name__ == '__main__':
    game = Game()
    game.run()
