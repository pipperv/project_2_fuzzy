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
			 	    [("animal","es","cheetah"),0.9]),
			 "R13":([("animal","es","mamifero"),
			 		 ("animal","es","carnivoro"),
			 		 ("animal","tiene","rayas negras")],
			 	    [("animal","es","tigre"),0.85]),
			 "R14":([("animal","es","mamifero"),
			 		 ("animal","es","carnivoro"),
			 		 ("animal","es","domestico")],
			 	    [("animal","es","perro"),0.9]),
			 "R15":([("animal","es","reptil"),
			 		 ("animal","es","domestico")],
			 	    [("animal","es","tortuga"),0.7]),
			 "R16":([("animal","es","mamifero"),
			 		 ("animal","es","ungulado"),
			 		 ("animal","tiene","cuello largo")],
			 	    [("animal","es","jirafa"),1.0]),
			 "R17":([("animal","es","mamifero"),
			 		 ("animal","es","ungulado"),
			 		 ("animal","tiene","rayas negras")],
			 	    [("animal","es","cebra"),0.95]),
			 "R18":([("animal","es","mamifero"),
			 		 ("animal","puede","volar"),
			 		 ("animal","es","feo")],
			 	    [("animal","es","murcielago"),0.9]),
			 "R19":([("animal","es","ave"),
			 		 ("animal","vuela","bien")],
			 	    [("animal","es","gaviota"),0.9]),
			 "R20":([("animal","es","ave"),
			 		 ("animal","corre","rapido")],
			 	    [("animal","es","avestruz"),1.0]),
			 "R21":([("animal","es","ave"),
			 		 ("animal","es","parlanchin")],
			 	    [("animal","es","loro"),0.95]),
			 "R22":([("animal","es","mamifero"),
			 		 ("animal","es","grande"),
			 		 ("animal","es","ungulado"),
			 		 ("animal","tiene","trompa")],
			 	    [("animal","es","elefante"),0.9])}

hipothesis_base = [(("animal","es","perro"),0.0),
				   (("animal","es","murcielago"),0.0),
				   (("animal","es","tigre"),0.0),
				   (("animal","es","elefante"),0.0),
				   (("animal","es","cebra"),0.0),
				   (("animal","es","jirafa"),0.0),
				   (("animal","es","tortuga"),0.0),
				   (("animal","es","cheetah"),0.0),
				   (("animal","es","gaviota"),0.0),
				   (("animal","es","avestruz"),0.0),
				   (("animal","es","loro"),0.0),]

facts_base = []

def get_rule_base():
	return rule_base

def set_rule_base(X):
	rule_base = X

def get_hipothesis_base():
	return hipothesis_base

def set_hipothesis_base(X):
	hipothesis_base = X

def get_facts_base():
	return facts_base

def set_facts_base(X):
	facts_base = X

def get_actions_from_concl(concl):
	unzipped = zip(*concl)
	unzipped_list = list(unzipped)
	return unzipped_list[0]