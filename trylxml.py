#! /usr/bin/env python
#_*_ coding:utf-8 _*_
import sys
import os
import requests
import re
from  bs4 import BeautifulSoup
from  lxml import etree
reload(sys)
sys.setdefaultencoding('utf-8')




headers = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:32.0) Gecko/20100101 Firefox/32.0'}

class BDTB(object):
	def __init__(self,baserUrl,seeLZ):
		self.baseURL = baseUrl
		self.seeLZ = "?see_lz="+str(seeLZ)
	def gethtml(self,pageNum):
		url = self.baseURL+self.seeLZ+"&pn="+str(pageNum)
		r = requests.get(url,headers)
		return r.text

	def getPage(self,pageNum):
		url = self.baseURL+self.seeLZ+"&pn="+str(pageNum)
		r = requests.get(url,headers)
		soup = BeautifulSoup(r.content)
		return soup
	def gettitle(self):
		page = self.getPage(1)
		for pagetitle in page.find_all(class_="core_title_txt"):
			for titiletext in pagetitle.stripped_strings:
				title = titiletext
				return title
		return str(title).decode("utf-8")
	def getpagenum(self):
		page = self.getPage(1)
		for pagetext in page.find_all("span",class_="red" ,style = None):
			pattern = re.compile(r'\d',re.S)
			pagetext = str(pagetext).decode("utf-8")
			result = re.search(pattern,pagetext)
			a =  result.group()
			return a
		return int(a) 
		
	def getcontext(self,pagenum):
		truetext = []
		page = self.gethtml(pagenum)
		html = etree.HTML(page)
		id =  html.xpath('//div[@class="l_post l_post_bright j_l_post clearfix  "]')
		for each in id:
			content = each.xpath('div[starts-with(@class,"d_post_content_main ")]/div[@class="p_content "]/cc/div[@class="d_post_content j_d_post_content "]')
			for i in content:
				info = i.xpath('string(.)')
				content_2 = info.replace('\n','').replace(' ','')
				truetext.append(content_2)
		return truetext
			


baseUrl = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseUrl,1)
pagenum = int(bdtb.getpagenum())
for i in range(pagenum):
	a = i+1
	for j in bdtb.getcontext(a):
		b= str(j)
		f = open("text","a")
		f.writelines(u'回复正文  :     '+b+'\n')
		f.close()
	print "num %d is add" % a
