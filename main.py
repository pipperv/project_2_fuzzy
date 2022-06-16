from init_global_var import *

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
			if H == fact and vc >= beta: Fh.append((fact,vc))
	else: return Fh
		
def mod_max(L):
	l_pos = [vc for vc in L if vc >= 0]
	l_neg = [vc for vc in L if vc < 0]
	

def check_proof(H):
	#Fase 1: Check Fact Base
	Fh = F(H)
	if len(Fh):
		vc_list = zip(*Fh)[1]
		

	for id in R(H):
		rule = rule_base[id]
		prem = rule[0]

		
