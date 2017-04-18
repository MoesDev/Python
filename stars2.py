def draw_stars(a):
	for x in a:
		text = ""
		if type(x) is int:
			n= "*" * x
			print n
		else:
			text = x.lower()
			n = len(text)
			letter = text[0] * n
			print letter

arr=[4,"Tom",1,"Michael",5,7,"Jimmy Smith"]
draw_stars(arr)