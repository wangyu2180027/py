import tkinter

root = tkinter.Tk()
#タイトルバのライトルをつける
root.title("初めてのTkinter")
#サイズ
root.geometry("800x600")

#ラベルを作る
label = tkinter.Label(root,text="初めてのラベル",font=("System",30))
label.place(x=300,y=300)
#画面を表示させる
root.mainloop()