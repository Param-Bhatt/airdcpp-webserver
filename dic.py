from itertools import permutations

s='ACNNO'
s=s.lower()
F = "".join(sorted(s))  # -->i have the sorted list now
# loop through comparison list
perms = set([''.join(p) for p in permutations(F)])
for p in perms:
    p=p+"\n"
    with open('Words.txt') as f:
        if p in f.read():
            print(p)


f.close()