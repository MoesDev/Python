def first_function(name):
	print name
	print 'outside of function'
	first_function('cody')

arr = [1,2,3]

def first_function(arr):
	for i in range(0, len (arr)):
		print arr[i]
	#for (var i =0, i < arr.length; i++):

arr = [1,2,3,4,5,6,7,8,9,10]

def first_function(arr):
	for i in range(0, len (arr)):
		if arr[i]%2 ==0:
			print arr[i]
	#for (var i =0, i < arr.length; i++):
	