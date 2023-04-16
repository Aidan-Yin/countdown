import time
import tkinter as tk
from tkinter.font import Font
from playsound import playsound

def countdown_timer(duration):
    remaining_time = duration
    while remaining_time > 0:
        timer_text.set("剩余时间: " + str(remaining_time) + "秒")
        window.update()
        time.sleep(1)
        remaining_time -= 1

    # 倒计时结束后播放提示音
    playsound('notification_sound.wav')
    timer_text.set("倒计时完成！")

def start_countdown():
    # 获取用户输入的时间
    user_input = entry.get()
    try:
        duration = int(user_input)
    except ValueError:
        timer_text.set("无效的输入，请输入数字。")
        return

    # 开始倒计时
    timer_text.set("开始倒计时...")
    countdown_timer(duration)

# 创建窗口并添加控件
window = tk.Tk()
window.title("倒计时器")
window.geometry("300x300")

my_font = Font(family='Arial', size=20)

entry_label = tk.Label(window, text="请输入倒计时时间（秒）：", font=my_font)
entry_label.pack(pady=10)

entry = tk.Entry(window, width=10, font=my_font)
entry.pack(pady=10)

start_button = tk.Button(window, text="开始倒计时", command=start_countdown, font=my_font)
start_button.pack()

timer_text = tk.StringVar()
timer_label = tk.Label(window, textvariable=timer_text, font=my_font)
timer_label.pack(pady=10)

window.mainloop()