from tkinter import *
window=Tk()  #blank window create
window.title('My Window') #title of the window
window.geometry('300x300+0+0') #widthxheight+x+y
turn=1

def show1():
	global turn

	if  turn == 1:
		s1.set('X')
		turn=2
	else:
		s1.set('O')
		turn=1
	if (s1.get()=='X' and s2.get()=='X' and s3.get()=='X') or (s4.get()=='X' and s5.get()=='X' and s6.get()=='X') or (s7.get()=='X' and s8.get()=='X' and s9.get()=='X') or (s1.get()=='X' and s5.get()=='X' and s9.get()=='X') or (s1.get()=='X' and s4.get()=='X' and s7.get()=='X') or (s3.get()=='X' and s5.get()=='X' and s7.get()=='X') or (s2.get()=='X' and s5.get()=='X' and s8.get()=='X') or (s3.get()=='X' and s6.get()=='X' and s9.get()=='X'):
		print('P1 is winner(X)')

	if (s1.get() == 'O' and s2.get() == 'O' and s3.get() == 'O') or (
			s4.get() == 'O' and s5.get() == 'O' and s6.get() == 'O') or (
			s7.get() == 'O' and s8.get() == 'O' and s9.get() == 'O') or (
			s1.get() == 'O' and s5.get() == 'O' and s9.get() == 'O') or (
			s1.get() == 'O' and s4.get() == 'O' and s7.get() == 'O') or (
			s3.get() == 'O' and s5.get() == 'O' and s7.get() == 'O') or (
			s2.get() == 'O' and s5.get() == 'O' and s8.get() == 'O') or (
			s3.get() == 'O' and s6.get() == 'O' and s9.get() == 'O'):
		print('P2 is winner(O)')
	e1.config(state="disabled")

s1=StringVar()
e1=Button(textvariable=s1,command=show1)
e1.grid(row=0,column=0)

def show2():
	global turn
	if  turn == 1:
		s2.set('X')
		turn=2
	else:
		s2.set('O')
		turn=1

	if (s1.get() == 'X' and s2.get() == 'X' and s3.get() == 'X') or (
			s4.get() == 'X' and s5.get() == 'X' and s6.get() == 'X') or (
			s7.get() == 'X' and s8.get() == 'X' and s9.get() == 'X') or (
			s1.get() == 'X' and s5.get() == 'X' and s9.get() == 'X') or (
			s1.get() == 'X' and s4.get() == 'X' and s7.get() == 'X') or (
			s3.get() == 'X' and s5.get() == 'X' and s7.get() == 'X') or (
			s2.get() == 'X' and s5.get() == 'X' and s8.get() == 'X') or (
			s3.get() == 'X' and s6.get() == 'X' and s9.get() == 'X'):
		print('P1 is winner(X)')
	if (s1.get() == 'O' and s2.get() == 'O' and s3.get() == 'O') or (
			s4.get() == 'O' and s5.get() == 'O' and s6.get() == 'O') or (
			s7.get() == 'O' and s8.get() == 'O' and s9.get() == 'O') or (
			s1.get() == 'O' and s5.get() == 'O' and s9.get() == 'O') or (
			s1.get() == 'O' and s4.get() == 'O' and s7.get() == 'O') or (
			s3.get() == 'O' and s5.get() == 'O' and s7.get() == 'O') or (
			s2.get() == 'O' and s5.get() == 'O' and s8.get() == 'O') or (
			s3.get() == 'O' and s6.get() == 'O' and s9.get() == 'O'):
		print('P2 is winner(O)')
	e2.config(state="disabled")

s2=StringVar()
e2=Button(textvariable=s2,command=show2)
e2.grid(row=0,column=1)

def show3():
	global turn
	if  turn == 1:
		s3.set('X')
		turn=2
	else:
		s3.set('O')
		turn=1
	if (s1.get() == 'X' and s2.get() == 'X' and s3.get() == 'X') or (
			s4.get() == 'X' and s5.get() == 'X' and s6.get() == 'X') or (
			s7.get() == 'X' and s8.get() == 'X' and s9.get() == 'X') or (
			s1.get() == 'X' and s5.get() == 'X' and s9.get() == 'X') or (
			s1.get() == 'X' and s4.get() == 'X' and s7.get() == 'X') or (
			s3.get() == 'X' and s5.get() == 'X' and s7.get() == 'X') or (
			s2.get() == 'X' and s5.get() == 'X' and s8.get() == 'X') or (
			s3.get() == 'X' and s6.get() == 'X' and s9.get() == 'X'):
		print('P1 is winner(X)')
	if (s1.get() == 'O' and s2.get() == 'O' and s3.get() == 'O') or (
			s4.get() == 'O' and s5.get() == 'O' and s6.get() == 'O') or (
			s7.get() == 'O' and s8.get() == 'O' and s9.get() == 'O') or (
			s1.get() == 'O' and s5.get() == 'O' and s9.get() == 'O') or (
			s1.get() == 'O' and s4.get() == 'O' and s7.get() == 'O') or (
			s3.get() == 'O' and s5.get() == 'O' and s7.get() == 'O') or (
			s2.get() == 'O' and s5.get() == 'O' and s8.get() == 'O') or (
			s3.get() == 'O' and s6.get() == 'O' and s9.get() == 'O'):
		print('P2 is winner(O)')
	e3.config(state="disabled")


s3=StringVar()
e3=Button(textvariable=s3,command=show3)
e3.grid(row=0,column=2)

def show4():
	global turn
	if  turn == 1:
		s4.set('X')
		turn=2
	else:
		s4.set('O')
		turn=1

	if (s1.get() == 'X' and s2.get() == 'X' and s3.get() == 'X') or (
			s4.get() == 'X' and s5.get() == 'X' and s6.get() == 'X') or (
			s7.get() == 'X' and s8.get() == 'X' and s9.get() == 'X') or (
			s1.get() == 'X' and s5.get() == 'X' and s9.get() == 'X') or (
			s1.get() == 'X' and s4.get() == 'X' and s7.get() == 'X') or (
			s3.get() == 'X' and s5.get() == 'X' and s7.get() == 'X') or (
			s2.get() == 'X' and s5.get() == 'X' and s8.get() == 'X') or (
			s3.get() == 'X' and s6.get() == 'X' and s9.get() == 'X'):
		print('P1 is winner(X)')
	if (s1.get() == 'O' and s2.get() == 'O' and s3.get() == 'O') or (
			s4.get() == 'O' and s5.get() == 'O' and s6.get() == 'O') or (
			s7.get() == 'O' and s8.get() == 'O' and s9.get() == 'O') or (
			s1.get() == 'O' and s5.get() == 'O' and s9.get() == 'O') or (
			s1.get() == 'O' and s4.get() == 'O' and s7.get() == 'O') or (
			s3.get() == 'O' and s5.get() == 'O' and s7.get() == 'O') or (
			s2.get() == 'O' and s5.get() == 'O' and s8.get() == 'O') or (
			s3.get() == 'O' and s6.get() == 'O' and s9.get() == 'O'):
		print('P2 is winner(O)')

	e4.config(state="disabled")


s4=StringVar()
e4=Button(textvariable=s4,command=show4)
e4.grid(row=1,column=0)

def show5():
	global turn
	if  turn == 1:
		s5.set('X')
		turn=2
	else:
		s5.set('O')
		turn=1
	if (s1.get() == 'X' and s2.get() == 'X' and s3.get() == 'X') or (
			s4.get() == 'X' and s5.get() == 'X' and s6.get() == 'X') or (
			s7.get() == 'X' and s8.get() == 'X' and s9.get() == 'X') or (
			s1.get() == 'X' and s5.get() == 'X' and s9.get() == 'X') or (
			s1.get() == 'X' and s4.get() == 'X' and s7.get() == 'X') or (
			s3.get() == 'X' and s5.get() == 'X' and s7.get() == 'X') or (
			s2.get() == 'X' and s5.get() == 'X' and s8.get() == 'X') or (
			s3.get() == 'X' and s6.get() == 'X' and s9.get() == 'X'):
		print('P1 is winner(X)')
	if (s1.get() == 'O' and s2.get() == 'O' and s3.get() == 'O') or (
			s4.get() == 'O' and s5.get() == 'O' and s6.get() == 'O') or (
			s7.get() == 'O' and s8.get() == 'O' and s9.get() == 'O') or (
			s1.get() == 'O' and s5.get() == 'O' and s9.get() == 'O') or (
			s1.get() == 'O' and s4.get() == 'O' and s7.get() == 'O') or (
			s3.get() == 'O' and s5.get() == 'O' and s7.get() == 'O') or (
			s2.get() == 'O' and s5.get() == 'O' and s8.get() == 'O') or (
			s3.get() == 'O' and s6.get() == 'O' and s9.get() == 'O'):
		print('P2 is winner(O)')
	e5.config(state="disabled")


s5=StringVar()
e5=Button(textvariable=s5,command=show5)
e5.grid(row=1,column=1)

def show6():
	global turn
	if  turn == 1:
		s6.set('X')
		turn=2
	else:
		s6.set('O')
		turn=1
	if (s1.get() == 'X' and s2.get() == 'X' and s3.get() == 'X') or (
			s4.get() == 'X' and s5.get() == 'X' and s6.get() == 'X') or (
			s7.get() == 'X' and s8.get() == 'X' and s9.get() == 'X') or (
			s1.get() == 'X' and s5.get() == 'X' and s9.get() == 'X') or (
			s1.get() == 'X' and s4.get() == 'X' and s7.get() == 'X') or (
			s3.get() == 'X' and s5.get() == 'X' and s7.get() == 'X') or (
			s2.get() == 'X' and s5.get() == 'X' and s8.get() == 'X') or (
			s3.get() == 'X' and s6.get() == 'X' and s9.get() == 'X'):
		print('P1 is winner(X)')
	if (s1.get() == 'O' and s2.get() == 'O' and s3.get() == 'O') or (
			s4.get() == 'O' and s5.get() == 'O' and s6.get() == 'O') or (
			s7.get() == 'O' and s8.get() == 'O' and s9.get() == 'O') or (
			s1.get() == 'O' and s5.get() == 'O' and s9.get() == 'O') or (
			s1.get() == 'O' and s4.get() == 'O' and s7.get() == 'O') or (
			s3.get() == 'O' and s5.get() == 'O' and s7.get() == 'O') or (
			s2.get() == 'O' and s5.get() == 'O' and s8.get() == 'O') or (
			s3.get() == 'O' and s6.get() == 'O' and s9.get() == 'O'):
		print('P2 is winner(O)')
	e6.config(state="disabled")


s6=StringVar()
e6=Button(textvariable=s6,command=show6)
e6.grid(row=1,column=2)

def show7():
	global turn
	if  turn == 1:
		s7.set('X')
		turn=2
	else:
		s7.set('O')
		turn=1
	if (s1.get() == 'X' and s2.get() == 'X' and s3.get() == 'X') or (
			s4.get() == 'X' and s5.get() == 'X' and s6.get() == 'X') or (
			s7.get() == 'X' and s8.get() == 'X' and s9.get() == 'X') or (
			s1.get() == 'X' and s5.get() == 'X' and s9.get() == 'X') or (
			s1.get() == 'X' and s4.get() == 'X' and s7.get() == 'X') or (
			s3.get() == 'X' and s5.get() == 'X' and s7.get() == 'X') or (
			s2.get() == 'X' and s5.get() == 'X' and s8.get() == 'X') or (
			s3.get() == 'X' and s6.get() == 'X' and s9.get() == 'X'):
		print('P1 is winner(X)')

	if (s1.get() == 'O' and s2.get() == 'O' and s3.get() == 'O') or (
			s4.get() == 'O' and s5.get() == 'O' and s6.get() == 'O') or (
			s7.get() == 'O' and s8.get() == 'O' and s9.get() == 'O') or (
			s1.get() == 'O' and s5.get() == 'O' and s9.get() == 'O') or (
			s1.get() == 'O' and s4.get() == 'O' and s7.get() == 'O') or (
			s3.get() == 'O' and s5.get() == 'O' and s7.get() == 'O') or (
			s2.get() == 'O' and s5.get() == 'O' and s8.get() == 'O') or (
			s3.get() == 'O' and s6.get() == 'O' and s9.get() == 'O'):
		print('P2 is winner(O)')
	e7.config(state="disabled")


s7=StringVar()
e7=Button(textvariable=s7,command=show7)
e7.grid(row=2,column=0)

def show8():
	global turn
	if  turn == 1:
		s8.set('X')
		turn=2
	else:
		s8.set('O')
		turn=1

	if (s1.get() == 'X' and s2.get() == 'X' and s3.get() == 'X') or (
			s4.get() == 'X' and s5.get() == 'X' and s6.get() == 'X') or (
			s7.get() == 'X' and s8.get() == 'X' and s9.get() == 'X') or (
			s1.get() == 'X' and s5.get() == 'X' and s9.get() == 'X') or (
			s1.get() == 'X' and s4.get() == 'X' and s7.get() == 'X') or (
			s3.get() == 'X' and s5.get() == 'X' and s7.get() == 'X') or (
			s2.get() == 'X' and s5.get() == 'X' and s8.get() == 'X') or (
			s3.get() == 'X' and s6.get() == 'X' and s9.get() == 'X'):
		print('P1 is winner(X)')

	if (s1.get() == 'O' and s2.get() == 'O' and s3.get() == 'O') or (
			s4.get() == 'O' and s5.get() == 'O' and s6.get() == 'O') or (
			s7.get() == 'O' and s8.get() == 'O' and s9.get() == 'O') or (
			s1.get() == 'O' and s5.get() == 'O' and s9.get() == 'O') or (
			s1.get() == 'O' and s4.get() == 'O' and s7.get() == 'O') or (
			s3.get() == 'O' and s5.get() == 'O' and s7.get() == 'O') or (
			s2.get() == 'O' and s5.get() == 'O' and s8.get() == 'O') or (
			s3.get() == 'O' and s6.get() == 'O' and s9.get() == 'O'):
		print('P2 is winner(O)')
	e8.config(state="disabled")



s8=StringVar()
e8=Button(textvariable=s8,command=show8)
e8.grid(row=2,column=1)

def show9():
	global turn
	if  turn == 1:
		s9.set('X')
		turn=2
	else:
		s9.set('O')
		turn=1
	if (s1.get() == 'X' and s2.get() == 'X' and s3.get() == 'X') or (
			s4.get() == 'X' and s5.get() == 'X' and s6.get() == 'X') or (
			s7.get() == 'X' and s8.get() == 'X' and s9.get() == 'X') or (
			s1.get() == 'X' and s5.get() == 'X' and s9.get() == 'X') or (
			s1.get() == 'X' and s4.get() == 'X' and s7.get() == 'X') or (
			s3.get() == 'X' and s5.get() == 'X' and s7.get() == 'X') or (
			s2.get() == 'X' and s5.get() == 'X' and s8.get() == 'X') or (
			s3.get() == 'X' and s6.get() == 'X' and s9.get() == 'X'):
		print('P1 is winner(X)')

	if (s1.get() == 'O' and s2.get() == 'O' and s3.get() == 'O') or (
			s4.get() == 'O' and s5.get() == 'O' and s6.get() == 'O') or (
			s7.get() == 'O' and s8.get() == 'O' and s9.get() == 'O') or (
			s1.get() == 'O' and s5.get() == 'O' and s9.get() == 'O') or (
			s1.get() == 'O' and s4.get() == 'O' and s7.get() == 'O') or (
			s3.get() == 'O' and s5.get() == 'O' and s7.get() == 'O') or (
			s2.get() == 'O' and s5.get() == 'O' and s8.get() == 'O') or (
			s3.get() == 'O' and s6.get() == 'O' and s9.get() == 'O'):
		print('P2 is winner(O)')
	e9.config(state="disabled")

s9=StringVar()
e9=Button(textvariable=s9,command=show9)
e9.grid(row=2,column=2)


window.mainloop()