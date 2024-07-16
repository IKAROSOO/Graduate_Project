from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('사진불러오기')
root.geometry('800x600')
 
img = ImageTk.PhotoImage(Image.open(r".\AKR20220415091000051_01_i_P4.jpg"))
label = Label(image=img)
label.pack()
 
quit = Button(root, text='종료하기', command=)
quit.pack()
 
root.mainloop()


