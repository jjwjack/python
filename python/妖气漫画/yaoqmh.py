import urllib.request
import re
import os


url = "http://www.yaoqmh.net/shaonvmanhua/list_4_1.html"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
# 封装获取html的三行代码
def getHtml(myurl):
	req = urllib.request.Request(url=myurl,headers=headers)
	response = urllib.request.urlopen(url)
	html = response.read().decode("utf-8")
	return html
# 获取漫画网首页html
def getMainHtml():
	html = getHtml(url)
	# 处理一下html，只保留中间的本子，侧边和顶部的本子不要
	startNum = html.find("mainleft")
	endNum = html.find("mainright")
	html = html[startNum:endNum]
	return html
# 从html获取本子编号，名字	
def getNumsAndNames():
	html = getMainHtml()
	# <a href="/shaonvmanhua/8389.html" class="pic show" title="里番H少女漫画之發情關係" target="_blank"><span class="bt">里番H少女漫画之發情關係</span> <span class="bg"></span><img class="scrollLoading" src="http://pic.taov5.com/1/615/183-1.jpg" xsrc="http://pic.taov5.com/1/615/183-1.jpg" alt="里番H少女漫画之發情關係" style="background:url(/static/images/loading.gif) no-repeat center;" width="150" height="185"></a>
	# <img class="scrollLoading" src="http://pic.taov5.com/1/615/183-1.jpg" xsrc="http://pic.taov5.com/1/615/183-1.jpg" alt="里番H少女漫画之發情關係" style="background:url(/static/images/loading.gif) no-repeat center;" width="150" height="185">
	regBookNum = r'href="/shaonvmanhua/(\d+)\.html"'
	bookNums = re.findall(regBookNum, html)
	regName = r'title="(.+?)"'
	bookNames = re.findall(regName, html)
	return bookNums,bookNames

# 打开每页，下载保存到这个名字的文件夹里
def downloadPic(i):
	bookNums = getNumsAndNames()[0]#获取本子编号
	bookNames = getNumsAndNames()[1]#获取本子名称

	urlBook = "http://www.yaoqmh.net/shaonvmanhua/"+bookNums[i]+".html"

	htmlBook = getHtml(urlBook)#获取本子html代码
	regPageNums = r"共(\d+))"#获取总页数
	# 格式为http://pic.taov5.com/1/615/183-1.jpg
	#       http://pic.taov5.com/1/618/160.jpg
	regImgStart1 = r"http://pic\.taov5\.com/1/(\d+)/\d+?\.jpg"#获取第一目录编号
	regImgStart2 = r"http://pic\.taov5\.com/1/\d+?/(\d+?)\.jpg"#获取第二目录编号
	reTest1 = r"日本邪恶少女漫画(.*?)妖气漫画网"
	test1 = re.findall(reTest1, htmlBook)
	pageNums = re.findall(regPageNums,htmlBook)#总页数，获得一个二维数组，因为上下共有两个总页数标签
	imgStart1 = re.findall(regImgStart1, htmlBook)#图片目录的第一个数字,findall返回一个数组
	imgStart2 = re.findall(regImgStart2, htmlBook)#图片目录的第二个数字
	# 开始页码和结束页码
	print(urlBook)
	print(test1)
	print(pageNums)
	print(imgStart1)
	print(imgStart2)
	os.system("pause")	

	rangeMin = int(imgStart2[0])

	rangeMax = int(imgStart2[0]) + int(pageNums[0])
	pageNums = int(pageNums[0])
	for pageNum in range(pageNums):
		urlImg = "http://pic.taov5.com/1/"+imgStart1[0]+"/"+str(rangeMin+pageNum)+".jpg"
		reqImg = urllib.request.Request(url=urlImg,headers=headers)
		responseImg = urllib.request.urlopen(reqImg)
		img = open(str(pageNum)+".jpg","wb")
		img.write(responseImg.read())
		img.close()
		print("已下载%d页，共%d页"%(pageNum+1,pageNums))#提示下载几页了，放在后面比较好
		# os.system("pause")

def downloadBook():
	bookNums = getNumsAndNames()[0]
	bookNames = getNumsAndNames()[1]
	# 打开每个本子网页，获取总页数，第一张图片的网址
	# <img alt="里番H少女漫画之發情關係" src="http://pic.taov5.com/1/615/143.jpg">
	for i in range(len(bookNums)):
		# 每个本子新建文件夹，下载完一个本子要返回上一级目录！！不然会一直新建子文件夹！
		# 断点续传，判断文件夹是否存在，如果不存在就创建，如果存在，判断里面的图片是否存在
		currentDir = os.getcwd()
		nameArray = []
		# 遍历当前文件夹，把所有文件夹名存入nameArray数组
		for i1,i2,i3 in os.walk(currentDir):
			nameArray.append(i2)
		nameArray = nameArray[0]
		# 名字数组里加上序号
		for eachname in nameArray:
			eachname = bookNums[i] + "_" + eachname
		# 如果文件夹已存在，输出这个文件夹名已存在
		if bookNums[i] + "_" + bookNames[i] in nameArray:
			print("已存在:"+bookNums[i] + "_" + bookNames[i])
		# 如果文件夹不存在，就新建文件夹，下载图片
		else:
			os.mkdir(bookNums[i] + "_" + bookNames[i])#新建文件夹
			os.chdir(bookNums[i] + "_" + bookNames[i])#跳转到指定目录#记得后面要返回上级目录！！
			print("正在下载："+bookNames[i])#给个下载提示本子名
			downloadPic(i)
		
			os.chdir(os.path.dirname(os.getcwd()))#返回上级目录
		
if __name__ == "__main__":
	downloadBook()
# 后期实现功能：esc停止运行，空格暂停，断点续传判断图片是否存在
