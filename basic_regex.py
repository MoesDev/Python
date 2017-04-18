import re

#def get_matching_words(regex):
words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

 #return [word for word in words if re.search(regex, word)]

print "1. Words with v :"
for word in words:
	if re.search(r'v', word):
		print word
print "---------------"

print "2. Words containing double -s :"
for word in words:
	if re.search(r'ss', word):
		print word
print "---------------"

print "3. Words ending in e:"
for word in words:
	if re.search(r'e$', word):
		print word
print "---------------"

print "4. Words with b any character then another b:"
for word in words:
	if re.search(r'b.b', word):
		print word
print "---------------"

print "5. Words with b at least one character then b:"
for word in words:
	if re.search(r'b.+b', word):
		print word
print "---------------"

print "6. Words with b and then another b somewhere after, including right after :"
for word in words:
	if re.search(r'b.*b', word):
		print word
print "---------------"

print "7. Words that include all 5 vowels in order:"
for word in words:
	if re.search(r'a.*e.*i.*o.*u', word):
		print word
print "---------------"

# print "8. words that contain letters from 'regular expression' one or more times :"
# for word in words:
# 	if re.search(r'(?regular)', word):
# 		print word
# print "---------------"

print "9. double letters:"
for word in words:
	if re.search(r'[\w]{2}[\w+]', word):
		print word
print "---------------"