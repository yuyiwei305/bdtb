#! /usr/bin/env python
#_*_ coding:utf-8 _*_
import sys
import os
import requests
import re
from  bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:32.0) Gecko/20100101 Firefox/32.0'}

class BDTB(object):
	def __init__(self,baserUrl,seeLZ):
		self.baseURL = baseUrl
		self.seeLZ = "?see_lz="+str(seeLZ)
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
		page = self.getPage(pagenum)
		for pagetxt in page.find_all("div",class_=re.compile('post_content_.*?',re.S)):
			parttern = re.compile(r'<.*>',re.S)
			for t in pagetxt.stripped_strings:
				truetext.append(t)
					
		for t in truetext:
			print t
			print "------------------------------------"
baseUrl = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseUrl,1)
#a = bdtb.gettitle()
#b = bdtb.getpagenum()
bdtb.getcontext(1)
