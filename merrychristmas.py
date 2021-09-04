import numpy
import random
from numpy.random import choice
h = 15
c, e = list('🔴🎀🌕') + ['🍀']*6, ['🌨️'] + ['✨'] + ['  ']*20

s = lambda l, n: ''.join(choice(l, n))
line = lambda i: s(e, h-i)+'  '+s(c,2*i-1)+'  '+s(e, h-i)

print('  '*h+'🌟', *(line(i) for i in range(2, h+1)), sep='\n\n')
