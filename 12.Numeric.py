from decimal import *

d = 8 * 2

print('x is {}'.format(d))
print(type(d))

f = 7*3.1443
print(type(f))
print('f is {}'.format(f))
x = 4/3
print('x is {}'.format(x))
print(type(x))
r= 8//4
print('r is {}'.format(r))
s = 9%3
print('s is {}'.format(s))

sxo = .1+.1+.1-.3
print('sxo is {}'.format(sxo))

ax = Decimal('.10')
bx =  Decimal('.30')
sumo = ax+ax+ax-bx
print('sumo ',sumo)