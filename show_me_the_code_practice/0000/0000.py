# '第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。'

from PIL import Image, ImageDraw, ImageFont


def add_num_to_photo(filename, text='1', fillcolor=(255, 0, 0)):
    img = Image.open(filename)
    width, height = img.size
    myfont = ImageFont.truetype('times.ttf', size=width//8)
    draw = ImageDraw.Draw(img)
    draw.text((width-width//8, 0), text, font=myfont, fill=fillcolor)
    img.save('1.jpg')

if __name__ == '__main__':
    filename = 'photo.JPG'
    text = '1'
    color = (0, 255, 0)
    add_num_to_photo(filename, text, color)
