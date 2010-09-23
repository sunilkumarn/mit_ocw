# Solution to problem 2

import string			
def substringmatchexact(target,key):
	match,final,index=0,[],0
	while target:
		match=string.find(target,key,index)
		if match==-1:return final
		else:
			index=match+len(key)
			final.append(match)

