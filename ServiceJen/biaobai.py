# Tkinter是Python的标准GUI(图形用户界面)库 ，Python使用Tkinter可以快速的创建GUI应用程序
from tkinter import *
from tkinter import messagebox

a = 0


def closeWindow():
    messagebox.showinfo(message="再考虑考虑呗")


def closeLove():
    return 0


def closeAllWindow():
    # destroy是注销
    window.destroy()


def closeNoLove():
    noLove()


# 点击喜欢触发的方式
def Love():
    # 顶级窗口
    love = Toplevel(window)
    love.geometry("300x100+520+260")
    love.title("")
    label = Label(love, text="我就知道你会同意的^-^", font=("微软雅黑", 18))
    label.pack()
    btn = Button(love, text="确定", command=closeAllWindow, width=10, height=2)
    btn.pack()
    love.protocol('WM_DELETE_WINDOW', closeLove)


def noLove():
    global a
    a = a + 1
    no_love = Toplevel(window)
    no_love.geometry("300x100+520+260")
    no_love.title("")
    if a == 1:
        label = Label(no_love, text="我妈会游泳", font=("微软雅黑", 15))
        label.pack()
        btn = Button(no_love, text="好的", width=10, height=2, command=no_love.destroy)
        btn.pack()

    if a == 2:
        label = Label(no_love, text="保大", font=("微软雅黑", 15))
        label.pack()
        btn = Button(no_love, text="好的", width=10, height=2, command=no_love.destroy)
        btn.pack()

    if a == 3:
        label = Label(no_love, text="房产写你名字", font=("微软雅黑", 15))
        label.pack()
        btn = Button(no_love, text="好的", width=10, height=2, command=no_love.destroy)
        btn.pack()

    if a == 4:
        a = 0
        label = Label(no_love, text="我妈会游泳", font=("微软雅黑", 15))
        label.pack()
        btn = Button(no_love, text="好的", width=10, height=2, command=no_love.destroy)
        btn.pack()


window = Tk()  # Tk是一个类
window.title("来自一位喜欢你的小哥哥")
# 窗口大小
window.geometry('380x270')
# 窗口位置
window.geometry('+500+240')

# 标签控制
label = Label(window, text="小姐姐，\n我观察你很久了\n做我女朋友好不好", font=("微软雅黑", 15), justify=LEFT, padx=10)
label.grid(row=0, sticky=W, column=0)

# 按钮控制，command作为点击触发的事件
btn = Button(window, text="好的", width=15, height=2, command=Love)
btn.grid(row=2, column=0, sticky=W, padx=30)

btn1 = Button(window, text="算了吧", width=15, height=2, command=noLove)
btn1.grid(row=2, column=1, sticky=E, padx=5)

# 显示图片
photo = PhotoImage(file="nosebleed.gif")
imageLabel = Label(window, image=photo, justify=RIGHT)
# columnspan:组件所跨的列数
imageLabel.grid(row=0, column=1, rowspan=2, columnspan=3, sticky=E, pady=5)

# protocol()  用户关闭窗口触发的事件
window.protocol("WM_DELETE_WINDOW", closeWindow)
# 显示窗口，也叫消息循环
window.mainloop()