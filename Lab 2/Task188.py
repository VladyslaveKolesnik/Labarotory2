a = int(input())
b = int(input())
c = int(input())
d = int(input())

cost = a

if d > b:
    cost = cost + (d - b) * c

print(cost)