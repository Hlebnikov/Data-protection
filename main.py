import cripto
import coder
import random
from sympy import prevprime 

p = 179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865485276302219601246094119453082952085005768838150682342462881473913110540827237163350510684586298239947245938479716304835356329624224137111

# print(prevprime(2**1024))

a=99999999; x=10**60; p=prevprime(2**1024)
print(("-"*15 + " pow %s^%s [mod %s]") % (a,x,p))

y = cripto.quickPowerByModule(a,x,p)
print(y)

print("-"*15 + " euklid ")
 
a,b = 99999999, 99999997
print(cripto.euklid(a,b))

print("-"*15 + " Common key generation")

xB = 45385765643534345
xA = 24353243242342342
cripto.commonKey(xA,xB)

print("-"*15 + " Baby-step giant-step")

a,x,p = 5,123,2903

y = cripto.quickPowerByModule(a,x,p)
decryptX = cripto.decrypt(y,a,p)
print("x = %s" % decryptX)
print("And it's " + ("right" if y==cripto.quickPowerByModule(a,decryptX,p) else "false"))

print("-"*15 + " Shamir")
ann = coder.ShamirAbonent()
bob = coder.ShamirAbonent()

m = 100
print("Ann has sended %s " % m)
x1 = ann.code(m)
x2 = bob.code(x1)
x3 = ann.decode(x2)
m = bob.decode(x3)
print("Bob has received %s" % m)

print("-"*15 + "RSA protocol")

m = 234
print("Ann has sended %s " % m)
ann = coder.RSAabonent()
bob = coder.RSAabonent()

e = ann.encrypt(m, bob.publicKey())
print("Bob has received %s" % bob.decrypt(e))

print("-"*10 + "ElGamal protocol")

ann = coder.ElGamal()
bob = coder.ElGamal()

m=15
print("Ann has sended %s " % m)
r,e = ann.code(m, bob.publicKey())
print("r = %s, e= %s" % (r,e))
m = bob.decode(r,e)
print("Bob has received %s " % m)

print("-"*10 + "Vername code")

message = "Hello, World!"
print("message: " + message)
codedMessage = ""
decodedMessage = ""
for ch in message:
	k = int(random.random() * 50) + 50
	coded = chr(coder.codeVarnam(ord(ch),k))
	codedMessage += coded
	decodedMessage += chr(coder.codeVarnam(ord(coded),k))
print("coded: " + codedMessage)
print("encoded: " + decodedMessage)

