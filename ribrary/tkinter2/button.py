import tkinter

def clickBtn():
    button["text"] = "クリックしました!"


root = tkinter.Tk()
root.title("ボタンを作ります")
root.geometry("600x800")
button = tkinter.Button(root,text="ボタンです",font=("Times New Roman",24),command=clickBtn)
#button.place(x=200,y=200)
button.pack()
root.mainloop()