# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，
# 为你的应用生成激活码（或者优惠券），
# 使用 Python 如何生成 200 个激活码（或者优惠券）

import random


def create_key(filename, digit=4, num=200):
    f = open(filename, 'a')
    for i in range(0, num):
        for j in range(0, num):
            f.write(chr(random.randint(65, 90)))
        f.write('\n')
    f.close()

if __name__ == '__main__':
    filename = 'output.txt'
    digit = 5
    num = 200
    create_key(filename, digit, num)
