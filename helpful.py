f = open('27-A.txt').readlines()
pars = list(map(lambda x: [int(i) for i in x.strip().split()], f[1:]))
pars_1 = []
papalow = [0, 0]

for i in pars:
    if i[0] % 5 != i[1] % 5:
        pars_1.append(i)


def savart(pars, papalow):
    suma = 0
    for i in pars:
        if i != papalow:
            suma += min(i)
    if suma + papalow[0] % 5 != 0:
        return suma + papalow[0] % 5
    elif suma + papalow[1] % 5 != 0:
        return suma + papalow[1] % 5
    else:
        return 10 ** 200


all_rez = []
for i in pars_1:
    all_rez.append(savart(pars, i))

print(min(all_rez))

