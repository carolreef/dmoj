d = int(input())
e = int(input())
plus = True
for _ in range(e*2):
    s = input()
    if s == '-':
        plus = False
    if s == '+':
        plus = True
    if s.isdigit():
        if plus == True:
            d += int(s)
        else:
            d -= int(s)
print(d)
    