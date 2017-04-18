import random

def coin_toss(y):
	head_count = 0
	tail_count = 0
	for x in range(1,y+1):
		random_num = random.random()
		coin = round(random_num)
		if coin == 0:
			toss="head"
			head_count+=1
		else:
			toss="tail"
			tail_count+=1
		print "Attempt #" + str(x) +": Throwing a coin... It's a "+ toss + "Got " + str(head_count) +" head(s) so far and "+ str(tail_count)+" tail(s) so far"

coin_toss(5000)