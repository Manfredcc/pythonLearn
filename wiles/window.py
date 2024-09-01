import tkinter as tk  
from tkinter import messagebox  
  
def start_timer():  
    # 尝试从Entry控件中获取用户输入，并将其转换为整数  
    try:  
        min = int(entry.get())  
        if min <= 0:  
            messagebox.showerror("错误", "时间必须大于0！")  
            return  
          
        # 使用Tkinter的after方法来安排回调函数在指定的时间后被调用  
        def timer_done():  
            # 计时结束，显示提醒窗口  
            messagebox.showinfo("提醒", "时间到！")  
          
        # 注意：Tkinter的after方法接受毫秒作为时间单位  
        root.after(min * 60 * 1000, timer_done)  
          
        # 清除输入框的内容（可选）  
        entry.delete(0, tk.END)  
    except ValueError:  
        # 如果用户输入的不是有效的整数，则显示错误消息  
        messagebox.showerror("错误", "请输入有效的整数！")  
  
# 创建主窗口  
root = tk.Tk()  
root.title("时间提醒器")  
# 设置窗口的初始大小（这里只是示例，你可以根据需要调整）  
width = 400  
height = 200  
  
# 获取屏幕的宽度和高度  
screen_width = root.winfo_screenwidth()  
screen_height = root.winfo_screenheight()  
  
# 计算窗口应该放置的x和y坐标，以便窗口中心与屏幕中心对齐  
x = (screen_width // 2) - (width // 2)  
y = (screen_height // 2) - (height // 2)  
  
# 设置窗口的几何形状（大小+位置）  
root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")  
  
# 创建一个标签来提示用户输入  
label = tk.Label(root, text="请输入计时时间（分钟）：")  
label.pack(pady=15)  
  
# 创建一个Entry控件供用户输入  
entry = tk.Entry(root)  
entry.pack(pady=15)  
  
# 创建一个按钮，点击时调用start_timer函数  
start_button = tk.Button(root, text="开始计时", command=start_timer)  
start_button.pack(pady=20)  
  
# 运行主事件循环  
root.mainloop()