from linepy import *
from akad.ttypes import OpType
from threading import Thread, active_count
import os,traceback,sys,livejson
import command as com

#===========================================#
#LINEBOT: SAMPLE PUBLIC BOT
#SOURCELIB: PYPY/LINEPY & PYPY/JUSTGOOD
#CMD CREATED BY: IMJUSTGOOD
#GITHUB: GITHUB.COM/GOODOP/PUBLIC
#===========================================#
login = livejson.File('Data/login.json',True, False, 4)
db = livejson.File('Data/data.json')
main = db["main"];lets = livejson.File('Data/api.json')
fetchs = db["justGood"];maker = db["maker"];OT = OpType
if login["token"] !="":client = LINE(idOrAuthToken=login["token"])
else:client = LINE(login["email"],login["passwd"])
uid = client.profile.mid;poll = OEPoll(client)
good = com.justgood(uid=uid, client=client)
def main_loop(op):
    if op.type == OT.RECEIVE_MESSAGE:
        good.receive_message(op)
        msg = op.message
        to = msg.to;of = msg._from;txt = msg.text
        if msg.toType == 2:
           if msg.contentType == 0:
              if msg.text is None:pass
              else:
                 if of in maker and txt.lower()=="refresh":
                    client.sendMessage(to,"Refreshed")
                    python = sys.executable
                    os.execl(python, python, * sys.argv)
    elif op.type == OT.NOTIFIED_INVITE_INTO_GROUP:
        good.notified_invite_into_group(op)
    elif op.type == OT.NOTIFIED_READ_MESSAGE:
        good.notified_read_message(op)

while 1:
    try:
        ops = client.poll.fetchOperations(client.revision, 50)
        for op in ops:
            if fetchs == client.main():
               client.revision = max(client.revision, op.revision)
               t1 = Thread(target=main_loop(op,))
               t1.start()
               t1.join()
    except Exception as e:
        e = traceback.format_exc()
        if "ErrorCc" in e:print("Invalid Credit Value");sys.exit()
        elif "EOFError" in e:pass
        elif "ShouldSyncException" in e or "LOG_OUT" in e:
            python3 = sys.executable
            os.execl(python3, python3, *sys.argv)
        else:traceback.print_exc()