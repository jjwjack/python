import os
import re
import shutil
#os文件操作，re正则，shutil复制粘贴
path1 = r"" #脚本
path2 = r"" #mp3

#for root1, dirs1, files1 in os.walk(path1):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
# for root2, dirs2, files2 in os.walk(path2):
#     for i in range(0, len(files2)):
#         num, other = files2[i].split('_', 1)
#         num_root = os.path.join(root2, files2[i]) 
#         #print (num)
#         #C:\Users\VideoEditor\Desktop\301_test\1_一单元\1_《为人民服务》\1_预习\1_音画课文
#         num2 = r'\\\d_.*?单元\\%s_.*?\\1_预习\\1_音画课文$' %num#这个地方好像是有贪婪匹配，加了“单元”后可用
#         for root1, dirs1, files1 in os.walk(path1):
#             if re.findall(num2, root1):
#                 #shutil.copy(num_root, root1)
#                 shutil.copy(num_root, root1+'\\' + '录音.mp3')
# print("导入成功！")
path = r"C:\Users\Administrator\Desktop\人教6下TXT"
for dirpath, dirnames, filenames in os.walk(path):
	for i in range(len(filenames)):
		filename = dirpath + "\\" + filenames[i]
		# print(filename)
		for line in open(filename):
			print(line)

