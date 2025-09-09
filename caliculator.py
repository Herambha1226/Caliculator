import tkinter as tk


root = tk.Tk()
root.title("Caliculator")
root.iconbitmap("C://Users//DELL//Desktop//Projects//caliculator//caliculator.ico")
root.geometry("350x540")
root.resizable(False,False)

def insert_number(number):
    enter_data.insert(tk.END,number)


enter_data = tk.Entry(root,width=50,border=3)
enter_data.grid(row=0,column=0,columnspan=5)

def click_operator(op):
    global first_num,operation
    
    try : 
        first_num = float(enter_data.get())
        operation = op
        enter_data.delete(0,tk.END)
    except ValueError:
        enter_data.delete(0,tk.END)
        enter_data.insert(0,'ERROR')
        
def Caliculate():
    global first_num,operation
    
    try:
        second_num = float(enter_data.get())
        
        
        if operation == "+":
            result = float(first_num) + float(second_num)
        elif operation == "-":
            result = first_num - second_num
        elif operation == "*":
            result = first_num*second_num
        elif operation == "/":
            if second_num == 0:
                result = "Error : Div by Zero"
            else:
                result = first_num/second_num
        else:
            result = "Error"
        enter_data.delete(0,tk.END)
        enter_data.insert(tk.END,result)
        first_num = None
        second_num = None
    except ValueError:
        enter_data.delete(0, tk.END)
        enter_data.insert(0, "Error")


def clear():
    enter_data.delete(0,tk.END)
    global first_number, operation
    first_number = None
    operation = None








button_1 = tk.Button(root,text='1',width=10,height=5,command=lambda: insert_number(1))
button_1.grid(row=1,column=0,pady=10)

button_2 = tk.Button(root,text='2',width=10,height=5,command=lambda: insert_number(2))
button_2.grid(row=1,column=1,pady=10)

button_3 = tk.Button(root,text='3',width=10,height=5,command=lambda: insert_number(3))
button_3.grid(row=1,column=2,pady=10)


button_4 = tk.Button(root,text='4',width=10,height=5,command=lambda: insert_number(4))
button_4.grid(row=2,column=0,pady=10)

button_5 = tk.Button(root,text='5',width=10,height=5,command=lambda: insert_number(5))
button_5.grid(row=2,column=1,pady=10)

button_6 = tk.Button(root,text='6',width=10,height=5,command=lambda: insert_number(6))
button_6.grid(row=2,column=2,pady=10)

button_7 = tk.Button(root,text='7',width=10,height=5,command=lambda: insert_number(7))
button_7.grid(row=3,column=0,pady=10)

button_8 = tk.Button(root,text='8',width=10,height=5,command=lambda: insert_number(8))
button_8.grid(row=3,column=1,pady=10)

button_9 = tk.Button(root,text='9',width=10,height=5,command=lambda: insert_number(9))
button_9.grid(row=3,column=2,pady=10)

button_0 = tk.Button(root,text='0',width=10,height=5,command=lambda: insert_number(0))
button_0.grid(row=4,column=0,pady=10)

button_add = tk.Button(root,text='+',width=10,height=5,command=lambda: click_operator("+"))
button_add.grid(row=1,column=4,pady=10)

button_subtraction = tk.Button(root,text='-',width=10,height=5,command=lambda: click_operator("-"))
button_subtraction.grid(row=2,column=4,pady=10)

button_multiple = tk.Button(root,text='*',width=10,height=5,command=lambda: click_operator("*"))
button_multiple.grid(row=3,column=4,pady=10)

button_division = tk.Button(root,text='/',width=10,height=5,command=lambda: click_operator("/"))
button_division.grid(row=4,column=4,pady=10)

button_equal = tk.Button(root,text='=',width=20,height=5,command=Caliculate)
button_equal.grid(row=4,column=1,columnspan=2,pady=10)

button_clear = tk.Button(root,text='clear',width=40,height=3,command=clear)
button_clear.grid(row=5,column=0,columnspan=5)

#addition
#def addition():
    

root.mainloop()