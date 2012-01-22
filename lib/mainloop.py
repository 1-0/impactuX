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

import menuI
import storyI
import runI
import setupI
import recordI
import endI
import functions

class scenes_run():
    """scenes_run - class of running game scenes"""
    def __init__(self):
        self.runing = True
        self.lvls_count = 10
        self.set_zero()

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
            self.game_lvl)
            if story_pass:
                if story_pass=="exit":
                    game_runing = False
                    return  "exit"
                if story_pass=="setup_game":
                    setupI.mainrun()
                    return 0
                else:
                    #start play screen
                    game_pass = runI.mainrun(functions.get_screen_set(), \
                    self.game_lvl, None, 0, self.g_score)
#                    game_pass = runI.mainrun(functions.get_screen_set(), \
#                    self.game_lvl, self.balls_pos, self.g_time, self.g_score)
                    if game_pass=="exit":
                        return  "exit"
                    if game_pass["run"]:
                        self.game_lvl += 1
                        self.g_score = game_pass["score"]
                        self.g_time = 0
                    elif game_pass["win"]:
                        g_res = "win"
                        game_runing = False
                    else:
                        g_res = "lose"
                        game_runing = False
            else:
                game_runing = False
        #start "The End" screen
        endI.mainrun(functions.get_screen_set(), g_res, \
        self.g_score, self.g_time)
                
        sss = self.g_score
        
        self.set_zero()
        return sss

    def mainrun(self):
        """mainrun(self) - main game screens class loop"""
        #start menu screen
        scene_i = menuI.mainrun(functions.get_screen_set()) #[next_window, exit_results]
        if scene_i == "exit":
            #functions.exit_game()
            self.runing = False
            return 0
        elif scene_i == "run_game":
            self.game_lvl = self.g_lvl
            game_result = self.runing_game()
            if game_result == "exit":
                self.runing = False
                return 0
            elif scene_i==0:
                return 0
            else:
                #functions.update_records(game_result)
                pass
        elif scene_i == "restore_game":
            self.game_lvl=self.g_lvl+1
            game_result = self.runing_game()
            if game_result == "exit":
                self.runing = False
                return 0
            elif scene_i==0:
                return 0
            else:
                #functions.update_records(game_result)
                pass
        elif scene_i == "setup_game":
            setup_result = menuI.mainrun(functions.get_screen_set())#start setup screen
            if setup_result == "exit":
                self.runing = False
                return 0
            else:
                pass
                #functions.update_setup(setup_result)
        elif scene_i == "record_game":
            rrr = recordI.mainrun(functions.get_screen_set())#start record screen
            if rrr == "exit":
                self.runing = False
                return 0

def mainrun():
    """mainrun() - main game loop"""
    n_game = scenes_run()
    while n_game.runing:
        n_game.mainrun()

if __name__ == '__main__':
    mainrun()
