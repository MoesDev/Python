def swap(the_list):
	x=0
	for the_list in range(0, len(the_list)-1):
		num1 = the_list.val[x]
		num2 = the_list.val[x+1] 
		if num1 > num2:
			(num1,num2) = (num2,num1)
			the_list[x]=num1
			the_list[x+1]=num2
		x+=1
	return the_list

g = [1,5,3,4,8,7]

print swap(g)
