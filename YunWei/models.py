#!/usr/bin/env python
#-*- coding: utf-8 -*-
#update:2014-09-12 by liufeily@163.com

from django.db import models


class ServerInfo(models.Model):
    server = models.CharField(max_length=20, verbose_name=u'游戏服')
    ip = models.CharField(max_length=20, verbose_name=u'IP地址')
    sid = models.CharField(max_length=20, verbose_name=u'id')

    def __unicode__(self):
        return u'%s' %(self.server)
   
    class Meta:
        verbose_name = u'游戏列表'
        verbose_name_plural = u'游戏列表管理'


