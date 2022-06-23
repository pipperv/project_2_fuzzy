from tkinter import *
from init_global_var import *
import sys

init_rule_base = rule_base.copy()
init_hipothesis_base =hipothesis_base.copy()
init_facts_base = facts_base.copy()
mark = {} # Marcador de Conclusiones (Opcional 5.2)

def init():
	rule_base = init_rule_base
	hipothesis_base = init_hipothesis_base
	facts_base = init_facts_base

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
	print(q)
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
	init()
	for h in hipothesis_base:
		H = check_proof(h,rule_precalif)
		if H is not None:
			vc = H[1]
			hipothesis_base[h] = vc
			if d1 and vc >= alpha:
				ans = f"El {H[0][0]} {H[0][1]} {H[0][2]} con certeza {vc:.2f}."
				final_var.set(ans)
				print(ans)
				return
	max_vc = 0.0
	for h in hipothesis_base:
		vc = hipothesis_base[h]
		if vc > max_vc:
			best_h = h
			max_vc = vc
	ans = f"El {best_h[0]} {best_h[1]} {best_h[2]} con certeza {max_vc:.2f}."
	final_var.set(ans)
	print(ans)
	return

import tkinter

def send_value():
	value = scale.get()
	ans_var.set(str(value))
	scale.set(0.00)

def start():
	AEI()

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

button=tkinter.Button(master, text="Start", command=start)
button.grid(row=1,column=1)

final_label=Label(master, textvariable=final_var)
final_label.grid(row=4,column=2)

master.after(500, start())
master.mainloop()