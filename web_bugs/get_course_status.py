import urllib.request
import re
import json


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def getCourseStatus(html):
    reg = r'var sectionDataObj = (.*);'
    course_crn_re = re.compile(reg)
    crn_list = re.findall(course_crn_re, html)
    for i, crn in enumerate(crn_list):
        decoded_json = json.loads(crn)
        l = len(decoded_json)
        for j in range(l):
            print('crn:', decoded_json[j]['crn'])
            print('availability:', decoded_json[j]['availability'])
            print()

html = getHtml("https://courses.illinois.edu/schedule/2016/fall/CS/491").decode('utf-8')
getCourseStatus(html)
