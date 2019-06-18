#DEBUG
BG='开始游戏'
#导入资源
from lrsclasses import *
from wxfunctionsDEBUG import *
import random
import time
#创建变量
Waiting=[]
#设置参数
Langren.number=2
Nvwu.number=1
Yuyanjia.number=1
Pingmin.number=3
Game=[]
Table={}
#临时参数
dengdailangren=False
dengdaishouwei=False
dengdainvwu=False
dengdaiyuyanjia=False
#登陆微信(Itchat部分)
wx.login()

#开始游戏
def startgame():
    temp=[]
    for x in range(Langren.number):
        temp.append('狼人')
    for x in range(Nvwu.number):
        temp.append('女巫')
    for x in range(Yuyanjia.number):
        temp.append('预言家')
    for x in range(Pingmin.number):
        temp.append('平民')
    temp=random.choices(temp,k=len(temp))
    for y in range(len(Game)):
        if temp[y]=='狼人':
            Langren.new(Game[y])
            print(Game[y]+'->狼人')
            wx.sendmsg('您的身份是狼人,您将在10s内进入狼人专用群',Game[y])
        elif temp[y]=='女巫':
            Nvwu.new(Game[y])
            print(Game[y]+'->女巫')
            wx.sendmsg('您的身份是女巫',Game[y])
        elif temp[y]=='预言家':
            Yuyanjia.new(Game[y])
            print(Game[y]+'->预言家')
            wx.sendmsg('您的身份是预言家',Game[y])
        elif temp[y]=='平民':
            Pingmin.new(Game[y])
            print(Game[y]+'->平民')
            wx.sendmsg('您的身份是平民',Game[y])
        time.sleep(0.5)
    time.sleep(1)
    LangrenGroupup=[]
    wx.send2group('名称分发完毕!')
    for x in range(len(Langrenx)):
        LangrenGroupup.append(x)
    wx.langrengroup(LangrenGroupup)
    mainloop()
def Calculation():
    #结束的统计
    print('游戏结束,暂无统计')
def Gameover():
    #判断
    return False
def Toupiao():
    #遗言 投票
    #自动统计并宣布谁出局
    print('##投票')
def mainloop():
    global dengdaishouwei
    global dengdailangren
    global dengdainvwu
    global dengdaiyuyanjia
    wx.send2group('天黑请闭眼!')
    time.sleep(0.5)
    wx.send2group('守卫请睁眼')
    time.sleep(1)
    wx.send2group('守卫请选择对象')
    #选择提示
    #操作完毕等待输入
    dengdaishouwei=True
    recv(['1'])
    while dengdaishouwei:
        time.sleep(1)
    wx.send2group('守卫请闭眼,狼人请睁眼')
    wx.send2langren('请稍后...')
    y=0
    TableStr='请选择对象:'
    for x in Game:
        y=y+1
        if All.alive(x)==Alive:
            Table[y]=x
            TableStr=TableStr+'\n'+str(y)+':'+x
    wx.send2langren(TableStr)
    dengdailangren=True
    recv(['1'])
    while dengdailangren:
        time.sleep(1)
    wx.send2group('狼人请闭眼,女巫请睁眼')
    #选择提示
    #操作完毕等待输入
    dengdainvwu=True
    recv(['1'])
    while dengdainvwu:
        time.sleep(1)
    wx.send2group('女巫请闭眼,预言家请睁眼')
    #选择提示
    #操作完毕等待输入
    dengdaiyuyanjia=True
    recv(['1'])
    while dengdaiyuyanjia:
        time.sleep(1)
    wx.send2group('天亮了')
    if Gameover()==False:
        print('投票啦')
        Toupiao()
        if Gameover()==False:
            mainloop()
    else:
        #结束统计
        Calculation()
#等待消息(Itchat部分)
#@itchat.msg_register(TEXT)
def recv(msg):
    global dengdaishouwei
    global dengdailangren
    global dengdainvwu
    global dengdaiyuyanjia
    global Waiting
    global Game
    global BG
    print('进入')
    if dengdailangren==True:
        dengdailangren=False
    if dengdainvwu==True:
        print('### 女巫')
        #判断 女巫是否活着 如果活着就选 挂了就延迟随机
        dengdainvwu=False
    if dengdaiyuyanjia==True:
        print('### 预言家')
        #判断 预言家是否活着 如果活着就选 挂了就延迟随机
        dengdaiyuyanjia=False
    print('退出')
    print(dengdaishouwei)
    if BG=='开始游戏':
        #开始游戏
        BG=''
        r='''
        if msg['User']['NickName'] in Waiting or msg['User']['NickName'] in Game:
            wx.sendmsg('您已在游戏中或在列表中,不能再次开始',msg['User']['NickName'])
        else:
            Wx2Name[msg['FromUserName']]=msg['User']['NickName']
            Name2Wx[msg['User']['NickName']]=msg['FromUserName']
            Waiting.append(msg['User']['NickName'])
            if len(Waiting)==Langren.number+Nvwu.number+Yuyanjia.number+Shouwei.number+Pingmin.number:
                if Game!=[]:
                    wx.sendmsg('无法加入,列表已满,请稍后再试',msg['User']['NickName'])
                    return False'''
        print('游戏开始')
        Wx2Name['ID1']='1'
        Name2Wx['1']='ID1'
        Wx2Name['ID2']='2'
        Name2Wx['2']='ID2'
        Wx2Name['ID3']='3'
        Name2Wx['3']='ID3'
        Wx2Name['ID4']='4'
        Name2Wx['4']='ID4'
        Wx2Name['ID5']='5'
        Name2Wx['5']='ID5'
        Wx2Name['ID6']='6'
        Name2Wx['6']='ID6'
        Wx2Name['ID7']='7'
        Name2Wx['7']='ID7'
        Wx2Name['ID8']='8'
        Name2Wx['8']='ID8'
        Waiting=['1','2','3','4','5','6','7','8']
        wx.group(Waiting)
        Game=Waiting
        Waiting=[]
        startgame()
recv(['1'])
#itchat.run()
