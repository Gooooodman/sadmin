#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'lupuxiao'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

'''
    搜集game相关数据
'''


class get_game():
    def __init__(self,iplist,port=22,gamedir="/data/server/"):
        self.iplist = iplist
        self.port = port

    def get_game_server_count(self):
        pass





