from random import randint
from tkinter import *


win = Tk()
win.title('Генератор примеров')
win.geometry('500x250')

l = Label(win, text='Количество примеров:', font='Times 15')
l.grid(sticky='w', column=0, row=0)
l2 = Label(win, text='Уровень сложности:', font='Times 15')
l2.grid(sticky='w', column=0, row=1)
l3 = Label(win, text='Кол-во знаков после запятой:', font='Times 15')
l3.grid(sticky='w', column=0, row=2)
e = Entry(win, font='Times 15')
e.grid(sticky='w', column=1, row=0)
e.insert(0, '10')
e2 = Entry(win, font='Times 15')
e2.grid(sticky='w', column=1, row=1)
e2.insert(0, '1')
e3 = Entry(win, font='Times 15')
e3.grid(sticky='w', column=1, row=2)
e3.insert(0, '2')



l4 = Label(win, text='Сохранить примеры в папку...', font='Times 15')
l4.grid(sticky='w', column=0, row=3)
l5=Label(win, text='Сохранить ответы в папку...', font='Times 15')
l5.grid(sticky='w', column=0, row=4)
e4=Entry(win, font='Times 15')
e4.grid(sticky='w', column=1, row=3)
e4.insert(0, 'results/')
e5=Entry(win, font='Times 15')
e5.grid(sticky='w', column=1, row=4)
e5.insert(0, 'results/')


s = ''
def run():
	global s
	f = open('templates/temple' + e2.get() + '.txt')
	op = [' + ', ' - ', ' * ']
	m = []
	for line in f:
		m.append(line)
	f.close()
	f = open(e4.get() + 'vr.txt', 'w')
	an = open(e5.get() + 'results/ans.txt', 'w')
	def p():
		global s
		bar = int(e3.get())
		x = randint(1, 10 * (10 ** bar)) / (10 ** bar)
		a = randint(1, 50)
		v = m[randint(0, len(m) - 1)]
		v = v[:-1]
		v = v.replace('x', str(x)).replace('a', str(a))
		try:
			v2 = v[v.find('['):v.find(']') + 1]
			v3 = str(round(eval(v2[1:-1]), bar))
			if float(v3) < 0:
				v3 = '(' + v3 + ')'
			v = v.replace(v2, v3)
		except SyntaxError:
			pass
		s += v
	for j in range(int(e.get())):
		p()
		n = randint(1, 4)
		for i in range(n):
			s += op[randint(0, len(op) - 1)]
			p()
		ans = eval(s)
		if int(ans) == ans:
			ans = int(ans)
		s = str(j + 1) + '.  ' + s + ' = ' + '\n' * 3
		f.write(s)
		an.write(str(j + 1) + '.  ' + str(ans) + '\n' * 3)
		s = ''
	f.close()
	an.close()


def tips():
	t = open('tips.txt', 'r', encoding='UTF-8')
	win2 = Tk()
	win2.title('Инструкция')
	win2.geometry('700x600')
	i = 0
	fr = Frame(win2)
	for line in t:
		j = Label(fr, text=line, font='Times 13', height=2)
		j.grid(column=0, pady=0, sticky='w')
		i += 1
	i = 0
	fr.grid(column=0, row=0)
	t.close()


but = Button(win, text='Сгенерировать', command=run, font='Times 15')
but.grid(sticky='w', column=0, row=5)
tip = Button(win, text='Инструкция', command=tips, font='Times 15')
tip.grid(sticky='w', column=1, row=5)
win.mainloop()
