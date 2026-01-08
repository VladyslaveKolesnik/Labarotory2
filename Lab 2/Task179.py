t = int(input()) % 6

if 0 < t < 4:
    print("green")
elif t == 4:
    print("yellow")
else:
    print("red")