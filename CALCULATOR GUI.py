from tkinter import *
root = Tk()
root.geometry("283x500")

root.title("Calculator by Shruti")


def select(event):
    global cal

    text = event.widget.cget("text")

    if text == "=":
        if cal.get().isdigit():
            display = int(cal.get())

        else:
            display = eval(entryCal.get())

        cal.set(display)
        entryCal.update()

    elif text == "C":
        cal.set("")
        entryCal.update()

    else:
        cal.set(cal.get() + text)
        entryCal.update()


cal = StringVar()
cal.set("")
entryCal = Entry(root, text=cal, font="Verdana 40")
entryCal.pack(fill=X)

f = Frame(root, bg="grey")

b1 = Button(f, text="9", font="Verdana 30")
b1.pack(side=LEFT,padx=5,pady=1)
b1.bind("<Button-1>", select)

b2 = Button(f, text="8", font="Verdana 30")
b2.pack(side=LEFT,padx=5,pady=1)
b2.bind("<Button-1>", select)

b3 = Button(f, text="7", font="Verdana 30")
b3.pack(side=LEFT,padx=5,pady=1)
b3.bind("<Button-1>", select)

b4 = Button(f, text="C", font="Verdana 30")
b4.pack(side=LEFT,padx=5,pady=1)
b4.bind("<Button-1>", select)
f.pack(anchor="w")


f = Frame(root, bg="grey")

b1 = Button(f, text="6", font="Verdana 30")
b1.pack(side=LEFT,padx=5,pady=1)
b1.bind("<Button-1>", select)

b2 = Button(f, text="5", font="Verdana 30")
b2.pack(side=LEFT,padx=5,pady=1)
b2.bind("<Button-1>", select)

b3 = Button(f, text="4", font="Verdana 30")
b3.pack(side=LEFT,padx=5,pady=1)
b3.bind("<Button-1>", select)

b4 = Button(f, text="=", font="Verdana 30")
b4.pack(side=LEFT,padx=2,pady=1)
b4.bind("<Button-1>", select)
f.pack(anchor="w")



f = Frame(root, bg="grey")

b1 = Button(f, text="3", font="Verdana 30")
b1.pack(side=LEFT,padx=5,pady=1)     
b1.bind("<Button-1>", select)
                                     
b2 = Button(f, text="2", font="Verdana 30")
b2.pack(side=LEFT,padx=5,pady=1)
b2.bind("<Button-1>", select)

b3 = Button(f, text="1", font="Verdana 30")
b3.pack(side=LEFT,padx=5,pady=1)
b3.bind("<Button-1>", select)


b4 = Button(f, text="*", font="Verdana 30")
b4.pack(side=LEFT,padx=5,pady=1)
b4.bind("<Button-1>", select)
f.pack(anchor="w")


f = Frame(root, bg="grey")

b1 = Button(f, text="0", font="Verdana 30")
b1.pack(side=LEFT,padx=5,pady=1)
b1.bind("<Button-1>", select)

b2 = Button(f, text="+", font="Tahoma 30")
b2.pack(side=LEFT,padx=5,pady=1)
b2.bind("<Button-1>", select)

b3 = Button(f, text="-", font="Magneto 30")
b3.pack(side=LEFT,padx=5,pady=1)
b3.bind("<Button-1>", select)
f.pack(anchor="w")

b4 = Button(f, text="/", font="Magneto 30")
b4.pack(side=LEFT,padx=5,pady=1)
b4.bind("<Button-1>", select)
f.pack(anchor="w")

f = Frame(root, bg="grey")

b1 = Button(f, text="%", font="Centaur 30")
b1.pack(side=LEFT,padx=5,pady=1)
b1.bind("<Button-1>", select)

b2 = Button(f, text=".", font="Magneto 30")
b2.pack(side=LEFT,padx=7,pady=1)
b2.bind("<Button-1>", select)

b3 = Button(f, text="(", font="Magneto 30")
b3.pack(side=LEFT,padx=7,pady=1)
b3.bind("<Button-1>", select)

b4 = Button(f, text=")", font="Magneto 30")
b4.pack(side=LEFT,padx=7,pady=1)
b4.bind("<Button-1>", select)
f.pack(anchor="w")

root.mainloop()