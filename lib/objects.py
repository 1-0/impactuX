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
    def __init__(self, listpng, pos_x=111, pos_y=111, dx=10, dy=5, delay=1, fff=0, direct=1, picname="rock"):
        
        pygame.sprite.Sprite.__init__(self)

        self.picname=picname
        self.loadImages(listpng)
        self.image = self.imageStand
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.frame = fff
        # increase delay value to slow down animation even more
        self.delay = delay
        self.pause = 0
        
        self.pos_x=pos_x
        self.xmax=615
        self.xmin=25
        self.dx=dx
        self.pos_y=pos_y
        self.ymax=455
        self.ymin=25
        self.dy = dy
        self.new_dx = None
        self.new_dy = None

#        self.direct = direct
        self.direct = dsign(self.dx)
        self.impacts = 0


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
        return impact_wall
        

    def update(self, o_list=None):
        self.pause += 1
        if self.pause >= self.delay:
            #reset pause and advance animation
            self.pause = 0
            self.frame += self.direct
            if abs(self.frame) >= len(self.setImages):
                self.frame = 0
            self.image = self.setImages[self.frame]
            
            #######start move
            self.o_move(o_list)
            self.rect.center = (self.pos_x, self.pos_y)
        
    def loadImages(self, pnglistname):
        self.setImages = pnglistname.getadd(self.picname, 10)
        self.imageStand = self.setImages[0]
        self.radius = self.imageStand.get_height()/2

    def impact(self, a_sprites):
        """impact(self, a_sprites) eval new speed - dx dy movo1+m2vo2
        +...=m1vn1+m2vn2+... all m=1"""
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

class AnimationO(AnimationObj):
    """AnimationObj() - class to use animated objects on sprites"""
    def o_move(self):
        pass

    def o_set_pos(self, n_x, n_y):
        self.pos_x, self.pos_y = n_x, n_y

class LoadedObj():
    """LoadedObj() - class to control loaded media objacts"""
    def __init__(self, basepath=".", baseext="png", startname=False, startcount=1):
        self.path=basepath+os.sep
        self.ext=baseext
        self.objdict={}
        if startname:
            self.addobj(startname, startcount)
            
        
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
        
class text_button:
    """text_button - very simply text button with radius"""
    def __init__ (self, b_coord, b_size, b_color, b_text, b_event, f_color=(0, 0, 0), f_height=18, f_name="."+os.sep+"fonts"+os.sep+"LiberationSans-Regular.ttf"):
        self.pos_x=b_coord[0]
        self.pos_y=b_coord[1]
        self.width=b_size[0]
        self.height=b_size[1]
        self.coord=b_coord
        self.color=b_color
        self.xradius=b_size[0]/2
        self.yradius=b_size[1]/2
        self.font=pygame.font.Font(f_name, f_height)
        self.fontcolor=f_color
        self.text=b_text
        
        self.doing=b_event
        
    def __getitem__(self,x):
        return self.coord, -1
        
    def show_at(self, plato):
        f1=self.font
        pygame.draw.rect(plato, self.color, (self.pos_x, self.pos_y, self.width, self.height), 0)
        # plato.blit.rrr
        plato.blit(f1.render(self.text, True, self.fontcolor), (self.pos_x+2, self.pos_y+2))
        
    def check_in(self, c_coordx, c_coordy):
        rox=self.width/2
        roy=self.height/2
        return sqcheck.CheckRectangle (self.pos_x+(rox), self.pos_y+(roy), rox, roy, c_coordx, c_coordy, 0, 0)
        
    def ch_state(self, event_type): pass
        
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
        #print "x---y "+ str(self.pos_x) + " --- " + str(self.pos_y)
        
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

class ObjList(object):
    def __init__(self, obj_type=0, start_list=[]):
        self.o_list=start_list
        self.o_type=obj_type

    def put_obj(self, aim_obj):
        for ooo in self.o_list:
            aim_obj.blit(ooo.picture,(ooo.pos_x,ooo.pos_x))
        
    def ch_obj(self, aim_obj):
        for ooo in self.o_list:
            aim_obj.blit(ooo.picture,(ooo.pos_x,ooo.pos_x))

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
