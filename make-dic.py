a = open('1.txt','w+')
b = open('2.txt','w+')
c = open('3.txt','w+')
d = open('4.txt','w+')
e = open('5.txt','w+')
f = open('6.txt','w+')
g = open('7.txt','w+')
h = open('8.txt','w+')
i = open('9.txt','w+')
j = open('10.txt','w+')

with open("Words.txt","r") as m:
    array = []
    for line in m:
        array.append(line)

for ab in array:
    print(ab)
    print(len(ab))
    print('*********************************')
    j=len(ab)-1
    if (j == 1):
        a.write(ab)
        print('Written to' + str(j))
    elif (j == 2):
        b.write(ab)
        print('Written to' + str(j))
    elif (j == 3):
        c.write(ab)
        print('Written to' + str(j))
    elif (j == 4):
        d.write(ab)
        print('Written to' + str(j))
    elif (j == 5):
        e.write(ab)
        print('Written to' + str(j))
    elif (j == 6):
        f.write(ab)
        print('Written to' + str(j))
    elif (j == 7):
        g.write(ab)
        print('Written to' + str(j))
    elif (j == 8):
        h.write(ab)
        print('Written to' + str(j))
    elif (j == 9):
        i.write(ab)
        print('Written to' + str(j))
    else :
        j.write(ab)
        print('Written to' + str(j))

