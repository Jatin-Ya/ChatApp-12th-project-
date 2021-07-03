import mysql.connector

m=mysql.connector.connect(host='localhost',database='project',user='root',password='1234')
mc=m.cursor()
suid=""
ruid=""


def entrycheck(uid,password):
    global suid
    suid=str(uid)
    q="SELECT uid,password FROM main where uid= %s and password= %s;"
    mc.execute(q,(uid,password))
    c=0
    for i in mc:
        c=c+1
    if c:
        return True
    else:
        return False

    
def check2(uid):
    global ruid
    ruid=str(uid)
    q="SELECT uid FROM main where uid="
    mc.execute(q+str(uid)+";")
    c=0
    for i in mc:
        c=c+1
    if c:
        return True
    else:
        return False

    

def fetch_name(uid):
    q="select name from main2 where uid= "        
    mc.execute(q+uid+";")
    r=""
    for i in mc:
        r=i[0]
    return r


def postmsg(msg):
    q="insert into messages (suid,ruid,message,status) values (%s,%s,%s,%s);"
    mc.execute(q,(suid,ruid,msg,"u"))
    q="commit;"
    mc.execute(q)


def getmsg():
    q="select message from messages where suid=%s and ruid=%s and status=%s;"
    mc.execute(q,(ruid,suid,"u"))
    msglist=[]
    for i in mc:
        msglist+=[i[0]]
    q="update messages set status=%s where suid=%s and ruid=%s and status=%s;"
    mc.execute(q,("r",ruid,suid,"u"))
    q="commit;"
    mc.execute(q)
    return  msglist

def getmessages():
    q="select suid,message from messages where (suid=%s and ruid=%s) or (suid=%s and ruid=%s);"
    mc.execute(q,(suid,ruid,ruid,suid))
    lst=[]
    for i in mc:
        lst+=[i]
    return lst



    
