#Solution to problem 3

import string
def constraintpair(first,second,m):
	final=[]
	for i in first:
		for j in second:
			if i + m + 1 == j:
				final.append(i)
	return final
			
def substringmatchexact(target,key):
	match,final,index=0,[],0
	while target:
		match=string.find(target,key,index)
		if match==-1:return final
		else:
			index=match+len(key)
			final.append(match)

def keygenerator(target,key):
	i,final=0,[]
	while i < len(key):
		if i==0:key1=' '+key[:i]
		else:key1=key[:i]
		if i==len(key)-1:key2=key[i+1:]+' '
		else:key2=key[i+1:]
		tuple1=substringmatchexact(target,key1);
		tuple2=substringmatchexact(target,key2)
		final.extend(constraintpair(tuple1,tuple2,len(key1)))
		i+=1
	returns=sorted(list(set(final)))
	return returns

