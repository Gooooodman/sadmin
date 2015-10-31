#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
# @login_required
# @PermissionVerify()
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
    ips=sorted(ips.iteritems(),key=lambda a:int(a[1].get("id")),reverse=False)
    s=str(len(ips))
    kwvars = {
        'sum':s,
        'ips':ips,
        'request':request,
    }    
    
    return render_to_response('UserManage/ListQQ.html',kwvars,RequestContext(request))




def ListYY(request):
    from  get_xml_info import get_info
    ips=get_info("/data/yunwei/yy.xml")
    ips=sorted(ips.iteritems(),key=lambda a:int(a[1].get("id")),reverse=False)
    #print ips
    s=str(len(ips))
    kwvars = {
        'sum':s,
        'ips':ips,
        'request':request,
    }    
    
    return render_to_response('UserManage/ListQQ.html',kwvars,RequestContext(request))


def ListTW(request):
    from  get_xml_info import get_info
    ips=get_info("/data/yunwei/tw.xml")
    ips=sorted(ips.iteritems(),key=lambda a:int(a[1].get("id")),reverse=False)
    print ips
    s=str(len(ips))
    kwvars = {
        'sum':s,
        'ips':ips,
        'request':request,
    }    
    
    return render_to_response('UserManage/ListQQ.html',kwvars,RequestContext(request))




















@csrf_exempt
def UpdateCDN(request):
    if request.method=='POST':
        print request.POST
        message = '渠道: %s                   版本： %s ' % (request.POST["qudao"],request.POST["version"])
        qudao=request.POST["qudao"]
        version=request.POST["version"]
        
        import subprocess
        cmd = "sh /data/yunwei/http_xml.sh"
        ret = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        stdout = ret.communicate()[0]
        kwvars= {'qudao':qudao,'version':version,'request':request,"ret":stdout}
        #return HttpResponse(message)
        return render_to_response('UserManage/update_cdn.html',kwvars,RequestContext(request))
    # else:
    #     message = 'You submitted an empty form.'
    else:    
    	kwvars = {

    		'request':request,
    	}  
    		
    	return render_to_response('UserManage/update_cdn.html',kwvars,RequestContext(request))


    


















