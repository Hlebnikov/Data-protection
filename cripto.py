import random
import math

def quickPowerByModule(x,y,N):
	if y==0: return 1
	r = 1
	c = x
	while y:
		if (y%2):
			r = r * c % N
		y //=2
		c = c*c % N 
	return r

def euklid(a,b):
	u = [a,1,0]
	v = [b,0,1]
	t = u
	while v[0]:
		q = u[0]//v[0]
		for i in range(3):
			u[i] = u[i] - v[i]*q
		t=u
		u=v
		v=t
	return(u)

def commonKey(xA,xB):
	g = 3
	P = 2903

	print("Ann's private key - %s" % xA)
	print("Bob's private key - %s" % xB)

	yA = quickPowerByModule(g,xA,P)
	yB = quickPowerByModule(g,xB,P)

	print("Ann's public key - %s" % yA)
	print("Bob's public key - %s" % yB)

	zAB = quickPowerByModule(yA,xB,P)
	zBA = quickPowerByModule(yB,xA,P)

	print("Common key:")
	print("Ann's %s" % zAB)
	print("Bob's %s" % zBA) 

def decrypt(y,a,p):
	m = 5
	k = p//m+1
	babySteps = [int(y*(a**i)%p) for i in range(m)]
	giantSteps = [int((a**((i+1)*m))%p) for i in range(k)]
	print("baby %s" % babySteps)
	print("giant %s" % giantSteps)
	j=0
	for i in range(k):
		t = (a**((i+1)*m)) % p
		if t in babySteps:
			j = babySteps.index(t)
			break
			
	print(j,i)
	return((i+1)*m - j)

def getCoprime(a):
	while 1:
		flag = True
		t = int(random.random() * (a-1) + 1)
		for i in range(2,t+1):
			if a%i==0 and t%i==0:
				flag = False
				break
		if flag : return t