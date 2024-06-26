import numpy as np

# 논리 회로 구현 AND, NAND, OR
def AND(x1, x2):
    w1, w2, theta=0.3, 0.3, 0.4
    y=x1*w1+x2*w2
    if y<=theta:
        return 0
    elif y>theta:
        return 1
    
def NAND(x1, x2):
    w1, w2, theta=-0.3, -0.3, -0.4
    y=x1*w1 + x2*w2
    if y<=theta:
        return 0
    elif y>theta:
        return 1

def OR(x1, x2):
    w1, w2, theta=0.2, 0.2, 0.1
    y=x1*w1 + x2*w2
    if y<=theta:
        return 0
    elif y>theta:
        return 1
    
print(AND(0,0))
print(AND(1,0))
print(AND(0,1))
print(AND(1,1))
    
# 가중치와 편향 도입
def AND2(x1, x2):
    x=np.array([x1, x2])
    w=np.array([0.3, 0.3])
    b=-0.4
    y=np.sum(w*x) + b
    if y<=0:
        return 0
    else:
        return 1
    
def NAND2(x1, x2):
    x=np.array([x1, x2])
    w=np.array([-0.3, -0.3])
    b=0.4
    y=np.sum(w*x)+b
    if y<=0:
        return 0
    else:
        return 1
    
def OR2(x1, x2):
    x=np.array([x1, x2])
    w=np.array([0.2, 0.2])
    b=-0.1
    y=np.sum(x*w)+b
    if y<=0:
        return 0
    else:
        return 1
    
print(AND2(0,0))
print(AND2(1,0))
print(AND2(0,1))
print(AND2(1,1))


# XOR 구현
def XOR(x1, x2):
    s1=NAND2(x1, x2)
    s2=OR2(x1, x2)
    y=AND2(s1, s2)
    return y
    
print(XOR(0,0))
print(XOR(1,0))
print(XOR(0,1))
print(XOR(1,1))
    