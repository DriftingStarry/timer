from datetime import datetime
from tkinter import *
def gettime():
    nowdate = datetime.now()
    targetdate = datetime(2024,7,29)
    r = targetdate - nowdate
    r = str(r)[:-7]
    return nowdate.strftime('%Y-%m-%d %H:%M:%S'),targetdate,r

root = Tk()
root.geometry('200x200')
root.title('Timer v1.0.1')
nowtime = Label(root,text='')
targetdate = Label(root,text='')
ra = Label(root,text='')
nowtime.pack(pady=5)
targetdate.pack(pady=5)
ra.pack(pady=5)
def update():
    n,t,r = gettime()
    nowtime["text"] = '当前时间:'+str(n) 
    targetdate["text"] = '美丽的假期最晚将在\n'+str(t)+'\n开始'
    ra["text"] = '就只有\n'+r+'\n这么点时间了'
    nowtime.after(1000,update)
update()
root.mainloop()