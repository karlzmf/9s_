# -*- coding: utf-8 -*-
# !/usr/bin/env python
import itchat


@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    message =  msg['Text']


itchat.auto_login()
itchat.run()
