from tkinter import *
import tkinter.messagebox as tmsg
import math
class sci_calculator(Tk):
    def __init__(self):
        super().__init__()  #calling super class constructor
        self.title("Scientific Calculator")
        self.wm_iconbitmap("calc2.ico")

    def clean(self,event):
        """function for cleaning the output space"""
        text = event.widget.cget("text")
        if text == "clr":
            self.svalue.set("")
            self.screen.update()
        elif text == u"\u2190":
            self.screen.delete(len(self.svalue.get()) - 1)
            self.screen.update()

    def click(self,event):
        """function for getting the input clicked ,on the output space"""
        text = event.widget.cget("text")
        try:
            if text == "=":
                self.svalue.set(eval(self.svalue.get()))
                self.screen.update()
            elif text=="x\u00b2":  #using UNICODE for symbol
                self.svalue.set(pow(float(self.svalue.get()),2))
                self.screen.update()
            elif text=="x\u00b3":   #using UNICODE for symbol
                self.svalue.set(pow(float(self.svalue.get()),3))
                self.screen.update()
            elif text==u"3\u221Ax": #using UNICODE for symbol
                self.svalue.set(float(self.svalue.get())**(1/3))
                self.screen.update()
            elif text==u"4\u221Ax": #using UNICODE for symbol
                self.svalue.set(float(self.svalue.get())**(1/4))
                self.screen.update()
            elif text=="!": #using UNICODE for symbol
                self.svalue.set(math.factorial(float(self.svalue.get())))
                self.screen.update()
            else:
               self.svalue.set(self.svalue.get() + text)
               self.screen.update()
        except Exception as e:
            self.svalue.set("ERROR")
            self.screen.update()

    def calc(self,event):
        """functioon for calculating the mathematical functions"""
        text=event.widget.cget("text")
        type = self.inp_var.get()
        try:

            if text == "sin":

                    if type=="1":
                        self.svalue.set(f"{math.sin(math.radians(float(self.svalue.get())))}")
                        self.screen.update()
                    elif type=="2":
                        self.svalue.set(f"{math.sin(float(self.svalue.get()))}")
                    else:
                        tmsg.showerror("Error","Please select a input method!!")

            elif text == "cos":

                    if type=="1":
                        self.svalue.set(f"{math.cos(math.radians(float(self.svalue.get())))}")
                        self.screen.update()
                    elif type=="2":
                        self.svalue.set(f"{math.cos(float(self.svalue.get()))}")
                    else:
                        tmsg.showerror("Error","Please select a input method!!")

            elif text == "tan":

                if type=="1":
                    self.svalue.set(f"{math.tan(math.radians(float(self.svalue.get())))}")
                    self.screen.update()
                elif type=="2":
                    self.svalue.set(f"{math.tan(float(self.svalue.get()))}")
                else:
                    tmsg.showerror("Error","Please select a input method!!")
            elif text == "asin":

                if type=="1":
                    self.svalue.set(f"{math.degrees(math.asin(float(self.svalue.get())))}")
                    self.screen.update()
                elif type=="2":
                    self.svalue.set(f"{math.asin(float(self.svalue.get()))}")
                else:
                    tmsg.showerror("Error","Please select a input method!!")
            elif text == "acos":

                if type=="1":
                    self.svalue.set(f"{math.degrees(math.acos(float(self.svalue.get())))}")
                    self.screen.update()
                elif type=="2":
                    self.svalue.set(f"{math.acos(float(self.svalue.get()))}")
                else:
                    tmsg.showerror("Error","Please select a input method!!")
            elif text == "atan":

                if type=="1":
                    self.svalue.set(f"{math.degrees(math.atan(float(self.svalue.get())))}")
                    self.screen.update()
                elif type=="2":
                    self.svalue.set(f"{math.atan(float(self.svalue.get()))}")
                else:
                    tmsg.showerror("Error","Please select a input method!!")
            elif text == "sqrt":
                self.svalue.set(f"{math.sqrt(float(self.svalue.get()))}")
                self.screen.update()

            elif text == "abs":
                self.svalue.set(f"{self.svalue.get()+text}")
                self.screen.update()

            elif text == "inv":
                self.svalue.set(f"{1/float(self.svalue.get())}")
                self.screen.update()
            elif text == "\u03C0":

                self.svalue.set(f"{self.svalue.get()+str(math.pi)}")
                self.screen.update()
            elif text == "pow":
                self.svalue.set(f"{self.svalue.get() +text}")
                self.screen.update()
            elif text == "exp":
                self.svalue.set(f"{math.exp(float(self.svalue.get()))}")
                self.screen.update()
            elif text == "loge":
                self.svalue.set(f"{math.log(float(self.svalue.get()))}")
                self.screen.update()
            elif text == "log2":
                self.svalue.set(f"{math.log2(float(self.svalue.get()))}")
                self.screen.update()
            elif text == "log10":
                self.svalue.set(f"{math.log10(float(self.svalue.get()))}")
                self.screen.update()
            elif text == "ceil":
                self.svalue.set(f"{math.ceil(float(self.svalue.get()))}")
                self.screen.update()
            elif text == "floor":
                self.svalue.set(f"{math.floor(float(self.svalue.get()))}")
                self.screen.update()
            elif text == u"e\u207F-1":
                print("hello")
                self.svalue.set(f"{math.expm1(float(self.svalue.get()))}")
                self.screen.update()
        except Exception as e:
            self.svalue.set("ERROR")
            self.screen.update()
# equating equation by pressing enter
    def keyboard_inp_eqaul_to(self,event):
        try:
            self.svalue.set(eval(self.svalue.get()))
            self.screen.update()
        except Exception as e:
            self.svalue.set("ERROR")
            self.screen.update()
#taking input from keyboard
    def key_press(self,event):
        try:
            if event.char in num_list or event.char in op_list :
                self.svalue.set(self.svalue.get()+event.char)
                self.screen.update()
        except Exception as e:
            self.svalue.set("ERROR")
            self.screen.update()

#functions for creating different type of buttons

    def create_fun_btn(self,frame,name):
        self.btn = Button(frame, text=name, font="lucidia 19 bold", bg="red", relief=GROOVE, bd=8)
        self.btn.pack(padx=8,pady=3,anchor="nw")
        self.btn.config(width=4)
        self.btn.bind("<Button-1>", self.calc)
    def create_num_btn(self,frame,name):
        self.btn = Button(frame, text=name, font="lucidia 19 bold", bg="orange", relief=GROOVE, bd=8)
        self.btn.pack(padx=8,pady=3,anchor="nw")
        self.btn.config(width=4)
        self.btn.bind("<Button-1>",self.click)
        window.bind('<Key>',self.key_press)
    def create_op_btn(self,frame,name):
        self.btn = Button(frame, text=name, font="lucidia 19 bold", bg="sky blue", relief=GROOVE, bd=8)
        self.btn.pack(padx=8, pady=3, anchor="nw")
        self.btn.config(width=4)
        self.btn.bind("<Button-1>", self.click)
    def create_othr_btn(self,frame,name):
        self.btn = Button(frame, text=name, font="lucidia 19 bold", bg="green", relief=GROOVE, bd=8)
        self.btn.pack(padx=8, pady=3, anchor="nw")
        self.btn.config(width=4)
        self.btn.bind("<Button-1>", self.calc)
    def create_clr_btn(self,frame,name):
        self.btn = Button(frame, text=name, font="lucidia 19 bold", bg="deep pink", relief=GROOVE, bd=8)
        self.btn.pack(padx=8, pady=3, anchor="nw")
        self.btn.config(width=4)
        self.btn.bind("<Button-1>", self.clean)
    def create_equal_to_btn(self,frame,name):
        self.btn = Button(frame, text=name, font="lucidia 25 bold", bg="deep pink", relief=GROOVE, bd=8)
        self.btn.pack(padx=8,pady=4,anchor="nw",ipady=8,ipadx=10)
        self.btn.config(height=2)
        self.btn.bind("<Button-1>", self.click)
        window.bind("<Return>", self.keyboard_inp_eqaul_to)

# lists for differet buton names
fun_list=["sin","cos","tan","asin","acos","atan","inv","abs","sqrt"]
op_list=["+","-","*","/","**","//","!","(",")","%","x\u00b2","x\u00b3",u"3\u221Ax",u"4\u221Ax"]
num_list=["9","8","7","6","5","4","3","2","1","0",".",","]
other_list=["\u03C0","pow","exp","loge","log2","log10","ceil","floor",u"e\u207F-1"]
clr_list=[u"\u2190","clr"]

#list for all buttons in column wise order
list=[['asin' ,'acos' ,'atan','abs', 'sqrt', 'inv'],['sin', '7' ,'4' ,'1' ,'.' ,'\u03C0'],['cos' ,'8', '5' ,'2', '0', 'pow'],['tan', '9', '6', '3' ,',' ,'exp'],['(', '+' ,'-' ,'*' ,'/', 'loge'],[')', '%' ,'//' ,'**' ,'!' ,'log2'],["x\u00b2","x\u00b3",u"\u2190",u"3\u221Ax",u"4\u221Ax",u"e\u207F-1"],['clr', '=' ,'' ,'ceil' ,'floor' ,'log10']]

# creating user interface
window=sci_calculator()  #object of our class
# window.geometry("880x670")
# window.minsize(880,670)
window.maxsize(880,window.winfo_screenheight())
#inserting my entry

#inserting the output space
window.svalue=StringVar()
window.svalue.set("")
window.screen=Entry(window,textvar=window.svalue,font="lucidia 29 bold",relief=SUNKEN,justify="right",bd=15,width=30,bg="cyan2")
window.screen.pack(ipadx=20,ipady=5,pady=20)

#getting the input from the user using radio butons
f_inp=Frame(window,bg="gray30")
inp_type_label=Label(f_inp,text="Input values are in",font="lucida 20 bold",justify="left",bg="gray30").pack(side="left",padx=40)
window.inp_var=StringVar()
radio=Radiobutton(f_inp,text="Degree",font="lucida 20 bold",bg="gray35",variable=window.inp_var,value=1,cursor="dot").pack(side="left",padx=22)
radio=Radiobutton(f_inp,text="Radian",font="lucida 20 bold",bg="gray35",variable=window.inp_var,value=2,cursor="dot").pack(side="left")
f_inp.pack()


#frames---creating butttons

f_main=Frame(window,relief=SUNKEN,bd=15,bg="cyan4")

#col1 frame
col1=Frame(f_main,bg="grey")

for i in range(6):
    if list[0][i] in fun_list:
        window.create_fun_btn(col1,list[0][i])
col1.pack(side="left")

#col2 frame
col2=Frame(f_main,bg="grey")

for i in range(6):
    if list[1][i] in fun_list:
        window.create_fun_btn(col2,list[1][i])

    elif list[1][i] in num_list:
        window.create_num_btn(col2,list[1][i])
    elif list[1][i] in other_list:
        window.create_othr_btn(col2,list[1][i])
col2.pack(side="left")
#col 3
col3=Frame(f_main,bg="grey")

for i in range(6):
    if list[2][i] in fun_list:
        window.create_fun_btn(col3,list[2][i])
    elif list[2][i] in num_list:
        window.create_num_btn(col3,list[2][i])
    elif list[2][i] in other_list:
        window.create_othr_btn(col3,list[2][i])

col3.pack(side="left")
#col4 frame
col4=Frame(f_main,bg="grey")

for i in range(6):
    if list[3][i] in fun_list:
        window.create_fun_btn(col4,list[3][i])
    elif list[3][i] in num_list:
        window.create_num_btn(col4,list[3][i])
    elif list[3][i] in other_list:
        window.create_othr_btn(col4,list[3][i])

col4.pack(side="left")
#col 5
col5=Frame(f_main,bg="grey")

for i in range(6):

    if list[4][i] in op_list:
        window.create_op_btn(col5,list[4][i])

    elif list[4][i] in other_list:
        window.create_othr_btn(col5,list[4][i])

col5.pack(side="left")
#col 6
col6=Frame(f_main,bg="grey")

for i in range(6):
    if list[5][i] in op_list:
        window.create_op_btn(col6,list[5][i])
    elif list[5][i] in other_list:
        window.create_othr_btn(col6,list[5][i])

col6.pack(side="left")
#col 7
col7=Frame(f_main,bg="grey")

for i in range(6):
    if list[6][i] in op_list:
        window.create_op_btn(col7,list[6][i])
    elif list[6][i] in clr_list:
        window.create_clr_btn(col7,list[6][i])
    elif list[6][i] in other_list:
        window.create_othr_btn(col7,list[6][i])

col7.pack(side="left")
#col 8
col8=Frame(f_main,bg="grey")
window.create_equal_to_btn(col8,"=")
for i in range(6):
    if list[7][i] in clr_list:
        window.create_clr_btn(col8,list[7][i])
    elif list[7][i] in other_list:
        window.create_othr_btn(col8,list[7][i])

col8.pack(side="left")
f_main.pack(pady=20,padx=10)
window.configure(bg="gray30")
window.mainloop()