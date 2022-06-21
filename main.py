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
			if H == fact and abs(vc) >= beta: Fh.append((fact,vc))
		return Fh
	else: return Fh

def ask_user(H):
	q = f"¿Con que certeza el {H[0]} {H[1]} {H[2]}? "
	vc = input(q)
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

def check_proof(H):
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
			concl = rule[1]
			vc_list = []
			for p in prem:
				hip = check_proof(p)
				vc_list.append(hip[1])
			vc_prem = min(vc_list)
			for c in concl:
				vc_rule = c[1]
				if H == c[0]: Hvc = vc_prem * vc_rule
				vc = vc_prem * vc_rule
				facts_base.append(( c[0] , vc ))
			return ( H , Hvc )

	#Fase 3: Ask User
	if not len(Rh):
		vc = float(ask_user(H))
		facts_base.append(( H , vc ))
		return ( H , vc )

def AEI(d1=True):
	for h in hipothesis_base:
		H = check_proof(h)
		vc = H[1]
		hipothesis_base[h] = vc
		if d1 and vc >= alpha:
			ans = f"El {H[0][0]} {H[0][1]} {H[0][2]} con certeza {vc}."
			print(ans)
			return
	max_vc = 0.0
	for h in hipothesis_base:
		vc = hipothesis_base[h]
		if vc > max_vc:
			best_h = h
			max_vc = vc
	ans = f"El {best_h[0]} {best_h[1]} {best_h[2]} con certeza {max_vc}."
	print(ans)
	return