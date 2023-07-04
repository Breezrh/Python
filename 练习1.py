# 引入 tkinter 库
import tkinter as tk

# 创建窗口
window = tk.Tk()
window.geometry("300x200")
window.title("登录界面")

# 添加标签名字
tk.Label(window, text="用户名").place(x=50, y=30)
tk.Label(window, text="密码").place(x=50, y=70)

# 添加文本框
username = tk.StringVar()
password = tk.StringVar()
tk.Entry(window, textvariable=username).place(x=110, y=30)
tk.Entry(window, textvariable=password, show='*').place(x=110, y=70)

# 登录函数
def login():
    if username.get() == "admin" and password.get() == "password":
        print("登录成功！")
    else:
        print("用户名或密码错误！")

# 添加登录按钮
tk.Button(window, text="登录", command=login).place(x=150, y=120)

# 进入消息循环
window.mainloop()