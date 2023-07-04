# 导入 tkinter 库
import tkinter as tk
# 导入时间模块
import time


# 定义计时器应用的主类
class TimerApp(tk.Frame):
    # 初始化
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # 创建界面上的组件
        self.create_widgets()
        # 初始化计时器数据
        self.start_time = None
        self.elapsed_time = 0.0
        self.paused_time = 0.0
        self.is_timer_running = False
        # 更新计时器的时间显示
        self.update_clock()

    # 创建界面上的组件
    def create_widgets(self):
        # 显示计时器的标签
        self.label = tk.Label(self.master, text="00:00:00", font=("Courier", 30))
        self.label.pack(pady=20)
        # 开始计时的按钮
        self.start_button = tk.Button(self.master, text="开始", command=self.start_timer)
        self.start_button.pack(side="left", padx=20)
        # 暂停计时的按钮
        self.pause_button = tk.Button(self.master, text="暂停", command=self.pause_timer, state="disabled")
        self.pause_button.pack(side="left", padx=20)
        # 重置计时器的按钮
        self.reset_button = tk.Button(self.master, text="重置", command=self.reset_timer, state="disabled")
        self.reset_button.pack(side="left", padx=20)
        # 退出应用的按钮
        self.quit_button = tk.Button(self.master, text="退出", command=self.master.destroy)
        self.quit_button.pack(side="left", padx=20)

    # 开始计时
    def start_timer(self):
        if self.is_timer_running:
            return
        if not self.start_time:
            # 计时器的开始时间为当前时间减去暂停的时间
            self.start_time = time.time() - self.paused_time
        self.is_timer_running = True
        # 更新开始计时按钮的文本
        self.start_button.config(text="继续")
        # 设置暂停计时按钮为可用状态
        self.pause_button.config(state="normal", text="暂停")
        # 设置重置计时器按钮为可用状态
        self.reset_button.config(state="normal")

    # 暂停计时
    def pause_timer(self):
        # 关闭计时器
        self.is_timer_running = False
        # 记录暂停的时间
        self.paused_time += time.time() - self.start_time
        # 更新按钮状态
        self.start_button.config(text="继续")
        self.pause_button.config(state="disabled")
        self.reset_button.config(state="normal")

    # 更新计时器显示的时间
    def update_clock(self):
        if self.is_timer_running:
            # 更新计时器已经运行的时间
            self.elapsed_time = time.time() - self.start_time
        # 将秒数转换为时分秒形式的字符串
        minutes, seconds = divmod(self.elapsed_time, 60)
        hours, minutes = divmod(minutes, 60)
        time_str = f"{hours:02.0f}:{minutes:02.0f}:{seconds:05.2f}"
        # 更新标签上的时间文本
        self.label.config(text=time_str)
        # 根据计时器状态更新按钮的状态和文本
        if self.is_timer_running:
            self.pause_button.config(text="暂停", state="normal")
        else:
            self.pause_button.config(text="继续", state="normal")
        # 定时器 50ms 后再次更新计时器的时间显示
        self.label.after(50, self.update_clock)

    # 重置计时器
    def reset_timer(self):
        # 关闭计时器
        self.is_timer_running = False
        # 重置计时器各项数据
        self.start_time = None
        self.elapsed_time = 0.0
        self.paused_time = 0.0
        # 更新按钮的状态和文本
        self.start_button.config(text="开始")
        self.pause_button.config(text="暂停", state="disabled")
        self.reset_button.config(state="disabled")
        # 更新标签上的时间文本
        self.label.config(text="00:00:00")


# 主函数
if __name__ == "__main__":
    root = tk.Tk()
    root.title("计时器")
    app = TimerApp(root)
    app.pack()
    root.mainloop()
