import urllib.request
import urllib.parse
import json

iplist = ["110.72.20.12:8123","180.76.154.5:8888"]
proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}
url = "http://www.whatismyip.com.tw/"
# url = "http://www.tuwenclub.com"

proxy_support = urllib.request.ProxyHandler({"http":"110.72.20.12:8123"})
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [("User-Agent","Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")]
urllib.request.install_opener(opener)
response = urllib.request.urlopen(url)
html = response.read().decode("utf-8")

print(html)

