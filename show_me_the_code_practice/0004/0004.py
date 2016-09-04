import re


def statistics(file_name):
    f = open(file_name, 'r').read()
    # match all the string with character, "-", "_", "."
    f = re.findall(r'[\w\-\.\']+', f)
    print(len(f))

file_name = 'English.txt'
statistics(file_name)
