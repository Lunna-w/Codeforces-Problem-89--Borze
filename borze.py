zero = "."
one = "-."
two = "--"

result = []

n = input()

i = 0
while i < len(n):
    if n[i:].startswith(two):
        result.append(2)
        i += 2
    elif n[i:].startswith(one):
        result.append(1)
        i += 2
    elif n[i:].startswith(zero):
        result.append(0)
        i += 1
    else:
        i += 1

print(''.join(map(str, result)))
