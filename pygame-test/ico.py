import math;

R = 100


tau = (math.sqrt(5) + 1)/2
s = math.sin(math.pi / 5)
r = tau - 0.5

print(0, 0, round(r*R, 2))

for i in range(5):
    alpha = - math.pi / 5.0 + i * math.pi / 2.5
    print(round(R*math.cos(alpha),2), round(R*math.sin(alpha),2), R/2)

for i in range(5):
    alpha =  i * math.pi / 2.5
    print(round(R*math.cos(alpha),2), round(R*math.sin(alpha),2), -R/2)

print(0, 0, - round(r*R,2))

