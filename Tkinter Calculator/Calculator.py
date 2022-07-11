import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk


expression = ''
answer = ''
results = ''
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.title('Calculator')
        self.master.geometry('{}x{}'.format(482,489))
        self.master.config(bg='#7AD3D8')
        self.master.resizable(0,0)

        self.lblDisplay = Label(self.master, textvariable=x, width=15,height=1,font=("Helvetica", 20), fg='White', bg='black',anchor='e')
        self.lblDisplay.grid(row=0, column=0, padx = (10,0), pady=(20,0),columnspan=4)

        self.lblDisplay2 = Label(self.master, text="Set",textvariable=y, width=15,height=1,font=("Helvetica", 20), fg='White', bg='black',anchor='e')
        self.lblDisplay2.grid(row=1, column=0, padx = (10,0), pady=(0,0),columnspan=4)

        self.txtWork = Text(self.master, width=18,height=16,font=("Helvetica", 15),bg='black', fg='White')
        self.txtWork.grid(row=2, column=4, padx = (10,0), pady=(10,0),columnspan=2, rowspan=7)

        self.btnSeven = Button(self.master, text='7', font=('Helvetica', '20'), width=3, height=1,padx=1, pady=1,bg='#E4EFF1',activebackground='#E4EFF1',command=lambda: [self.Number(7), self.ChangeState()])
        self.btnSeven.grid(row=4, column=0, padx = (10,0), pady=(5,0))

        self.btnEight = Button(self.master, text='8', font=('Helvetica', '20'), width=3, height=1,padx=1, pady=1,bg='#E4EFF1',activebackground='#E4EFF1',command=lambda: [self.Number(8), self.ChangeState()])
        self.btnEight.grid(row=4, column=1, padx = (5,0), pady=(5,0))

        self.btnNine = Button(self.master, text='9', font=('Helvetica', '20'), width=3, height=1,padx=1, pady=1,bg='#E4EFF1',activebackground='#E4EFF1',command=lambda: [self.Number(9), self.ChangeState()])
        self.btnNine.grid(row=4, column=2, padx = (5,0), pady=(5,0))

        self.btnFour = Button(self.master, text='4', font=('Helvetica', '20'), width=3, height=1,padx=1, pady=1,bg='#E4EFF1',activebackground='#E4EFF1',command=lambda: [self.Number(4), self.ChangeState()])
        self.btnFour.grid(row=5, column=0, padx = (10,0), pady=(5,0))

        self.btnFive = Button(self.master, text='5',font=('Helvetica', '20'), width=3, height=1,padx=1, pady=1,bg='#E4EFF1',activebackground='#E4EFF1',command=lambda: [self.Number(5), self.ChangeState()])
        self.btnFive.grid(row=5, column=1, padx = (5,0), pady=(5,0))

        self.btnSix = Button(self.master, text='6', font=('Helvetica', '20'), width=3, height=1,padx=1, pady=1,bg='#E4EFF1',activebackground='#E4EFF1',command=lambda: [self.Number(6), self.ChangeState()])
        self.btnSix.grid(row=5, column=2, padx = (5,0),pady=(5,0))

        self.btnOne = Button(self.master, text='1', font=('Helvetica', '20'), width=3, height=1,padx=1, pady=1,bg='#E4EFF1',activebackground='#E4EFF1',command=lambda: [self.Number(1), self.ChangeState()])
        self.btnOne.grid(row=6, column=0, padx = (10,0), pady=(5,0))

        self.btnTwo = Button(self.master, text='2', font=('Helvetica', '20'), width=3, height=1,padx=1, pady=1,bg='#E4EFF1',activebackground='#E4EFF1',command=lambda: [self.Number(2), self.ChangeState()])
        self.btnTwo.grid(row=6, column=1, padx = (5,0), pady=(5,0))

        self.btnThree = Button(self.master, text='3', font=('Helvetica', '20'), width=3, height=1,padx=1, pady=1,bg='#E4EFF1',activebackground='#E4EFF1',command=lambda: [self.Number(3), self.ChangeState()])
        self.btnThree.grid(row=6, column=2, padx = (5,0), pady=(5,0))

        self.btnZero = Button(self.master, text='0', font=('Helvetica', '20'), width=7, height=1,padx=1, pady=1,bg='#E4EFF1',activebackground='#E4EFF1',command=lambda: [self.Number(0), self.ChangeState()])
        self.btnZero.grid(row=7, column=0, padx = (10,0), pady=(5,0), columnspan=2)

        self.btnDot = Button(self.master, text='.', font=('Helvetica', '20'), width=3, height=1,padx=1, pady=1,bg='#E4EFF1',activebackground='#E4EFF1',command=lambda: [self.Decimal('.'), self.ChangeState()])
        self.btnDot.grid(row=7, column=2, padx = (5,0), pady=(5,0))

        self.btnPlus = Button(self.master, text='+', font=('Helvetica', '20'), width=3, height=3,padx=1, pady=1,bg='#7790B4',activebackground='#7790B4',command=lambda: [self.Operator('+'), self.ChangeState()])
        self.btnPlus.grid(row=4, column=3, padx = (5,0),pady=(4,0),rowspan=2)

        self.btnMinus = Button(self.master, text='-', font=('Helvetica', '20'), width=3, height=1,padx=1, pady=1,bg='#7790B4',activebackground='#7790B4',command=lambda: [self.Operator('-'), self.ChangeState()])
        self.btnMinus.grid(row=3, column=3, padx = (5,0), pady=(4,0))

        self.btnMulti = Button(self.master, text='*', font=('Helvetica', '20'), width=3, height=1,padx=1, pady=1,bg='#7790B4',activebackground='#7790B4',command=lambda: [self.Operator('*'), self.ChangeState()])
        self.btnMulti.grid(row=3, column=2, padx = (5,0), pady=(4,0))

        self.btnDivide = Button(self.master, text='/', font=('Helvetica', '20'), width=3, height=1,padx=1, pady=1,bg='#7790B4',activebackground='#7790B4',command=lambda: [self.Operator('/'), self.ChangeState()])
        self.btnDivide.grid(row=3, column=1, padx = (5,0), pady=(4,0))

        self.btnClearAll = Button(self.master, text='A/C', font=('Helvetica', '20'), width=3, height=1,padx=1, pady=1,bg='#DA1717',activebackground='#DA1717',command=lambda: [self.ClearAll(), self.ChangeState()])
        self.btnClearAll.grid(row=3, column=0, padx = (10,0), pady=(4,0))

        self.btnEqual = Button(self.master, text='=', font=('Helvetica', '20'), width=3, height=3,padx=1, pady=1,bg='#7790B4',activebackground='#7790B4',command=lambda: self.Equal())
        self.btnEqual.grid(row=6, column=3, padx = (5,0),pady=(4,0),rowspan=2)

        self.btnBack = Button(self.master, text='C', font=('Helvetica', '20'), width=3, height=1,padx=1, pady=1,bg='#DA1717',activebackground='#DA1717',command=lambda: [self.Back(), self.ChangeState()])
        self.btnBack.grid(row=2, column=0, padx = (10,0), pady=(15,0))

        self.btnNegative = Button(self.master, text='Neg', font=('Helvetica', '20'), width=3, height=1,padx=1, pady=1,bg='#DA1717',activebackground='#DA1717',command=lambda: self.Neg())
        self.btnNegative.grid(row=2, column=1, padx = (5,0), pady=(15,0))

        self.btnClear = Button(self.master, text='CE', font=('Helvetica', '20'), width=3, height=1,padx=1, pady=1,bg='#DA1717',activebackground='#DA1717',command=lambda: [self.Clear(), self.ChangeState()])
        self.btnClear.grid(row=2, column=2, padx = (5,0), pady=(15,0))

        image = Image.open(".\Images\Girl.jpg")
        resize_image = image.resize((200, 73))
        photo = ImageTk.PhotoImage(resize_image)

        self.lblImage = Label(self.master, image = photo, bg='black')
        self.lblImage.image = photo
        self.lblImage.grid(row=0, column=4, columnspan=2, rowspan=2,padx = (10,0), pady=(20,0))

        

    def Number(self, item):
        global expression
        global answer
        global results
        if expression == results:
            expression = ''
        if expression.__contains__('+'):
            expression = expression + str(item)
        elif expression.startswith('-'):
            expression = str(item)
        elif expression.__contains__('-'):
            expression = expression + str(item)
        elif expression.__contains__('/'):
            expression = expression + str(item)
        elif expression.__contains__('*'):
            expression = expression + str(item)
        elif expression.__contains__('.'):
            if expression == answer:
                expression = expression + str(item)
            else:
                expression = str(item)
        else:
            expression = expression + str(item)
        answer = answer + str(item)
        x.set(expression)
        y.set(answer)

    def Operator(self, item):
        global expression
        global answer
        if expression[-1:] == '+':
            expression = expression[:-1] + str(item)
        elif expression[-1:] == '-':
            expression = expression[:-1] + str(item)
        elif expression[-1:] == '/':
            expression = expression[:-1] + str(item)
        elif expression[-1:] == '*':
            expression = expression[:-1] + str(item)
        else:
            expression = expression + str(item)
        answer = ""
        x.set(expression)
        y.set(answer)

    def Decimal(self, item):
        global expression
        global answer
        if expression == results:
            expression = ''
        numlist = expression.split('+')
        numlist1 = expression.split('-')
        numlist2 = expression.split('/')
        numlist3 = expression.split('*')
        if '+' in expression and '.' not in numlist[-1]:
            expression = expression + str(item)
        elif '-' in expression and '.' not in numlist1[-1]:
            expression = expression + str(item)
        elif '/' in expression and '.' not in numlist2[-1]:
            expression = expression + str(item)    
        elif '*' in expression and '.' not in numlist3[-1]:
            expression = expression + str(item)
        elif '.' in expression:
            expression = expression
        else:
            expression = expression + str(item)
            
        if '.' in answer:
            answer = answer
        else:
            answer = answer + str(item)
        x.set(expression)
        y.set(answer)

    def Clear(self):
        global expression
        global answer
        expression = ""
        answer = ""
        x.set("")
        y.set("")
    
    def ClearAll(self):
        global expression
        global answer
        expression = ""
        answer = ""
        x.set("")
        y.set("")
        self.txtWork.delete(1.0, END)

    def Equal(self):
        global expression
        global answer
        global results
        expression2 = expression + ' ' + "="
        results = round(eval(expression), 12)
        if results - int(results) == 0:
            results = int(results)
            x.set(str(results))
        else:
            x.set(str(results))
        results = str(results)
        result2 = results
        expression4 = results
        answer = ""
        y.set("")
        if (result2 == expression):
            self.txtWork.insert(-1.0, result2)
        else:
            expression3 = expression2 +  ' ' + expression4 + '\n' + '\n'
            self.txtWork.insert(-1.0, expression3)
        expression = results
        self.btnEqual['state'] = DISABLED

    def Back(self):
        global expression
        global answer
        expression = expression[:-1]
        answer = answer[:-1]
        x.set(expression)
        y.set(answer)

    def Neg(self):
        global expression
        if (expression[:1] == '-'):
            expression = expression[1:]
        else:
            expression = '-' + expression
        x.set(expression)
    
    def ChangeState(self):
        if (self.btnEqual['state'] == DISABLED):
            self.btnEqual['state'] = NORMAL

if __name__ == "__main__":
    root = Tk()
    x = StringVar()
    y = StringVar()
    App = ParentWindow(root)
    root.mainloop()
