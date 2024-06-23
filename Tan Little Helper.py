import customtkinter as ctk
import tkinter as tk
import matplotlib.pyplot as mpt
import math



app = ctk.CTk()
app.geometry("1366x768")
app.title("Tan's Little Helper")
app.grid_columnconfigure(0, weight=1)

tab = ctk.CTkTabview(width = 1366, height= 768, master = app)
tab.pack(padx= 20, pady = 20)
tab1 = tab.add("SIMPLE CALCULATOR")
tab2 = tab.add("SCIENTIFIC CALCULATOR")
tab3 = tab.add("GRAPHICAL CALCULATOR")
tab4 = tab.add("ASK AI")

#taking input from the user

InpEntryBox = ctk.CTkEntry(master = tab1, placeholder_text="Enter Input", width = 500, height = 150, font = ('Arial', 40))
InpEntryBox.place(x = 700, y = 10)

def EnterNum(num):
    InpEntryBox.insert(tk.INSERT, num)
    


def CE():
    InpEntryBox.delete(0,tk.END)
   

def bksp():
    InpEntryBox.delete(len(InpEntryBox.get())-1, tk.END)
    

output = ctk.CTkLabel(master = tab1, width = 500, height= 150, font = ("Arial", 40), text = "Here you will see output.")
output.place(x= 700, y = 350)

def computeoutput():
    try:
        output.configure(text = eval(InpEntryBox.get()))
        
    except ZeroDivisionError:
        output.configure(text = "Divided By Zero!!!")
        
    except:
        output.configure(text = "Can not.")
        
    

#key making for SIMPLE CALCULATOR



b0 = ctk.CTkButton(tab.tab("SIMPLE CALCULATOR"), text = "0")
b0.grid(padx = 20, pady= 20, row = 3, column = 0)
b1 = ctk.CTkButton(tab.tab("SIMPLE CALCULATOR"), text = "1")
b1.grid(padx = 20, pady= 20, row = 3, column = 1)
b2 = ctk.CTkButton(tab.tab("SIMPLE CALCULATOR"), text = "2")
b2.grid(padx = 20, pady= 20, row = 3, column = 2)
b3 = ctk.CTkButton(tab.tab("SIMPLE CALCULATOR"), text = "3")
b3.grid(padx = 20, pady= 20, row = 3, column = 3)
b4 = ctk.CTkButton(tab.tab("SIMPLE CALCULATOR"), text = "4")
b4.grid(padx = 20, pady= 20, row = 2, column = 0)
b5 = ctk.CTkButton(tab.tab("SIMPLE CALCULATOR"), text = "5")
b5.grid(padx = 20, pady= 20, row = 2, column = 1)
b6 = ctk.CTkButton(tab.tab("SIMPLE CALCULATOR"), text = "6")
b6.grid(padx = 20, pady= 20, row = 2, column = 2)
b7 = ctk.CTkButton(tab.tab("SIMPLE CALCULATOR"), text = "7")
b7.grid(padx = 20, pady= 20, row = 2, column =3)
b8 = ctk.CTkButton(tab.tab("SIMPLE CALCULATOR"), text = "8")
b8.grid(padx = 20, pady= 20, row = 1, column = 0)
b9 = ctk.CTkButton(tab.tab("SIMPLE CALCULATOR"), text = "9")
b9.grid(padx = 20, pady= 20, row = 1, column = 1)
bbksp = ctk.CTkButton(tab.tab("SIMPLE CALCULATOR"), text = "⌫")
bbksp.grid(padx = 20, pady = 20, row =1, column = 2)
bce = ctk.CTkButton(tab.tab("SIMPLE CALCULATOR"), text = "CE")
bce.grid(padx = 20, pady = 20, row = 1, column = 3)
bAdd = ctk.CTkButton(tab.tab("SIMPLE CALCULATOR"), text = "+")
bAdd.grid(padx = 20, pady = 20, row = 0, column = 0)
bSubt = ctk.CTkButton(tab.tab("SIMPLE CALCULATOR"), text = "-")
bSubt.grid(padx = 20, pady = 20, row = 0, column = 1)
bMult = ctk.CTkButton(tab.tab("SIMPLE CALCULATOR"), text = "*")
bMult.grid(padx = 20, pady = 20, row = 0, column = 2)
bDiv = ctk.CTkButton(tab.tab("SIMPLE CALCULATOR"), text = "/")
bDiv.grid(padx = 20, pady = 20, row =0, column = 3)
bGo = ctk.CTkButton(tab.tab("SIMPLE CALCULATOR"), text = "GO!")
bGo.place(x = 850, y = 200)

#adjusting buttons
b0.configure(height = 110, width = 90, fg_color = "#A0DB8E", text_color = "black", hover_color="#90C57F", border_width =3.5, border_color = "#648958", font = ("Arial", 36), command = lambda: EnterNum(0))
b1.configure(height = 110, width = 90, fg_color = "#A0DB8E", text_color = "black", hover_color="#90C57F", border_width =3.5, border_color = "#648958", font = ("Arial", 36), command = lambda: EnterNum(1))
b2.configure(height = 110, width = 90, fg_color = "#A0DB8E", text_color = "black", hover_color="#90C57F", border_width =3.5, border_color = "#648958", font = ("Arial", 36), command = lambda: EnterNum(2))
b3.configure(height = 110, width = 90, fg_color = "#A0DB8E", text_color = "black", hover_color="#90C57F", border_width =3.5, border_color = "#648958", font = ("Arial", 36), command = lambda: EnterNum(3))
b4.configure(height = 110, width = 90, fg_color = "#A0DB8E", text_color = "black", hover_color="#90C57F", border_width =3.5, border_color = "#648958", font = ("Arial", 36), command = lambda: EnterNum(4))
b5.configure(height = 110, width = 90, fg_color = "#A0DB8E", text_color = "black", hover_color="#90C57F", border_width =3.5, border_color = "#648958", font = ("Arial", 36), command = lambda: EnterNum(5))
b6.configure(height = 110, width = 90, fg_color = "#A0DB8E", text_color = "black", hover_color="#90C57F", border_width =3.5, border_color = "#648958", font = ("Arial", 36), command = lambda: EnterNum(6))
b7.configure(height = 110, width = 90, fg_color = "#A0DB8E", text_color = "black", hover_color="#90C57F", border_width =3.5, border_color = "#648958", font = ("Arial", 36), command = lambda: EnterNum(7))
b8.configure(height = 110, width = 90, fg_color = "#A0DB8E", text_color = "black", hover_color="#90C57F", border_width =3.5, border_color = "#648958", font = ("Arial", 36), command = lambda: EnterNum(8))
b9.configure(height = 110, width = 90, fg_color = "#A0DB8E", text_color = "black", hover_color="#90C57F", border_width =3.5, border_color = "#648958", font = ("Arial", 36), command = lambda: EnterNum(9))
bbksp.configure(height = 110, width = 90, fg_color = "#A0DB8E", text_color = "black", hover_color="#90C57F", border_width =3.5, border_color = "#648958", font = ("Arial", 36), command = lambda : bksp())
bAdd.configure(height = 110, width = 90, fg_color = "#A0DB8E", text_color = "black", hover_color="#90C57F", border_width =3.5, border_color = "#648958", font = ("Arial", 36), command = lambda: EnterNum('+'))
bSubt.configure(height = 110, width = 90, fg_color = "#A0DB8E", text_color = "black", hover_color="#90C57F", border_width =3.5, border_color = "#648958", font = ("Arial", 36), command = lambda: EnterNum('-'))
bce.configure(height = 110, width = 90, fg_color = "#A0DB8E", text_color = "black", hover_color="#90C57F", border_width =3.5, border_color = "#648958", font = ("Arial", 36), command = lambda: CE())
bMult.configure(height = 110, width = 90, fg_color = "#A0DB8E", text_color = "black", hover_color="#90C57F", border_width =3.5, border_color = "#648958", font = ("Arial", 36), command = lambda: EnterNum('*'))
bDiv.configure(height = 110, width = 90, fg_color = "#A0DB8E", text_color = "black", hover_color="#90C57F", border_width =3.5, border_color = "#648958", font = ("Arial", 36), command = lambda: EnterNum('/'))
bGo.configure(height = 80, width = 150, fg_color = "#A0DB8E", text_color = "black", hover_color="#90C57F", border_width =3.5, border_color = "#648958", font = ("Arial", 36), command = lambda: computeoutput())


mode = "dark"
def change_mode():
    global mode
    if(mode == "dark"):
        app._set_appearance_mode("light")
        mode = "light"
    if(mode == "light"):
        app._set_appearance_mode("dark")
        mode = "dark"
    
    






modeChanger = ctk.CTkButton(master = app, text = "☀️/🌙", command = lambda : change_mode())
modeChanger.place(x = 1, y = 1)

#======================================================================================================================================================================================================================================#
# graphical calculator

GraphTextBox = ctk.CTkTextbox(master = tab3, height = 100, width = 500, font = ("Arial", 40))
GraphTextBox.place(x = 350, y = 10)






























app.mainloop()