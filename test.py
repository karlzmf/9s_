# -*- coding: utf-8 -*-
#!/usr/bin/env python
import itchat

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print msg['Text']

itchat.auto_login()
itchat.run()


