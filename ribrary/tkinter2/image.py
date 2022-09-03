import tkinter 
root = tkinter.Tk()
root.title("画像を表示")
canvas = tkinter.Canvas(root,width=500,height=400,bg="skyblue")
canvas.pack()
img = tkinter.PhotoImage(file="ribrary/tkinter2/LINE_Brand_icon 2.png").subsample(3)
canvas.create_image(250,200,image=img)
root.mainloop()