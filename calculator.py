from tkinter import *
from tkinter import PhotoImage
def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if(text=="="):
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif(text=="C"):
        scvalue.set(" ")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()


root=Tk()
root.geometry("600x800")
root.title("Simple Mathematical Calculator By Rosan")
root.minsize(300,600)
root.maxsize(400,800)
icon=PhotoImage(file='calculator.png')
root.iconphoto(False,icon)
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 20 bold",bg="light green" )
screen.pack(fill='x',padx=50,pady=50,ipadx=20,ipady=20)

# f=Frame(root,bg="grey",relief=SUNKEN)
# b=Button(f,text="7",font="lucida 20 bold",padx=10,pady=10)
# b.pack(side=LEFT,padx=10,pady=10)
# b.bind("<Button-1>",click)
# b=Button(f,text="8",font="lucida 20 bold",padx=10,pady=10)
# b.pack(side=LEFT,padx=10,pady=10)
# b.bind("<Button-1>",click)
# b=Button(f,text="9",font="lucida 20 bold",padx=10,pady=10)
# b.pack(side=LEFT,padx=10,pady=10)
# b.bind("<Button-1>",click)
# b=Button(f,text="C",font="lucida 20 bold",padx=10,pady=10)
# b.pack(side=LEFT,padx=10,pady=10)
# b.bind("<Button-1>",click)
# f.pack( )


btn_font = ("Helvetica", 20, "bold")
btn_bg = "pink"
btn_active_bg = "white"
btn_fg = "#000000"


# Create button frames with rows and columns
# button_texts = [
#     ["7", "8", "9", "C"],
#     ["4", "5", "6", "+"],
#     ["1", "2", "3", "-"],
#     [".", "0", "*", "/"],
#     ["%", "=", "", ""]
# ]
button_text=[
    ["7","8","9","C"],
    ["4","5","6","+"],
    ["1","2","3","-"],
    [".","0","*","/"],
    ["%","=","",""],
]
# for row_values in button_texts:
#     f = Frame(root, bg="light grey")
#     for text in row_values:
#         if text != "":
#             b = Button(f, text=text, font=btn_font, padx=10, pady=10, bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, relief=RAISED)
#             b.pack(side=LEFT, expand=True, fill="both", padx=5, pady=5)
#             b.bind("<Button-1>", click)
#     f.pack(expand=True, fill="both")
for row_values in button_text:
    f=Frame(root,bg="light blue")
    for text in row_values:
        if text!="":
            b=Button(f,text=text,font=btn_font,padx=10,pady=10,bg=btn_bg,fg=btn_fg,activebackground=btn_active_bg,relief=SUNKEN)
            b.pack(side=LEFT,expand=True,fill="both",padx=5,pady=5)
            b.bind("<Button-1>",click)

    f.pack(expand=True,fill="both")
root.mainloop()