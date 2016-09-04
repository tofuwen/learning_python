"你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。"

import re
import glob
from collections import OrderedDict


def get_num(word, article):
    f = open(article, 'r', encoding='utf-8').read()
    # This method is wrong! It cannot match the first word.
    # regular = re.compile(r'[\s\,\;\.\n]{1}' + word + r'[\s\,\;\.\n]{1}')
    # occurences = regular.findall(f)
    # return len(occurences)
    words_list = re.findall(r'[\w]+', f)
    ans = 0
    for w in words_list:
        if word == w:
            ans += 1
    return ans


def article_analysis(path):
    articles = glob.glob('*.txt')
    for article in articles:
        dict_data = OrderedDict()
        doc = open(article, 'r', encoding='utf-8').read()
        words = re.findall(r'[\w\-\_\'\.]+', doc)
        words = list(map(lambda x: x.strip('.'), words))
        for word in words:
            dict_data[word] = get_num(word, article)
        print(dict_data.items())
        sorted_dict_data = OrderedDict(
            sorted(dict_data.items(), key=lambda x: x[1], reverse=True)
        )
        print('In %s, the word that shows up most is: ' % article)
        for first_item in sorted_dict_data:
            print(first_item + ' : %s times.' % sorted_dict_data[first_item])
            break

path = '.'
article_analysis(path)
