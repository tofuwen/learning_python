#coding=utf-8
import urllib.request
import re


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def getImg(html):
    reg = r'src="(http://static.+?\.png)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    for i, url in enumerate(imglist):
        urllib.request.urlretrieve(url, "%s.jpg" % (i, ))
    for url in imglist:
        print(url)
    return imglist

html = getHtml("http://tieba.baidu.com/p/4637403344").decode('utf-8')
getImg(html)
