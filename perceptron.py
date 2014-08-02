

def perceptron(inputs, weights, bias):
  if (weights[0]*inputs[0]+weights[1]*inputs[1])+bias <= 0:
    return 0
  else:
    return 1

# this is the NAND
for inp in [[0,0],[0,1],[1,0],[1,1]]:
  print 'Input is', inp
  print perceptron(inp,[-2,-2],3)

def nand(inp):
  return perceptron(inp,[-2,-2],3)

# multilayer computation to compute sum with carry:

for x1,x2 in [[0,0],[0,1],[1,0],[1,1]]:
  print 'Input is', [x1,x2]
  x3 = nand([x1,x2])
  #print 'x3', x3
  x4 = nand([x1,x3])
  #print 'x4', x4
  x5 = nand([x3,x2])
  #print 'x5', x5
  x6 = nand([x4,x5])
  print 'sum', x6
  x7 = nand([x3,x3])
  print 'carry', x7

# let's have a look at the sigmoid function

from pylab import *
x = arange(-5,5,0.01)
y = 1/(1+exp(-x))
plot(x,y)
show()


