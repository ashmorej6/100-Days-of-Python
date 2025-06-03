import tkinter

window = tkinter.Tk()
window.title("GUI Program")
window.minsize(500, 300)

my_label = tkinter.Label(text="I am a label", font=("Arial", 24))
my_label.pack(side="left")



window.mainloop()
