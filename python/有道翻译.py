import urllib.request
import urllib.parse
import json

userinput = ""
while  userinput != "exit":
	userinput = input("输入要翻译的话（exit退出）：")
	url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link"
	data = {}
	data["type"] = "AUTO"
	data["i"] = userinput
	data["doctype"] = "json"
	data["xmlVersion"] = "1.8"
	data["keyfrom"] = "fanyi.web"
	data["ue"] = "UTF-8"
	data["action"] = "FY_BY_CLICKBUTTON"
	data["typoResult"] = "true"
	data = urllib.parse.urlencode(data).encode("utf-8")
	response = urllib.request.urlopen(url,data)
	result = response.read().decode("utf-8")
	result = json.loads(result)
	result = result["translateResult"][0][0]["tgt"]
	print(result)
