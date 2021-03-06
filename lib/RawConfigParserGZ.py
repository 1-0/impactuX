#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       RawConfigParserGZ.py
#       RawConfigParserGZ - class to read/write conf ini files from/to gz-archive
#       Based on RawConfigParser from ConfigParser.py - included in python 2.6 distr.
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

from configparser import ConfigParser as ConfigParser

class RawConfigParserGZ(ConfigParser):
    def read(self, filenames):
        """Read and parse a gz filename or a list of filenames.
        """
        # import gzip
        # import new_gzip as gzip

        if isinstance(filenames, str):
            filenames = [filenames,]
        read_ok = []
        for filename in filenames:
            try:
                fp = open(filename)
                # fp = gzip.open(filename)
            except IOError:
                continue
            self._read(fp, filename)
            fp.close()
            read_ok.append(filename)
        return read_ok

if __name__ == '__main__':
    print("insert test RawConfigParserGZ...")


