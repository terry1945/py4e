fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

for lin in hand:
    lin = lin.strip()
    #print(lin)
    wds = lin.split()
    print(wds)
    for w in wds:
        print(w)


