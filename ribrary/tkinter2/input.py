from importlib.metadata import entry_points
import tkinter 
def clickBtn():
    txt = entry.get()
    button["text"] = txt
root = tkinter.Tk()
root.title("テキスト入力")
root.geometry("400x200")
#这个是 只能输入20个文字
entry = tkinter.Entry(width=20)
entry.place(x = 10,y = 10)
button = tkinter.Button(text="ボタンです",font=("Times New Roman",200),command=clickBtn)


button.place(x=20,y=100)
root.mainloop()