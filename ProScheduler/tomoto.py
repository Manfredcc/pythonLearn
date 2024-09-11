import time, datetime
import tkinter as tk
import tkinter.messagebox as messagebox
import threading
import os
import logging

# === configuration ===
independent = 1 # 1:独立使用 2:作为模块嵌入到其他程序
timeConfig = { 'work-1': 25, 'nap-1': 5,# 自由搭配，工作和休息周期
               'work-2': 25, 'nap-2': 5,
               'work-3': 25, 'rest': 15}
threads = [] # 维护所有的番茄时钟线程
stop_event = threading.Event()  # 线程退出标志位
tomotoRecordPath = '' # 若该路径未被定义，则默认保存番茄记录在当前目录下
logging.basicConfig(level=logging.DEBUG)
# logging.disable()

# 将屏幕设置为当前显示器中央
def windowCenter(window, width, height):
    # 获取屏幕的宽度和高度  
    screen_width = window.winfo_screenwidth()  
    screen_height = window.winfo_screenheight()  
    # 计算窗口应该放置的x和y坐标，以便窗口中心与屏幕中心对齐  
    x = (screen_width // 2) - (width // 2)  
    y = (screen_height // 2) - (height // 2) 
    window.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

# 记录番茄状态
def recordTomoto(string):
    if '' != tomotoRecordPath: # 自定义番茄记录路径
        if not os.path.exists(tomotoRecordPath): # 如果文件不存在，则创建
            os.makedirs(os.path.dirname(tomotoRecordPath), exist_ok=True) # 创建前置目录
        with open(tomotoRecordPath, 'a', encoding = 'utf-8') as file:
            file.write('\n' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
                    + ', ' + str(string))
            file.close()
    else: # 使用当前路径
        with open('tomotoRecord.csv', 'a', encoding = 'utf-8') as file:
            file.write('\n' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
                    + ', ' + str(string))
            file.close()

# 标记番茄状态
# 备注：好番茄指一个完整的，不被打断的周期
def markTomoto():
    wMark = tk.Tk()
    wMark.title('这是一个好番茄吗？')
    windowCenter(wMark, 300, 100)
    var = tk.StringVar()
    def onButtonClick(string):
        recordTomoto(string)
        wMark.destroy()
    bGoodTomoto = tk.Button(wMark, text = '好番茄', command = lambda: onButtonClick('好番茄'))
    bBadTomoto = tk.Button(wMark, text = '坏番茄', command = lambda: onButtonClick('坏番茄'))
    bGoodTomoto.pack(side = 'left', padx = 50)
    bBadTomoto.pack(side = 'right', padx = 50)
    wMark.mainloop()

# 启动一个定时器，定时结束，现实一个消息窗口
# @message：消息窗口信息
# @duration: 定时时间
def startMessageTimer(message, duration):
    try:
        if duration < 0:
            messagebox.showerror('w(ﾟДﾟ)w', '时间必须是正整数哦')
        rawDuration = duration
        duration *= 60
        checkInterval = 1
        while not stop_event.is_set() and duration > 0:
            time.sleep(checkInterval)
            duration -= checkInterval
            if duration <= 0:
                messagebox.showinfo('^_^', message + ' : ' + str(rawDuration) + '(min) over')
        return
    except ValueError:
        messagebox.showerror('w(ﾟДﾟ)w', '请输入有效整数(分钟)')

# 退出所有线程
def onCloseing(window):
    stop_event.set()  # 设置退出标志  
    for thread in threads:  
        try:  
            # 尝试在5秒内等待线程结束  
            thread.join(timeout=5)  
            if thread.is_alive():
                logging.error('线程 %s 超时未退出', thread.name)  
        except Exception as e:  
            logging.error('等待线程 %s 退出时发生错误: %s', thread.name, str(e))
    window.destroy()
    logging.info('关闭窗口')

# 计算截止时间（下一次定时器结束）
def calculateDuetime(dueTime, duration):
    endTime = datetime.datetime.now() + datetime.timedelta(minutes = duration)
    dueTime.config(text = endTime.strftime("%Y-%m-%d %H:%M:%S"))

# 番茄时钟
# @duetime：截止时间（下一次定时器结束）
def tomoto(duetime):
    for msg, duration in timeConfig.items():
        logging.debug(f"{msg}: {duration}")
        if stop_event.is_set():
            logging.debug('exit by window close')
            return
        calculateDuetime(duetime, duration)
        startMessageTimer(msg, duration)
    markTomoto()

# 创建线程：启动一个番茄时钟
def onStartEgoTomoto(duetime):
    threadObj = threading.Thread(target = tomoto, args = (duetime, ))
    threads.append(threadObj)
    threadObj.start()

def main(window):
    # 标签：显示计时时间
    lDueTime = tk.Label(window, text = '一起摇滚吧')
    # 按钮：开始计时
    bStartTomoto = tk.Button(window, text = '开始！', bg = 'orange', command = 
                             lambda: onStartEgoTomoto(lDueTime))
    bStartTomoto.pack(side = 'top', pady = 10)
    lDueTime.pack(side = 'top', pady = 10)
    # 关闭窗口：销毁所有线程
    window.protocol("WM_DELETE_WINDOW", lambda: onCloseing(window))
    # 主界面循环
    window.mainloop()

if independent:
    # 创建主界面
    window = tk.Tk()
    window.title('Ego Tomoto')
    windowCenter(window, 240, 100)
    # 开始
    main(window)