#!/usr/bin/python
#-*- coding: utf-8 -*-

'''
通过后台api,下载xml文件进行读取可用信息


用法：python get_xml_info.py --name qq --getip 
表示获取qq渠道ip(去重)
'''

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2
from  parse_xml import *
from optparse import OptionParser

def down_xml(url,name):
	'''下载url命令为name.xml'''
	filename="%s.xml"%name
	if os.path.exists(filename):
		os.remove(filename)

	file=open(filename,'w')
	try:
		res=urllib2.urlopen(url)
		xml=res.read()	
		file.write(xml)
		print "\033[1;33m已保存 %s 在本地.\033[0m"%filename
	except Exception as err:
		print "下载url地址保存%s失败!  信息: %s"%(filename,str(err))
	finally: 
		file.close()



def get_ip(xmlfile,repeat=True):
	try:
		xml=parse_xml(xmlfile,show_log=False)
		#判断文件
		xml.xml_exists()
		name=xmlfile.split(".")[0]
		namefile="%s_ip.txt"%name
		if os.path.exists(namefile):
			os.remove(namefile)			
		file=open(namefile,'w+')
		xml.get_root()
		childs=xml.get_element_children(xml.root)

		if repeat:
			ips=[]
			print "####################################### %s 渠道 IP 列表(去重) 如下: (以保存%s中) #######################################"%(name,namefile)
			for child in childs:
				ips.append(child.get("ip"))
			ips=sorted(list(set(ips)))
			for ip in ips:
				print ip 
				file.write(ip)
				file.write("\n")	
		else:	
			print "####################################### %s 渠道 IP 列表如下: (以保存%s中) #######################################"%(name,namefile)
			for child in childs:
				print child.get("ip")
				file.write(child.get("ip"))
				file.write("\n")
		
	except Exception as err:
		print err
	finally:
		file.close()




def get_info(xmlfile):
	try:
		xml=parse_xml(xmlfile,show_log=False)
		#判断文件
		xml.xml_exists()		
		xml.get_root()
		all={}
		#dirc={}
		childs=xml.get_element_children(xml.root)
		for child in childs:
			plat=child.get("platform")
			cid=child.get("id")
			ip=child.get("ip")
			mark=plat+"_s"+cid
			dirc={mark:{}}
			dirc[mark].update({"ip":ip,"id":cid,"platform":plat})
			all.update(dirc)
		return all
	except Exception as err:
		print "获取失败.错误如下:",err




def get_all_info(xmlfile,ret=True):
	try:
		xml=parse_xml(xmlfile,show_log=False)
		#判断文件
		xml.xml_exists()		
		xml.get_root()
		all=[]
		childs=xml.get_element_children(xml.root)

		name=xmlfile.split(".")[0]
		namefile="%s_info.txt"%name
		if os.path.exists(namefile):
			os.remove(namefile)			
		file=open(namefile,'w+')


		for child in childs:
			l=[]
			cid=child.get("id")
			ip=child.get("ip")
			plat=child.get("platform")
			l.append(cid)
			l.append(ip)
			l.append(plat)
			all.append(l)
			file.write(cid)
			file.write(" ")
			file.write(ip)
			file.write(" ")
			file.write(plat)
			file.write("\n")
		file.close()
		if ret:
			print "####服####  ##### ip ####  #### 平台 ####"
			for s in all:
				print "    %s        %s      %s"%(s[0],s[1],s[2])
		return all
	except Exception as err:
		print err	



def main(argv):
	get_tw_url="http://dz-gateway.joy-cell.com/api/get_all_server.php"
	get_qq_url="http://dz-gateway-qq.xneo.cn/api/get_all_server.php"
	get_yy_url="http://dz-gateway.xneo.cn/api/get_all_server.php"

	plat={}
	plat["yy"]=get_yy_url
	plat["qq"]=get_qq_url
	plat["tw"]=get_tw_url

	usage = """用法:%prog --name [qq|tw|yy|ALL] --getip
				eg:%prog --name qq --getip      表示获取qq渠道ip"""
	parser = OptionParser(usage)

	parser.add_option("--name",action="store",type="str",dest="name",help="指定渠道如yy,qq,tw,ALL",metavar="name")
	parser.add_option("--getip",action="store_true",dest="getip",help="获取渠道ip")
	parser.add_option("--getinfo",action="store_true",dest="getinfo",help="获取渠道信息如：ip,id,platform")

	option,args = parser.parse_args()
	name = option.name

	if not name:
		parser.error("\033[1;31m选项--name 必须指定\033[0m")

	if name not in plat:		
		print "渠道 %s 指定错误..."%name
		exit()

	if option.getip:	
		url=plat[name]
		#调用下载函数
		down_xml(url,name)
		#获取ip(去重)
		get_ip("%s.xml"%name,repeat=True)


	if option.getinfo:
		url=plat[name]
		#调用下载函数
		down_xml(url,name)
		
		get_all_info("%s.xml"%name,ret=False)

	else:
		parser.error("\033[1;31m选项--name,--getip必须同时指定\033[0m")


if __name__ == "__main__":
	main(sys.argv)




# all=get_all_info("qq.xml",ret=False)
# print all

# file=open("qq_info.txt",'r')
# info=file.readline()
# file.close()
# print info[0]






























