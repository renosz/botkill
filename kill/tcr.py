# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

cl = LINETCR.LINE()
cl.login(token='AuthTokenAnda')
cl.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

KAC=[cl]
mid = cl.getProfile().mid
Bots=[mid]
oa='u02ce6a7e0a53802a4e7d3eb24101e53e'
admin=["u3ac8d486c3e1a75b0c8d4284feae285f","uebcbec2df1e585a2bc487d71de2b26fb","u7e95090c82f6d35273ac41dc8ff91bb6"]
zonaaman=['c9d3173d930cccb79659126b060ce0b3e']
try:
    cl.sendText('uebcbec2df1e585a2bc487d71de2b26fb', 'Login in DESKTOP3TT1SRen-x64')
except:
    pass
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "defender":True,
    "dblack":False,
    "clock":True,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":True,
    "atjointicket":False
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 19:
            if wait["defender"] == True:
                if op.param2 in admin:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1, [op.param2])
        if op.type == 13:
            if op.param3 in mid:
                if op.param2 in admin:
                    if op.param1 in zonaaman:
                        cl.acceptGroupInvitation(op.param1)
                        cl.sendText(op.param1, 'Kawasan Zona Aman!')
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        gs = cl.getGroup(op.param1)
                        targets = []
                        for g in gs.members:
                            targets.append(g.mid)
                        if targets == []:
                            cl.sendText(op.param1, "Not found target.")
                        else:
                            for target in targets:
                               if target in admin:
                                   pass
                               else:
                                   try:
                                       cl.kickoutFromGroup(op.param1, [target])
                                   except:
                                       cl.leaveGroup(op.param1)
                        cl.leaveGroup(op.param1)
                else:
                    cl.acceptGroupInvitation(op.param1)
                    cl.sendText(op.param1, 'You are not admin!')
                    cl.leaveGroup(op.param1)
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
