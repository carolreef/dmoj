n = int(input())
for _ in range(n):
    code = input()
    cap = ''
    num = ''
    calc = 0
    pos = True
    for i in range(len(code)):
        if code[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            cap += code[i]
        if code [i] == '-':
            pos = False
        if code[i] in '1234567890':
            num += code[i]
            if ((i+1 < len(code) and code[i+1] not in '1234567890') or i == len(code)-1):
                if pos == True:
                    calc += int(num)
                else:
                    calc -= int(num)
                num = ''
                pos = True
    cap += str(calc)
    print(cap)