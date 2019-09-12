from itertools import permutations

s='RIPTS'
s=s.lower()
F = "".join(sorted(s))  # -->i have the sorted list now
# loop through comparison list
perms = set([''.join(p) for p in permutations(F)])
j=0
answers = []
for p in perms:
    p=p+"\n"

    with open('Words.txt') as f:
        if p in f.read():
            answers.append(p.upper())
            print(p)
            j+=1
for ans in answers:
    print(ans)

f.close()