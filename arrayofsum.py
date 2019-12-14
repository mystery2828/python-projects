import time
start=time.time()
x=[1,2,3,4,5,6,7,2,3,4,5,6]
key=7
x.sort()
lo=0
hi=len(x)-1
y=[]
def keys(x,lo,hi,y):
	while(lo<hi):
		if(x[lo]+x[hi])>key:
			return keys(x,lo,hi-1,y)
		elif(x[lo]+x[hi])<key:
			return keys(x,lo+1,hi,y)
		else:
			y.extend([[x[lo],x[hi]]])
			return keys(x,lo+1,hi-1,y)
	return y
print(keys(x,lo,hi,y))
print(time.time()-start)
