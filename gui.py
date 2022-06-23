from tkinter import *
from PIL import Image, ImageTk
import sys

rule_base = {"R1":([("animal","tiene","pelo")],
				   [(("animal","es","mamifero"),0.8),
				    (("animal","es","ave"),-1.0),
				    (("animal","es","reptil"),-1.0)]),
			 "R2":([("animal","da","leche")],
				   [(("animal","es","mamifero"),1.0),
				    (("animal","es","ave"),-1.0),
				    (("animal","es","reptil"),-1.0)]),
			 "R3":([("animal","pone","huevos"),
			 		("animal","tiene","piel dura")],
				   [(("animal","es","mamifero"),-1.0),
				    (("animal","es","ave"),-1.0),
				    (("animal","es","reptil"),1.0)]),
			 "R4":([("animal","pone","huevos"),
			 		("animal","puede","volar")],
				   [(("animal","es","ave"),1.0),
				    (("animal","es","reptil"),-1.0)]),
			 "R5":([("animal","tiene","plumas")],
				   [(("animal","es","mamifero"),-1.0),
				    (("animal","es","ave"),1.0),
				    (("animal","es","reptil"),-1.0)]),
			 "R6":([("animal","come","carne")],
			 	   [(("animal","es","carnivoro"),1.0)]),
			 "R7":([("animal","tiene","garras")],
			 	   [(("animal","es","carnivoro"),0.8)]),
			 "R8":([("animal","es","mamifero"),
			 		("animal","tiene","pezuñas")],
				   [(("animal","es","ungulado"),1.0)]),
			 "R9":([("animal","es","mamifero"),
			 		("animal","es","rumiante")],
				   [(("animal","es","ungulado"),0.75)]),
			 "R10":([("animal","vive","con personas")],
			 	    [(("animal","es","domestico"),0.9)]),
			 "R11":([("animal","vive","en zoologico")],
			 	    [(("animal","es","domestico"),-0.8)]),
			 "R12":([("animal","es","mamifero"),
			 		 ("animal","es","carnivoro"),
			 		 ("animal","tiene","manchas oscuras")],
			 	    [(("animal","es","cheetah"),0.9)]),
			 "R13":([("animal","es","mamifero"),
			 		 ("animal","es","carnivoro"),
			 		 ("animal","tiene","rayas negras")],
			 	    [(("animal","es","tigre"),0.85)]),
			 "R14":([("animal","es","mamifero"),
			 		 ("animal","es","carnivoro"),
			 		 ("animal","es","domestico")],
			 	    [(("animal","es","perro"),0.9)]),
			 "R15":([("animal","es","reptil"),
			 		 ("animal","es","domestico")],
			 	    [(("animal","es","tortuga"),0.7)]),
			 "R16":([("animal","es","mamifero"),
			 		 ("animal","es","ungulado"),
			 		 ("animal","tiene","cuello largo")],
			 	    [(("animal","es","jirafa"),1.0)]),
			 "R17":([("animal","es","mamifero"),
			 		 ("animal","es","ungulado"),
			 		 ("animal","tiene","rayas negras")],
			 	    [(("animal","es","cebra"),0.95)]),
			 "R18":([("animal","es","mamifero"),
			 		 ("animal","puede","volar"),
			 		 ("animal","es","feo")],
			 	    [(("animal","es","murcielago"),0.9)]),
			 "R19":([("animal","es","ave"),
			 		 ("animal","vuela","bien")],
			 	    [(("animal","es","gaviota"),0.9)]),
			 "R20":([("animal","es","ave"),
			 		 ("animal","corre","rapido")],
			 	    [(("animal","es","avestruz"),1.0)]),
			 "R21":([("animal","es","ave"),
			 		 ("animal","es","parlanchin")],
			 	    [(("animal","es","loro"),0.95)]),
			 "R22":([("animal","es","mamifero"),
			 		 ("animal","es","grande"),
			 		 ("animal","es","ungulado"),
			 		 ("animal","tiene","trompa")],
			 	    [(("animal","es","elefante"),0.9)])}

hipothesis_base = {("animal","es","perro"):0.0,
				   ("animal","es","murcielago"):0.0,
				   ("animal","es","tigre"):0.0,
				   ("animal","es","elefante"):0.0,
				   ("animal","es","cebra"):0.0,
				   ("animal","es","jirafa"):0.0,
				   ("animal","es","tortuga"):0.0,
				   ("animal","es","cheetah"):0.0,
				   ("animal","es","gaviota"):0.0,
				   ("animal","es","avestruz"):0.0,
				   ("animal","es","loro"):0.0}

facts_base = []

alpha = 0.7
beta = 0.2
gamma = 0.85
epsilon = 0.5
delta_nom = 0.2

mark = {} # Marcador de Conclusiones (Opcional 5.2)

def init():
	for h in hipothesis_base:
		hipothesis_base[h] = 0.0
	facts_base = []
	mark = {}

def R(H):
	Rh = {}
	for id in rule_base:
		concl = rule_base[id][1]
		for h, vc in concl:
			if H == h and abs(vc) >= epsilon: Rh[id] = rule_base[id]
	return Rh

def F(H):
	Fh = []
	if len(facts_base):
		for fact, vc in facts_base:
			if H == fact and abs(vc) >= beta: Fh.append((fact,vc))
		return Fh
	else: return Fh

def ask_user(H):
	q = f"¿Con que certeza el {H[0]} {H[1]} {H[2]}? "
	q_var.set(q)
	button.wait_variable(ans_var)
	vc = float(ans_var.get())
	return vc

def disyuncion(L):
	l_pos = [vc for vc in L if vc >= 0]
	l_neg = [vc for vc in L if vc < 0]
	p , n = 0 , 0
	if len(l_pos): p = max(l_pos)
	if len(l_neg): n = min(l_neg)
	if abs(n) > p : return n
	else: return p

def conjuncion(L):
	l_pos = [vc for vc in L if vc >= 0]
	l_neg = [vc for vc in L if vc < 0]
	if len(l_pos):
		p = min(l_pos)
		if len(l_neg):
			n = max(l_neg)
			if abs(n) <= p : return n
		return p
	elif len(l_neg):
		n = max(l_neg)
		return n

# Prefcalificador de Reglas (Opcional 5.1)
def precalif(prem):
	for claus in prem:
		Fh = F(claus)
		if len(Fh):
			vc_list = list(zip(*Fh))[1]
			if disyuncion(vc_list) < beta: return False
	return True

def check_proof(H,rule_precalif=False):
	#Fase 1: Check Fact Base
	Fh = F(H)
	if len(Fh):
		vc_list = list(zip(*Fh))[1]
		vc = disyuncion(vc_list)
		return ( H , vc )
		
	#Fase 2: Check Rule Base
	Rh = R(H)
	if len(Rh):
		for id in Rh:
			rule = rule_base[id]
			prem = rule[0]
			#PRECALIFICADOR DE LA REGLA (Opcional 5.1):
			if rule_precalif:
				continuar = precalif(prem)
			else:
				continuar = True
			#Precalificador aproves!!
			if continuar: 
				concl = rule[1]
				vc_list = []
				for accion in concl:
					if H == accion[0]:
						vc_rule = accion[1]
				delta = delta_nom / vc_rule
				vc_prem = 0.0
				for claus in prem:
					trip_claus = check_proof(claus)
					if trip_claus is not None:
						vc_claus = trip_claus[1]
						if vc_claus < beta: # La clausula falla
							vc_prem = vc_claus
							break
						vc_list.append(vc_claus)
						vc_prem = min(vc_list)
				if abs(vc_prem) >= delta:
					vc = vc_prem * vc_rule
					facts_base.append(( H , vc ))
					if abs(vc) >= gamma: return ( H , vc )
		# Si se evaluaron todas las reglas, se revisa la base de hechos
		Fh = F(H)
		if len(Fh):
			vc_list = list(zip(*Fh))[1]
			vc = disyuncion(vc_list)
			return ( H , vc )

	#Fase 3: Ask User
	if not len(Rh):
		if H not in mark: #Revisa el Marcador de Conclusiones (Opcional 5.2)
			vc = float(ask_user(H))
			facts_base.append(( H , vc ))
			# Anota la conclusion en el marcador si el valor de certeza es menor a beta.
			if abs(vc) < beta: mark[H] = vc
			return ( H , vc )

def AEI(d1=True,rule_precalif=True):
	for h in hipothesis_base:
		H = check_proof(h,rule_precalif)
		if H is not None:
			vc = H[1]
			hipothesis_base[h] = vc
			if d1 and vc >= alpha:
				ans = f"El {H[0][0]} {H[0][1]} {H[0][2]} con certeza {vc:.2f}."
				path = f"img/{H[0][2]}.jpg"
				final_var.set(ans)
				display_image(path)
				return
	max_vc = 0.0
	for h in hipothesis_base:
		vc = hipothesis_base[h]
		if vc > max_vc:
			best_h = h
			max_vc = vc
	ans = f"El {best_h[0]} {best_h[1]} {best_h[2]} con certeza {max_vc:.2f}."
	path = f"img/{best_h[2]}.jpg"
	final_var.set(ans)
	display_image(path)
	return

import tkinter

def send_value():
	value = scale.get()
	ans_var.set(str(value))
	scale.set(0.00)

def display_image(img_path):
	image = Image.open(img_path)
	image = image.resize((300, 300), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(image)
	photo = Label(master,image=img)
	photo.image = img
	photo.grid(row=5,column=2)

def init_img():
	image = Image.open("img/empty.jpg")
	image = image.resize((300, 300), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(image)
	photo = Label(master,image=img)
	photo.image = img
	photo.grid(row=5,column=2)

def start():
	AEI()

def restart_aei():
	init_img()
	final_var.set('')
	init()
	start()

master=tkinter.Tk()
master.title("AEI para adivinar Animalitos")
master.geometry("420x720")

q_var = StringVar()
q_var.set('Presione el boton "Start" para empezar')

ans_var = StringVar()
final_var = StringVar()
final_var.set('')

q_label=Label(master, textvariable=q_var)
q_label.grid(row=2,column=2)

scale=Scale(master, from_=-1.0, to=1.0, resolution=0.01, length=300 , orient=HORIZONTAL)
scale.grid(row=3,column=2)

button=tkinter.Button(master, text="Enviar", command=send_value)
button.grid(row=3,column=3)

frame=tkinter.Frame(master, width=40, height=40)
frame.grid(row=1,column=1)

final_label=Label(master, textvariable=final_var)
final_label.grid(row=4,column=2)

init_img()

button_r=tkinter.Button(master, text="Reiniciar", command=restart_aei)
button_r.grid(row=6,column=2)

master.after(500, start())
master.mainloop()