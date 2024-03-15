# Enter your code here. Read input from STDIN. Print output to STDOUT
instructions = int(input())
ops = []
for _ in range(instructions):
    ops.append(list(input().split()))

s = ""
undo = []
for op in ops:
    if op[0] == '1':
        undo.append(s)
        s += op[1]
    elif op[0] == '2':
        undo.append(s)
        s = s[0: -int(op[1])]
    elif op[0] == '3':
        print(s[int(op[1]) - 1])
    elif op[0] == '4':
        s = undo.pop(-1)