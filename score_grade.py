def grade(x,y):
	x=input("What is the score: ")
	if x>=60 and x<70:
		y="D"
	elif x>=70 and x<80:
		y="C"
	elif x>=60 and x<90:
		y="B"
	elif x>=90 and x<=100:
		y="A"
	else:
		y="not a valid grade entry"
	print "Score "+str(x)+"; Your grade is "+y

for count in range(0,10):
	score=0
	output=""
	grade(score,output)
print "End of program, Bye!"


