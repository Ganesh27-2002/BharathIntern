
from tkinter import *
expression = ""
def press(num):
	global expression

	expression = expression + str(num)

	equation.set(expression)
def equalpress():

	try:

		global expression

		total = str(eval(expression))

		equation.set(total)

		expression = ""

	except:

		equation.set(" error ")
		expression = ""

def clear():
	global expression
	expression = ""
	equation.set("")

if __name__ == "__main__":
	
	gui = Tk()

	gui.configure(background="light blue")

	gui.title("Calculator")

	gui.geometry("410x260")

	equation = StringVar()

	# expression_field = Entry(gui, textvariable=equation)
	expressionfield = Entry(gui, textvariable=equation, font=('Helvetica', 10))


	expressionfield.grid(columnspan=4, ipadx=128)

	btn1 = Button(gui, text=' 1 ', fg='black', bg='light green',
					command=lambda: press(1), height=2, width=12)
	btn1.grid(row=2, column=0)

	btn2 = Button(gui, text=' 2 ', fg='black', bg='light green',
					command=lambda: press(2), height=2, width=12)
	btn2.grid(row=2, column=1)

	btn3 = Button(gui, text=' 3 ', fg='black', bg='light green',
					command=lambda: press(3), height=2, width=12)
	btn3.grid(row=2, column=2)

	btn4 = Button(gui, text=' 4 ', fg='black', bg='light green',
					command=lambda: press(4), height=2, width=12)
	btn4.grid(row=3, column=0)

	btn5 = Button(gui, text=' 5 ', fg='black', bg='light green',
					command=lambda: press(5), height=2, width=12)
	btn5.grid(row=3, column=1)

	btn6 = Button(gui, text=' 6 ', fg='black', bg='light green',
					command=lambda: press(6), height=2, width=12)
	btn6.grid(row=3, column=2)

	btn7 = Button(gui, text=' 7 ', fg='black', bg='light green',
					command=lambda: press(7), height=2, width=12)
	btn7.grid(row=4, column=0)

	btn8 = Button(gui, text=' 8 ', fg='black', bg='light green',
					command=lambda: press(8), height=2, width=12)
	btn8.grid(row=4, column=1)

	btn9 = Button(gui, text=' 9 ', fg='black', bg='light green',
					command=lambda: press(9), height=2, width=12)
	btn9.grid(row=4, column=2)

	btn0 = Button(gui, text=' 0 ', fg='black', bg='light green',
					command=lambda: press(0), height=2, width=12)
	btn0.grid(row=5, column=0)

	plus = Button(gui, text=' + ', fg='black', bg='orange',
				command=lambda: press("+"), height=2, width=12)
	plus.grid(row=2, column=3)

	minus = Button(gui, text=' - ', fg='black', bg='orange',
				command=lambda: press("-"), height=2, width=12)
	minus.grid(row=3, column=3)

	multiply = Button(gui, text=' * ', fg='black', bg='orange',
					command=lambda: press("*"), height=2, width=12)
	multiply.grid(row=4, column=3)

	divide = Button(gui, text=' / ', fg='black', bg='orange',
					command=lambda: press("/"), height=2, width=12)
	divide.grid(row=5, column=3)

	equal = Button(gui, text=' = ', fg='black', bg='light yellow',
				command=equalpress, height=2, width=12)
	equal.grid(row=5, column=2)

	clear = Button(gui, text='Clear', fg='black', bg='orange',
				command=clear, height=2, width=12)
	clear.grid(row=5, column='1')

	Decimal= Button(gui, text='.', fg='black', bg='orange',
					command=lambda: press('.'), height=2, width=12)
	Decimal.grid(row=6, column=0)
	gui.mainloop() 
