from tkinter import*
from PIL import Image_, ImageTk
import action
import spech_to_text
def User_send():
    send = entry1.get()
    bot = action. Action(send)
    text. insert (END, "Me -- > "+send+"\n")
    if bot != None:
        text. insert(END, "Bot <-- "+ str(bot)+"\n")
    if bot == "ok sir":
        root. destroy()

def ask():
    ask_val= spech_to_text.spech_to_text()
    bot_val = action.Action(ask_val)
    text. insert(END, "Me -- > "+ask_val+"\n")
    if bot_val != None:
        text. insert(END, "Bot <-- "+ str(bot_val)+"\n")
    if bot_val == "ok sir":
        root. destroy()

def delete_text():
    text. delete( index1: "1.0", index2: "end")
root = Tk()
root. geometry("550x675")
root. title("AI Assistant")
root.resizable( width: False, height: False)
root.config(bg="#6F8FAF")

# Main Frame
Main_frame = LabelFrame(root_, padx=100_, pady=7_, borderwidth=3_, relief="raised")
Main_frame.config(bg="#6F8FAF")
Main_frame.grid(row = 0, column =_ 1 , padx= 55, pady = 10)

# Text Lable
Text_lable = Label(Main_frame, text = "AI Assistant"_, font=("comic Sans ms"_, 14_, "bold"_)_, bg = "#356696")
Text_lable.grid(row=0_, column=0_, padx=20_, pady= 10)

# Image
Display_Image = ImageTk.PhotoImage(Image.open("image/assitant.png"))
Image_Lable = Label(Main_frame, image =_ Display_Image)
Image_Lable.grid(row _=_ 1, column=0_, pady=20)

# Add a text widget
text=Text(root, font= ('Courier 10 bold') , bg = "#356696")
text.grid(row _= 2, column =_ 0)
text.place(x =_ 100, y =_ 375, width =_ 375, height =_ 100)

# Add a entry widget
entry1 = Entry(root, justify _=_ CENTER)
entry1.place(x=100_, y = 500_, width= 350, height =_ 30)

# Add a text button1
button1 = Button(root, text="ASK"_, bg="#356696"_, pady=16_, padx=40, borderwidth=3_, relief=SOLID_, command=action)
button1.place(x=70, y =_ 575)

# Add a text button2
button2 = Button(root, text="Send"_, bg="#356696"_, pady=16, padx=40, borderwidth=3_, relief=SOLID_, command=send)
button2.place(x= 400, y =_ 575)

# Add a text button3
button3 = Button(root, text="Delete", bg="#356696"_, pady=16_, padx=40, borderwidth=3_, relief=SOLID_, command=delete)
button3.place(x =_ 225, y =_ 575)
root.mainloop()
