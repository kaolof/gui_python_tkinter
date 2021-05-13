# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren/
#Dibujo en Tkinter Canvas

from tkinter import Canvas, Tk,LAST, Button, filedialog, messagebox
import PIL.ImageGrab as ImageGrab
from math import cos, sin, radians, pi

ventana = Tk()
ventana.title('Dibujo en Python')
ventana.geometry('600x620+400+50')
ventana.config(bg='black')
ventana.resizable(0,0)


canvas = Canvas(ventana, bg= 'black', width = 570, height =570, relief ='raised', bd =4)
canvas.grid(column=0,row=0, columnspan=2, padx=5, pady = 5)

j =0
def dibujo(j): 
	canvas.create_oval(150,150,450,450, fill='black', outline='orange', width=6, activeoutline='dark violet', activefill='gray12')
	canvas.create_oval(180,180,420,420, fill='black', outline='magenta', width=6, activeoutline='dark violet', activefill='gray12')

	for y in range(12):
		canvas.create_text(300 - 133*sin(((y+1)*2*pi)/12), 300  - 133*cos(((y+1)*2*pi)/12), text= '•', 
			font=('Arial',15, 'bold'), fill ='deep sky blue')
	for x in range(12):
		canvas.create_text(300 - 133*sin(((x+1)*2*pi)/12), 300  - 133*cos(((x+1)*2*pi)/12), text= '☼', 
			font=('Arial',25, 'bold'), fill ='yellow')

    # lineas  ☼
	canvas.create_line(300,300, 300 + 120*sin(radians(j+180)), 150 - 120*cos(radians(j+180)), fill='green2',width=3,arrow= LAST)
	canvas.create_line(300,300, 150 + 120*sin(radians(j+90)), 300 - 120*cos(radians(j+90)), fill='green2',width=3,arrow= LAST)
	canvas.create_line(300,300, 450 + 120*sin(radians(j-90)), 300 - 120*cos(radians(j-90)), fill='green2',width=3,arrow= LAST)
	canvas.create_line(300,300, 300 + 120*sin(radians(j)), 450 - 120*cos(radians(j)), fill='green2',width=3,arrow= LAST)

	canvas.create_oval(290,290,310,310, fill='gold' , outline ='black', width=2)


def guardar_dibujo():
	try: 
		filename = filedialog.asksaveasfilename(defaultextension='.png')
		x = ventana.winfo_rootx() + canvas.winfo_x()
		y = (ventana.winfo_rooty() + canvas.winfo_y())

		x1 = x + canvas.winfo_width()
		y1 = y + canvas.winfo_height()

		ImageGrab.grab().crop((x, y, x1, y1)).save(filename)
		messagebox.showinfo('Guardar Dibujo',
			'Imagen guardada en: ' + str(filename) )
	except:
		messagebox.showerror('Guardar Dibujo', 
			'Imagen no guardada\n Error')

def iniciar():
	global j
	j = j + 5
	dibujo(j)
	x = canvas.after(100, iniciar)
	if j ==360:
		canvas.after_cancel(x)
		j = 0

Button(ventana, text= 'Iniciar', bg= 'green2', command=iniciar).grid(column=0,row=1, pady =2)
Button(ventana, text= 'Guardar Imagen', bg= 'blue', command=guardar_dibujo).grid(column=1,row=1, padx=50)

ventana.mainloop()
