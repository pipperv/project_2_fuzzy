from init_global_var import *

def R(H):
	Rh = {}
	for id in rule_base:
		concl = rule_base[id][1]
		h_list = get_actions_from_concl(concl)
		if H in h_list: Rh[id] = rule_base[id]
	return Rh

def F(H):
	Fh = {}
	for fact in facts_base:


def check_rule_base(H):
