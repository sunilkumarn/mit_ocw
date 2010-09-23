#Recursive solution to problem 1
import string
def substringmatch(target,key):
	match=string.find(target,key)
	if match==-1:return 0
	else:
	 target=target[match+len(key):]
	 return 1+substringmatch(target,key)



