# import itchat

# itchat.auto_login()

# itchat.send('Hello, filehelper', toUserName='filehelper')

import json
import requests
import itchat

excludes = ['ikun', 'rap', '唉', '救命', '太难了', '唱跳', '坤', '啊']

response = requests.get(host)
if response:
    print(response.json())
access_token = response.json()['access_token']

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print(f'receive msg: {msg.text}')
    if '爱你' in msg.text:
        return '么么哒~'
    if '想你' in msg.text:
        return 'I miss you too'
    if '在吗' in msg.text:
        return '不在, 在想你'
    if any(e in msg.text for e in excludes):
        hitokoto_url = 'https://v1.hitokoto.cn/?c=j&c=h&c=l'
        res = requests.get(hitokoto_url)
        return res.json()['hitokoto']

    return f'{msg.text}吗？'


itchat.auto_login()
itchat.run()
