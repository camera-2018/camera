# 2021年2月3日by xyxsw
# 基于909的图片爬虫
from pyquery import PyQuery as pq
import requests
import re
import os

# doc = pq(url="http://909tu.com/s/senluocaituan/",encoding='utf-8')
# # 获取总页面第一页

# span = doc('.hezi ul li .biaoti a')
# # 找到文件a标签

list1 = ["1548"]
# 输入****.html
list2 = []
list3 = []
# for span in span.items():

# 	dx = span.attr.href
# 	# 遍历文件夹网址
# 	# dx  zhongguo/19199.html
# 	dx = re.sub("\D","",dx)
# 	list1.append(dx)
# list1len = len(list1)+1
# for i in range(0,list1len):
	

url3 = 'http://909tu.com/zhongguo/{}.html'.format(list1[0])
doc3 = pq(url=url3,encoding='utf-8')

ym = doc3('#pages a')

for ym in ym.items():
	ymm = ym.attr.href
	list3.append(ymm)

last = list3[-1]
lastyz1 = last.partition("_")
lastyz2 = lastyz1[-1].partition(".")
lastpage = lastyz2[0]
lastpage1 = int(lastpage)+1


for s in range(1,lastpage1):

	if s == 1 :	
		url = "http://909tu.com/zhongguo/{0}.html".format(list1[0])
	else:
		url="http://909tu.com/zhongguo/{0}{1}{2}.html".format(list1[0],"_",s)


	doc1 = pq(url=url,encoding='utf-8')
	# 获取http://909tu.com/zhongguo/19199.html的页面


	tu = doc1('.content  img')
	# 找到每一个图片的标签


	for tu in tu.items():

		dxtu = tu.attr.src
		# http://img.909tu.com/ri/d/file/bigpic/2019/11/21/11/zcdqprhfz1v.jpg找到地址
		
		list2.append(dxtu)


print(list2)
x = 1
os.mkdir("{}".format(list1[0]))
for l in list2:
	img = requests.get(l).content
	path = "\\{}\\".format(list1[0])+str(x)+".jpg"
	with open(path,'wb') as f:
		f.write(img)
		print("正在保存第{}张".format(x))
		x += 1


