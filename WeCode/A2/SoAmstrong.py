n = input()
print(sum([int(d) ** len(n) for d in n]) == int(n))
