name=input("name :")
cost=0
types_="none"
pick="none"
types='choose among groceries,deos,snacks,fruits :'
groceries={"rice":1000,"maize":100,"bread":50,"salt":15,"dal":60,"checkout":"checkout"}
deos={'wildstone':300,'axe' :332,'engage':250,"axe chocolate":304,"checkout":"checkout"}
snacks={'oreo':30,'lays':20,'kurkure':20,"cheetohs":20,"nachos":20,"darkfantasy":30,"dairymilksilk":65,"checkout":"checkout"}
fruits={'apple':50,'orange':10,'banana':5,"guava":10,"strawberries":10,"checkout":"checkout"}
while types_!="checkout":
	types_=input(types)
	if types_ == "groceries" :
		pick="none"
		while pick!="checkout":
			try:	
				pick=groceries[input(groceries.keys())]
				if pick!="checkout":
					q=int(input("quantity :"))
					cost=cost+pick*q
				else:
					break
					pick="none"
			except(KeyError,ValueError):
				print("select a valid option")
				continue
	elif types_ == "deos" :
		pick="none"
		while pick!="checkout":
			try:	
				pick=deos[input(deos.keys())]
				if pick!="checkout":
					q=int(input("quantity :"))
					cost=cost+pick*q
				else:
					break
					pick="none"
			except(KeyError,ValueError):
				print("select a valid option")
				continue
	elif types_ == "fruits" :
		pick="none"
		while pick!="checkout":
			try:
				pick=fruits[input(fruits.keys())]
				if pick!="checkout":
					q=int(input("quantity :"))
					cost=cost+pick*q
				else:
					break
					pick="none"
			except(KeyError,ValueError):
				print("select a valid option")
				continue
	elif types_ == "snacks":
		pick="none"
		while pick!="checkout":
			try:
				pick=snacks[input(snacks.keys())]
				if pick!="checkout":
					q=int(input("quantity :"))
					cost=cost+pick*q
				else:
					break
					pick="none"
			except(KeyError,ValueError):
				print("select a valid option")
				continue
	elif types_== "checkout":
		break
	else :
		print("please give a valid input else checkout")
print("your bill amount :",cost)
