#!/usr/bin/python
#-*- coding: utf-8 -*-

'''
对xml文件进行解析
'''


import os
import xml.etree.ElementTree as ET

class parse_xml():
	def __init__(self,xmlfile,show_log=True):
		self.xmlfile = xmlfile
		#显示信息
		self.show_log = show_log 


	def xml_exists(self):
		if not os.path.exists(self.xmlfile):
			raise Exception("路径 [{}] 不存在! 请检查...".format(self.xmlfile))


	def get_root(self):
		self.xml_exists()
		if self.show_log:
			print('开始解析文件 : [{}]'.format(self.xmlfile))
		tree = ET.parse(self.xmlfile)
		self.root = tree.getroot()		


	def get_element_children(self,element):
		"""在这个元素下返回子元素"""
		#self.get_root()
		if element is not None:
			if self.show_log:
				print('开始处理元素 : [{}]'.format(element))
				print('标记为 : [{}]'.format(element.tag))
			return [c for c in element]
		else:
			print('元素不存在!')


	def get_element_tag(self,element):
		'''返回元素下的标记.'''
		if element is not None:
			if self.show_log:
				print('开始处理元素 : [{}]'.format(element))
			return element.tag
		else:
			print('元素不存在!')

	def get_element_attrib(self,element):
		'''返回元素下的属性'''
		if element is not None:
			if self.show_log:
				print('开始处理元素 : [{}]'.format(element))
			return element.attrib
		else:
			print('元素不存在!')


	def get_elements_tag(self,elements):
		'''返回元素下的所有的标记'''
		if elements is not None:
			tags = []
			for e in elements:
				tags.append(e.tag)
			return tags
		else:
			print('元素不存在!')


	def get_elements_attrib(self,elements):
		'''返回元素下的所有的属性'''
		if elements is not None:
			attribs = []
			for a in elements:
				attribs.append(a.attrib)
			return attribs
		else:
			print('元素不存在!')



def main():
	xml=parse_xml("server_list_000028.xml",show_log=False)
	xml.get_root()
	#print xml.root
	#xml.xml_exists()
	print xml.get_element_children(xml.root)
	#childrens=xml.get_element_children(xml.root)
	#print xml.get_element_tag(xml.root)

	#print xml.get_element_attrib(xml.root)

	#print xml.get_elements_tag(xml.root)

	#print xml.get_elements_attrib(childrens[1])	


if __name__ == '__main__':
    main()








































# class parse_xml():
# 	def __init__(self,url=None):
# 		self.url=url
# 		self.get_tw_url="http://dz-gateway.xneo.cn/api/get_all_server.php"
# 		self.get_qq_url="http://dz-gateway-qq.xneo.cn/api/get_all_server.php"
# 		self.get_yy_url="http://dz-gateway.xneo.cn/api/get_all_server.php"

# 		plat={}
# 		plat["yy"]=self.get_yy_url
# 		plat["qq"]=self.get_qq_url
# 		plat["tw"]=self.get_tw_url
# 		if self.url != None:
# 			plat["url"]=self.url


#print plat


# res=urllib2.urlopen("http://dz-gateway.xneo.cn/api/get_all_server.php")
# xml=res.read()
# print xml




	# def Down_xmlfile(self,url):
	# 	# file=open()
	# 	# try:
	# 	# 	res=urllib2.urlopen(url)
	# 	# 	xml=res.read()





	# def Get_all_ip(self,xmlfile):



	# def Get_all_ip_server(self,xmlfile):



























































