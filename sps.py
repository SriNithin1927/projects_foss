import random
p=int(input("one player or two players : "))
while True:
	if p==1:
		n=input("player name : ")
		break
	elif p==2 :
		n=input("player1 name : ")
		k=input("player1 name : ")
		break
	else :
		print("choose only 1 or 2 players")
		p=int(input("one player or two players : "))
score=0
cpu=0
score2=0
a=["stone","paper","scissors"]
x=int(input("final score to win : "))
if p==1 :
	while True:
		if score == x or cpu == x:
			break
		b=input("choose : ")
		c=random.choice(a)
		print("cpu : "+c)
		if b!=a[1] and b!=a[0] and b!=a[2]:
			print("select among scissors stone and paper only")
		elif b=="stone" and c=="scissors" :
			score=score+1
			print("plus 1 to "+n)
			print("your score "+str(score))
			print("cpu score "+str(cpu))
		elif b=="paper" and c=="stone" :
			score=score+1
			print("plus 1 to "+n)
			print("your score "+str(score))
			print("cpu score "+str(cpu))
		elif b=="scissors" and c=="paper" :
			score=score+1
			print("plus 1 to "+n)
			print("your score "+str(score))
			print("cpu score "+str(cpu))
		elif c=="paper" and b=="stone" :
			cpu=cpu+1
			print("plus 1 to cpu")
			print("your score "+str(score))
			print("cpu score "+str(cpu))
		elif c=="scissors" and b=="paper" :
			cpu=cpu+1
			print("plus 1 to cpu")
			print("your score "+str(score))
			print("cpu score "+str(cpu))
		elif c=="stone" and b=="scissors" :
			cpu=cpu+1
			print("plus 1 to cpu")
			print("your score "+str(score))
			print("cpu score "+str(cpu))
	print("your total score "+str(score))
	print("cpu total score "+str(cpu))
	if cpu>score :
		print("better luck next time")
	else :
		print("winner winner chicken dinner congrats "+n)
elif p==2:
	while True:
		if score == x or cpu == x:
			break
		b=input("choose : ")
		c=input("choose : ")
		print("cpu : "+c)
		if b!=a[1] and b!=a[0] and b!=a[2]:
			print("select among scissors stone and paper only")
		elif b=="stone" and c=="scissors" :
			score=score+1
			print("plus 1 to "+n)
			print(n+" score "+str(score))
			print(k+" score "+str(cpu))
		elif b=="paper" and c=="stone" :
			score=score+1
			print("plus 1 to "+n)
			print(n+" score "+str(score))
			print(k+" score "+str(cpu))
		elif b=="scissors" and c=="paper" :
			score=score+1
			print("plus 1 to "+n)
			print(n+"score "+str(score))
			print(k+" score "+str(cpu))
		elif c=="paper" and b=="stone" :
			cpu=cpu+1
			print("plus 1 to "+k)
			print(n+" score "+str(score))
			print(k+" score "+str(cpu))
		elif c=="scissors" and b=="paper" :
			cpu=cpu+1
			print("plus 1 to "+k)
			print(n+" score "+str(score))
			print(k+" score "+str(cpu))
		elif c=="stone" and b=="scissors" :
			cpu=cpu+1
			print("plus 1 to "+k)
			print(n+" score "+str(score))
			print(k+" score "+str(cpu))
	print(n+" total score "+str(score))
	print(k+" total score "+str(cpu))
	if cpu>score :
		print("winner winner chicken dinner congrats "+k)
	else :
		print("winner winner chicken dinner congrats "+n)


