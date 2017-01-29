# python 3
# also need pillow

import itchat, time, re
from itchat.content import *

@itchat.msg_register([TEXT])
def text_reply(msg):
	match = re.search('年', msg['Text']).span()
	if match:
		itchat.send(('鸡年大吉啊！'), msg['FromUserName'])

itchat.auto_login(enableCmdQR=True, hotReload=True)
itchat.run()