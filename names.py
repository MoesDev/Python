#Monet Harkin

#Part 1 - Names
students = [
	{'first_name': 'Michael', 'last_name': 'Jordan'},
	{'first_name': 'John', 'last_name': 'Rosales'},
	{'first_name': 'Mark', 'last_name': 'Guillen'},
	{'first_name': 'KB', 'last_name': 'Tonel'}
]

print "Part 1"
print "-----------------"

for x in students:
	print x['first_name']+" "+x['last_name']

print "------------------"
print "Part 2"
print "------------------"


#Part 2 - Names

def number(x):
	x+=1
	return x

users ={
	'Students': [
		{'first_name': 'Michael', 'last_name': 'Jordan'},
		{'first_name': 'John', 'last_name': 'Rosales'},
		{'first_name': 'Mark', 'last_name': 'Guillen'},
		{'first_name': 'KB', 'last_name': 'Tonel'}
	],
	'Instructors': [
		{'first_name': 'Michael', 'last_name': 'Choi'},
		{'first_name': 'Martin', 'last_name': 'Puryear'}
	]
}

for key, data in users.items():
	print key
	count=0
	for index in data:
		count = number(count)
		name_length = len(index['first_name']) + len(index['last_name'])
		print str(count) + " - " + index['first_name'] + " "+ index['last_name'] + " - " + str(name_length)
	