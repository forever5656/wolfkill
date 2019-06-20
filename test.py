import itchat

itchat.auto_login()
@itchat.msg_register(itchat.content.TEXT)
def recv(msg):
   print(msg['Content'])
itchat.run()
