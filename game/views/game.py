#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
import time
from django.shortcuts import render_to_response,RequestContext
import  subprocess
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json
import os
from tools.get_server import get_server
from django.contrib.auth.decorators import login_required

import ConfigParser

@login_required
@csrf_exempt
def game_install(request):
    if request.method == 'POST':
        name = request.POST['name']
        server_id = request.POST['server_id']
        ip = request.POST['ip']
        start_date = request.POST['start_date']
        start_date = start_date.replace(" ","_")
        server_name = request.POST['server_name']
        if not ip or not name or not server_id or not  start_date or not server_name:
            message = "参数有误或参数不全..."
            kwvars = {"message":message,}
            return HttpResponse(json.dumps(kwvars),content_type='application/json')
        log_file = "/tmp/game_install.log"
        file=open(log_file,'a')
        port = 22
        ssh_conn = "ssh -A -p %s -o StrictHostKeyChecking=no -o GSSAPIAuthentication=no %s"%(port,ip)
        install_cmd = """echo "Yes" |%s 'bash install.sh %s %s %s %s --server_name "%s"'"""%(ssh_conn,name,server_id,ip,start_date,server_name)
        #install_cmd = """%s 'yum install vsftpd -y'"""%ssh_conn
        print install_cmd

        pipe = subprocess.PIPE
        install_ret = subprocess.Popen(install_cmd,stdout=pipe,stderr=pipe,shell=True)
        last_line= ""
        while install_ret.poll() == None:
            line = install_ret.stdout.readline()
            if len(line) >0:
                last_line = line
                #print line.strip()
                file.write(line+"</br>")
                file.flush()
        file.close()
        if install_ret.returncode != 0:
            message = "安装失败."
        else:
            message = "安装完成."

        kwvars = {"message":message,}
        return HttpResponse(json.dumps(kwvars),content_type='application/json')

    else:
        kwvars = {
            'request':request,
        }
        return render_to_response('game/install.html',kwvars,RequestContext(request))




def game_read_log_file(request):
    filename = '/tmp/game_install.log'
    with open(filename,'r') as f:
        return HttpResponse(f.read())



def game_clean_log(request):
    import datetime
    now=datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    cmd = "mv /tmp/game_install.log /tmp/game_install_%s.log;touch /tmp/game_install.log"%now
    pipe = subprocess.PIPE
    ret = subprocess.Popen(cmd,stdout=pipe,stderr=pipe,shell=True)
    stdout,stderr = ret.communicate()
    if ret.returncode != 0 :
        message = "清理失败.."
    else:
        message = "清空成功.."
    kwvars = {"message":message,}
    return HttpResponse(json.dumps(kwvars),content_type='application/json')


def form_test(request):
    kwvars = {
        'request':request,
    }
    return render_to_response("game/install.html",kwvars,RequestContext(request))



def jindutiao(request):
    kwvars = {
        'request':request,
    }
    return render_to_response("game/gundongtiao.html",kwvars,RequestContext(request))


def jindutiao_game_read_log_file(request):
    filelog="/tmp/game_install.log"
    filename="/tmp/num.txt"
    file=open(filelog,'r')
    lines=file.readlines()
    for line in lines:
        #print line
        line=line.strip("\n")
        if re.search(r"jindu:",line,re.I):
            num =  line.split(":")[1]
            file=open(filename,'w')
            file.write(num)
            file.close()
        else:
            file=open(filename,'r')
            num=file.read()
            file.close()
    if not num:
        num = 1
    return HttpResponse(num)





# def game_info(request):
#     if os.path.exists("/tmp/en.xml"):
#         file_time=os.stat("/tmp/en.xml").st_atime
#         now_time=time.time()
#         check_time=now_time-file_time
#         if check_time < 86400:
#             gt=get_server()
#             ip_server=gt.get_ip_server("/tmp/en.xml")
#             for ip in ip_server:
#                 l=list(ip_server[ip].split(","))
#                 ip_server[ip]=l
#             return render_to_response("game/game_info.html",{"dicts":ip_server,},RequestContext(request))
#     else:
#         cf = ConfigParser.ConfigParser()
#         cf.read("/data/django/game/views/gameserver.conf")
#         en_url=cf.get("get_all_server","en")
#         gt=get_server()
#         gt.down_xml(en_url,'en')
#         ip_server=gt.get_ip_server("/tmp/en.xml")
#         for ip in ip_server:
#             l=list(ip_server[ip].split(","))
#             ip_server[ip]=l
#         return render_to_response("game/game_info.html",{"dicts":ip_server,},RequestContext(request))

def game_info(request):
    web_url=request.META.get("PATH_INFO")
    name=list(web_url.strip("/").split("/"))[-1]
    filepath="/tmp/%s.xml"%name
    #print filepath
    if os.path.exists(filepath):
        #print "if"
        file_time=os.stat(filepath).st_atime
        now_time=time.time()
        check_time=now_time - file_time
        if check_time < 86400:
            gt=get_server()
            ip_server=gt.get_ip_server(filepath)
            for ip in ip_server:
                l=list(ip_server[ip].split(","))
                ip_server[ip]=l
            return render_to_response("game/game_info.html",{"dicts":ip_server,},RequestContext(request))
    else:
        #print "else"
        cf = ConfigParser.ConfigParser()
        cf.read("/data/django/game/views/gameserver.conf")
        url=cf.get("get_all_server",name)
        #print url
        gt=get_server()
        gt.down_xml(url,name)
        ip_server=gt.get_ip_server(filepath)
        for ip in ip_server:
            l=list(ip_server[ip].split(","))
            ip_server[ip]=l
        return render_to_response("game/game_info.html",{"dicts":ip_server,},RequestContext(request))

















