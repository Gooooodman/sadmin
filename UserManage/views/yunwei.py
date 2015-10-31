#!/usr/bin/env python
#-*- coding: utf-8 -*-

from django.shortcuts import render_to_response,RequestContext


@login_required
@PermissionVerify()
def ListQQ(request):
    # import subprocess
    # cmd = "python /data/yunwei/get_xml_info.py --name qq --getinfo"
    # ret = subprocess.call(cmd,shell=True,stdout=open('/data/null','w'),stderr=subprocess.STDOUT)
    # if ret == 0:
    #     id = 0
    # else:
    #     id = 1
    #     return 1
    # print id
    # file=open("/data/yunwei/qq_info.txt",'r')
    # ips=file.readlines()
    # file.close()

    from  get_xml_info import get_info
    ips=get_info("/data/yunwei/qq.xml")
    #print ips

    kwvars = {
        'ID':id,
        'ips':ips,
        'request':request,
    }    
    print request.path
    return render_to_response('UserManage/ListQQ.html',kwvars,RequestContext(request))




def UpdateCDN(request):
	kwvars = {

		'request':request,
	}  
	print request.path	
	return render_to_response('UserManage/update_cdn.html',kwvars,RequestContext(request))



















