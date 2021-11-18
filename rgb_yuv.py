Wr = 0.299
Wg = 0.587
Wb = 0.114
Um = 0.436
Vm = 0.615
print ("R:")
R= int(input())

print ("G:")
G= int(input())

print ("B:")
B= int(input())


Y = Wr*R + Wg*G + Wb*B
U = Um*(B-Y)/(1-Wb)
V = Vm*(R-Y)/(1-Wr)
print ("Y:", Y)
print ("U:", U)
print ("V:", V)

R = Y + 1.140*V
G = Y - 0.395*U - 0.581*V
B = Y + 2.032*U

print ("R:", R)
print ("G:", G)
print ("B:", B)
