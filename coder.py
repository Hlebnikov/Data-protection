import cripto
import random

class ShamirAbonent():
	"""docstring for ShamirAbonent"""
	def __init__(self, p=257):
		self.p = p
		self.c = cripto.getCoprime(p-1)
		print(self.c)
		self.d = cripto.euklid(p-1,self.c)[2]
		while self.d <= 0: self.d+=self.p-1

	def code(self, message):
		return cripto.quickPowerByModule(message, self.c, self.p)

	def decode(self, message):
		return cripto.quickPowerByModule(message, self.d, self.p)

class RSAabonent:
	def __init__(self, p = 181, q = 433):
		self.p = p
		self.q = q
		self.n = p*q
		self.fi = (p-1)*(q-1)
		self.d = cripto.getCoprime(self.fi)
 		self.c = cripto.euklid(self.fi,self.d)[2]
		while self.c<=0: self.c+=self.fi

	def publicKey(self):
		return self.d

	def encrypt(self, message, key):
		return cripto.quickPowerByModule(message,key,self.n)

	def decrypt(self, message):
		return cripto.quickPowerByModule(message,self.c,self.n)

class ElGamal():
	"""docstring for ElGamal"""
	def __init__(self, p=30803, g=2):
		self.p = p
		self.g = g
		if g**(p//2) % p == 1:
			print("Warning! Pair P and Q are not safe!")

		self.x = int(random.random() * self.p-1) + 1

	def publicKey(self):
		return cripto.quickPowerByModule(self.g, self.x, self.p)

	def code(self, m, key):
		k = int(random.random() * self.p-2 + 1)
		r = cripto.quickPowerByModule(self.g, k, self.p)
		e = m*(key**k) % self.p
		return (r, e)

	def decode(self, r, e):
		return e * r**(self.p-1-self.x) % self.p

def codeVarnam(m,k):
	return m^k
		


