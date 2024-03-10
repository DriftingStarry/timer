from datetime import datetime
import tkinter as tk

def cultime(start,end):
    gap = end - start
    gap = str(gap)[:-7]
    return gap

def getnow():
    nowtime = datetime.now()
    nowtime = nowtime.strftime('%Y-%m-%d %H:%M:%S')
    return nowtime

def get_target():
    user_input = entry.get()
    # input format: 'year month day'
    try:
        y, m, d = map(int,user_input.split())
    except:
        y, m, d = 2024, 7, 29
    targetdate = datetime(y, m, d)
    return targetdate
def update():
    nowtime = getnow()
    targetdate = get_target()
    timegap = cultime(datetime.now(), targetdate)

    nowtime_L["text"] = nowtime
    targetdate_L["text"] = targetdate
    timegap_L["text"] = timegap
    nowtime_L.after(1000,update)


root = tk.Tk()
root.title('Timer v1.1.0') #title
root.geometry('300x300') #size

t1 = tk.Label(text='当前时间')
t1.pack()

nowtime = getnow()
nowtime_L = tk.Label(root,text=nowtime)
nowtime_L.pack()

t2 = tk.Label(text = '请输入目标时间\n例如 2024 7 29')
t2.pack()

entry = tk.Entry(root)
et = tk.StringVar()
et.set('2024 7 29')
entry["textvariable"] = et
entry.pack()

t3 = tk.Label(text='识别到的时间, 未识别到则默认2024 7 29')
t3.pack()

targetdate = datetime(2024, 7, 29)
targetdate_L = tk.Label(root, text = targetdate)
targetdate_L.pack()

t4 = tk.Label(text='距离目标时间还有')
t4.pack()
timegap = cultime(datetime.now(),targetdate)
timegap_L = tk.Label(root,text=timegap)
timegap_L.pack()

update()
root.mainloop()