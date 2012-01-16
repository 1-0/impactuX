#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       mainloop.py
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

import menuI
import storyI
import runI
import setupI
import recordI
import endI
import functions

class scenes_run():
    """scenes_run - class of runing game scenes"""
    def __init__():
        self.runing = True
        self.game_lvl = 0
        self.g_time = 0
        self.g_score = 0
        self.balls_pos = None
        self.lvls_count = 10
        
    def runing_game():
        game_runing = True
        while game_runing:
            #start story screen
            story_pass = storyI.mainrun(functions.get_screen_set(), \
            self.game_lvl)
            if story_pass:
                #start play screen
                game_pass = runI.mainrun(functions.get_screen_set(), \
                self.game_lvl, self.balls_pos, self.g_time, self.g_score)
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
        winI.mainrun(functions.get_screen_set(), g_res, \ 
        self.g_score, self.g_time)
                
        self.game_lvl = 0
        self.g_time = 0
        sss = self.g_score
        self.g_score = 0
        self.balls_pos = None
        return sss

    def mainrun():
        wind_i = menuI.mainrun(functions.get_screen_set()) #[next_window, exit_results]
        if wind_i[0] == "exit":
            functions.exit_game(wind_i[1])
        elif wind_i[0] == "run_game":
            game_result = self.runing_game(wind_i[1])
            functions.update_records(game_result)
        return 0
    
if __name__ == '__main__':
    n_game = scenes_run()
    while n_game.runing:
        n_game.mainrun()
