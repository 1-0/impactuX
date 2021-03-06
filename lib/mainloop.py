#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       mainloop.py
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

import lib.menuI as menuI
import lib.storyI as storyI
import lib.runI as runI
import lib.setupI as setupI
import lib.recordI as recordI
import lib.endI as endI
import lib.functions as functions

class scenes_run():
    """scenes_run - class of running game scenes"""
    def __init__(self):
        self.runing = True
        self.lvls_count = 10
        self.set_zero()
        #self.g_score = 888

    def set_zero(self):
        """set_zero(self) initialize zero game settings"""
        self.g_lvl = 0
        self.game_lvl = 0
        self.g_time = 0
        self.g_score = 0
        self.balls_pos = None
        
    def runing_game(self):
        """runing_game(self) start playing"""
        game_runing = True
        while game_runing:
            #start story screen
            story_pass = storyI.mainrun(functions.get_screen_set(), \
            self.game_lvl, self.g_score)
            if story_pass:
                if story_pass=="exit":
                    game_runing = False
                    return  "exit"
                if story_pass=="menu":
                    self.set_zero()
                    #setupI.mainrun()
                    return 0
                else:
                    #start play screen
                    game_pass = runI.mainrun(functions.get_screen_set(), \
                    self.game_lvl, self.balls_pos, self.g_time, self.g_score)
#                    game_pass = runI.mainrun(functions.get_screen_set(), \
#                    self.game_lvl, self.balls_pos, self.g_time, self.g_score)
                    self.g_time=0
                    self.balls_pos=None
                    if game_pass["exit"]:
                        return  "exit"
                    elif game_pass["loose"]:
                        g_res = "loose"
                        game_runing = False
                        self.g_score=game_pass["score"]
                    elif game_pass["wingame"]:
                        g_res = "wingame"
                        game_runing = False
                        self.g_score=game_pass["score"]
                    elif game_pass["winlvl"]:
                        self.game_lvl += 1
                        self.g_time = 0
                        functions.save_game(game_pass["score"], 0, self.game_lvl, None)
                        g_res = "winlvl"
                        self.g_score=game_pass["score"]
                    else:
                        if (game_pass["time"]>0) or (self.game_lvl>0):
                            functions.save_game(game_pass["score"], game_pass["time"], self.game_lvl, game_pass["balls"])
                        self.set_zero()
                        return  0
                endI.mainrun(functions.get_screen_set(), g_res, \
                self.g_score, self.g_time, self.game_lvl)
                if game_pass["loose"]:
                    if functions.set_check_rec([game_pass["score"],\
                                                game_pass["time"]],):
                        recordI.mainrun(functions.get_screen_set(),\
                                        game_pass["score"],\
                                        game_pass["time"])

            else:
                game_runing = False
        #start "The End" screen
                
        sss = self.g_score
        
        self.set_zero()
        return sss

    def mainrun(self):
        """mainrun(self) - main game screens change class loop"""
        #start menu screen
        scene_i = menuI.mainrun(functions.get_screen_set()) #[next_window, exit_results]
        if scene_i == "exit":
            #functions.exit_game()
            self.runing = False
            return 0
        elif scene_i == "run":
            self.game_lvl = self.g_lvl
            game_result = self.runing_game()
            if game_result=="exit":
                self.runing = False
                return 0
            elif scene_i==0:
                return 0
            else:
                #functions.update_records(game_result)
                pass
        elif scene_i == "restore":
            lll=functions.load_game()
            self.game_lvl=lll["level"]
            self.g_time=lll["time"]
            self.g_score=lll["score"]
            self.balls_pos=lll["balls"]
            game_result = self.runing_game()
            if game_result=="exit":
                self.runing = False
                return 0
            elif scene_i==0:
                return 0
            else:
                #functions.update_records(game_result)
                pass
        elif scene_i == "setup":
            setup_result = setupI.mainrun(functions.get_screen_set())#start setup screen
            if setup_result == "exit":
                self.runing = False
                return 0
            else:
                pass
                #functions.update_setup(setup_result)
        elif scene_i == "record":
            rrr = recordI.mainrun(functions.get_screen_set())#start record screen
            if rrr == "exit":
                self.runing = False
                return 0

def mainrun():
    """mainrun() - main game loop"""
    import pygame
    n_game = scenes_run()
    while n_game.runing:
        n_game.mainrun()

    pygame.init()
    pygame.display.set_mode((640,480),0,32)
    

if __name__ == '__main__':
    mainrun()
