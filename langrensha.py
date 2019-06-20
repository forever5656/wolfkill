#导入资源
from lrsclasses import Langren
from lrsclasses import Pingmin
from lrsclasses import Nvwu
from lrsclasses import Yuyanjia
from lrsclasses import All
from lrsclasses import Langrenx
from lrsclasses import Pingminx
from lrsclasses import Nvwux
from lrsclasses import Yuyanjiax
from lrsclasses import GetError

from wxfunctions import *
from collections import Counter
import random
import time
import _thread

#创建变量
Waiting = []
#设置参数
Langren.number =  1
Nvwu.number = 0
Yuyanjia.number = 0
Pingmin.number = 1
Game = []
Table = {}
Result = []
Done = []
Killed = ''
Alive = True
Dead = False
#临时参数
dengdailangren = False
#dengdaishouwei=False
dengdainvwu = False
dengdaiyuyanjia = False
dengdaitoupiao = False
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
    print(temp)
    temp = random.choices(temp, k=len(temp))
    print (temp)
    for y in range(len(Game)):
        if temp[y] == '狼人':
            Langren.new(Game[y])
            print(Game[y] + '->狼人')
            wx.sendmsg('您的身份是狼人,您将在10s内进入狼人专用群', Game[y])
        elif temp[y] == '女巫':
            Nvwu.new(Game[y])
            print(Game[y] + '->女巫')
            wx.sendmsg('您的身份是女巫',Game[y])
        elif temp[y] == '预言家':
            Yuyanjia.new(Game[y])
            print(Game[y] + '->预言家')
            wx.sendmsg('您的身份是预言家', Game[y])
        elif temp[y] == '平民':
            Pingmin.new(Game[y])
            print(Game[y] + '->平民')
            wx.sendmsg('您的身份是平民', Game[y])
        time.sleep(0.5)
    time.sleep(1)
    Groupup = []
    for x in range(len(Game)):
        Groupup.append(Name2Wx[Game[x]])
    wx.group(Groupup)
    LangrenGroupup=[]
    wx.send2group('名称分发完毕!')
    for x in range(len(Langrenx)):
        LangrenGroupup.append(Name2Wx[Langrenx[x]])
    wx.langrengroup(LangrenGroupup)
    print("hhh1")
    mainloop()
def Calculation(x = None):
    if x == 'Langren':
        wx.send2group('游戏结束,狼人胜利')
    return
    #结束的统计
    #print('游戏结束,暂无统计')
def Gameover():
    Proved = False
    for x in Langrenx:
        if All.alive(x) == True:
            Proved = True
    if not Proved:
        return 'Pingmin'
    Proved=False
    for x in Pingminx:
        if All.alive(x)==True:
            Proved=True
    for x in Nvwux:
        if All.alive(x)==True:
            Proved=True
    for x in Yuyanjiax:
        if All.alive(x)==True:
            Proved=True
    if not Proved:
        return 'Langren'
    #判断
    return False
def Toupiao():
    global Result
    global dengdaitoupiao
    global Done

    Result=[]
    Done=[]
    if Killed == '没有人':
        wx.send2group('请私聊投票(数字)')
    else:
        wx.send2group('请死者说遗言,请私聊投票(数字)')
    Table={}
    y=0
    TableStr='请选择对象:'
    for x in Game:
        if All.alive(x) == Alive:
            y = y+1
            Table[y] = x
            TableStr = TableStr + '\n'+str(y) + ':' + x
    wx.send2group(TableStr)
    dengdaitoupiao = True
    while dengdaitoupiao:
        time.sleep(1)
    print(Result)
    x = Counter(Result)
    y = sorted(x)
    Langren.kill(y[0])
    wx.send2group(y[0] + '被投票出局')
    #遗言 投票
    #自动统计并宣布谁出局
    return

def mainloop():
    global dengdailangren
    global dengdainvwu
    global dengdaiyuyanjia
    global Killed
    Table = {}
    wx.send2group('天黑请闭眼!')
    time.sleep(0.5)
    wx.send2group('狼人请睁眼')
    y = 0
    TableStr = '请选择对象:'
    for x in Game:
        if All.alive(x) == Alive:
            y = y + 1
            Table[y] = x
            TableStr = TableStr + '\n' + str(y) + ':' + x
    wx.send2langren(TableStr)
    dengdailangren = True
    while dengdailangren:
        time.sleep(1)
    wx.send2group('狼人请闭眼,女巫请睁眼')
    #选择提示
    #操作完毕等待输入
    for zz in Nvwux:
        wx.sendmsg('刚刚 ' + Killed + ' 死了,您可以选择救[1]或者不救[2]', zz)
    dengdainvwu = True
    while dengdainvwu:
        if len(Nvwux)==0:
            x=list(range(10))
            x.pop(0)
            time.sleep(random.choice(x))
            dengdainvwu = False
        time.sleep(1)
    wx.send2group('女巫请闭眼,预言家请睁眼')
    #选择提示
    #操作完毕等待输入
    for zz in Yuyanjiax:
        wx.sendmsg('请稍后...', zz)
    y = 0
    TableStr = '请选择对象:'
    for x in Game:
        y = y+1
        Table[y] = x
        TableStr = TableStr+'\n'+str(y)+':'+x
    for zz in Yuyanjiax:
        wx.sendmsg(TableStr,zz)
    dengdaiyuyanjia = True
    while dengdaiyuyanjia:
        if len(Yuyanjiax)==0:
            x=list(range(10))
            x.pop(0)
            time.sleep(random.choice(x))
            dengdainvwu = False
        time.sleep(1)
    if Killed=='':
        Killed='没有人'
    wx.send2group('天亮了,昨晚' + Killed + '被杀')
    if Gameover()==False:
        Toupiao()
        if Gameover()==False:
            mainloop()
        else:
            Calculation(Gameover())
    else:
        #结束统计
        Calculation(Gameover())
#等待消息(Itchat部分)
@itchat.msg_register(TEXT)
def recv(msg):
    global dengdailangren
    global dengdainvwu
    global dengdaiyuyanjia
    global Waiting
    global Game
    global dengdaitoupiao
    global Result
    global Done
    global Killed
    print("Call Recv")
    if dengdaitoupiao == True:
        if msg['User']['NickName'] in Game:
            if All.alive(msg['User']['NickName'])==True and msg['User']['NickName'] not in Done:
                if msg['Content'] in Table:
                    Result.append(Table[msg['Content']])
                    Done.append(msg['User']['NickName'])
                else:
                    wx.sendmsg('选项不存在,请重新选择',msg['User']['NickName'])
            else:
                wx.sendmsg('您已死或已参与投票,无法投票',msg['User']['NickName'])
        dengdaitoupiao = False
    if dengdailangren == True:
        StillAlive = False
        for x in Langrenx:
            if All.alive(x):
                StillAlive = True
        if not StillAlive:
            x=list(range(10))
            x.pop(0)
            time.sleep(random.choice(x))
            Calculation('Langren')
        if msg['User']['NickName'] in Game:
            if All.job(msg['User']['NickName'])=='狼人' and All.alive(msg['User']['NickName'])==Alive:
                if msg['Content'] in Table:
                    if Langren.kill(Table[msg['Content']]):
                        print('操作成功')
                        wx.send2langren('成功杀死' + Table[msg['Content']])
                        Killed = Table[msg['Content']]
                    else:
                        print('操作失败:'+GetError.Error)
                        wx.send2langren('无法杀死'+Table[msg['Content']]+':目标玩家已死')
            else:
                wx.sendmsg('您无法发送该指令:您不是狼人或您已死',msg['User']['NickName'])
        dengdailangren = False
    if dengdainvwu == True:
        #print('### 女巫')
        StillAlive = False
        for x in Nvwux:
            if All.alive(x):
                StillAlive=True
        if not StillAlive:
            x=list(range(10))
            x.pop(0)
            time.sleep(random.choice(x))
            dengdainvwu=False
        if msg['User']['NickName'] in Nvwux and All.alive(msg['User']['NickName'])==True:
            if msg['Content'] == '1' or msg['Content'] == '救':
                if Nvwu.save(Killed)==False:
                    wx.sendmsg('无法操作,您的机会已用完.请输入2',msg['User']['NickName'])
            elif msg['Content'] == '2' or msg['Content'] == '不救':
                Nvwu.kill(Killed)
                Killed=''
            wx.sendmsg('操作完成',msg['User']['NickName'])
        else:
            wx.sendmsg('不能操作:您不是女巫或您已死',msg['User']['NickName'])
        #判断 女巫是否活着 如果活着就选 挂了就延迟随机
        dengdainvwu = False
    if dengdaiyuyanjia == True:
        StillAlive = False
        for x in Yuyanjiax:
            if All.alive(x):
                StillAlive = True
        if not StillAlive:
            x = list(range(10))
            x.pop(0)
            time.sleep(random.choice(x))
            dengdaiyuyanjia = False
        if msg['User']['NickName'] in Game:
            if msg['User']['NickName'] in Yuyanjiax and All.alive(msg['User']['NickName'])==True:
                if msg['Content'] in Table:
                    wx.sendmsg('他/她的身份是:'+All.job(Table[msg['Content']]), msg['User']['Content'])
                else:
                    wx.sendmsg('输入错误',msg['User']['NickName'])
        #print('### 预言家')
        #判断 预言家是否活着 如果活着就选 挂了就延迟随机
        dengdaiyuyanjia = False
    if msg['Content'] == '开始游戏':
        #开始游戏
        if msg['User']['NickName'] in Waiting or msg['User']['NickName'] in Game:
            wx.sendmsg('您已在游戏中或在列表中,不能再次开始',msg['User']['NickName'])
        else:
            Wx2Name[msg['FromUserName']] = msg['User']['NickName']
            Name2Wx[msg['User']['NickName']] = msg['FromUserName']
            Waiting.append(msg['User']['NickName'])
            if len(Waiting) == Langren.number + Nvwu.number + Yuyanjia.number + Pingmin.number:
                if Game!=[]:
                    wx.sendmsg('无法加入,列表已满,请稍后再试', msg['User']['NickName'])
                    return False
                print('游戏开始')
                wx.group(Waiting)
                Game=Waiting
                Waiting=[]
                print(Game)
                _thread.start_new_thread(startgame,())
        print(Waiting)
itchat.run()
