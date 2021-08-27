alfa = 'nwrx7o2z6vf8kamq1cy4djbu9s0pg3t5ielh '


def glis(name, key1, key2, rkey1, rkey2):
    secl = []
    for i in range(0, len(name)):
        a = name[i]

        alfa1 = ['n', 'w', 'r', 'x', '7', 'o', '2', 'z', '6', 'v', 'f',
                 '8', 'k', 'a', 'm', 'q', '1', 'c', 'y', '4', 'd', 'j',
                 'b', 'u', '9', 's', '0', 'p', 'g', '3', 't', '5', 'i', 'e', 'l', 'h']
        for c in range(0, 36):
            if a == alfa1[c]:
                a = 5 + c
                a = (a ** key1 + key2 ** 2) * rkey1 / rkey2
                b = (a * rkey2) - 1 / (a / 2)
                a = int(a)
                b = int(b)
                b = str(b)
                a = str(a)
                a = a + alfa1[c - rkey2] + b + alfa1[c - rkey1]

        secl.append(a)
    return secl


def descrip(name, k1, k2, rkey1, rkey2):
    mainl = glis(alfa, k1, k2, rkey1, rkey2)
    maind = (gdic(mainl))

    for c in range(0, len(mainl)):
        name = name.replace(mainl[c], maind[mainl[c]])
    return name


def gdic(a):
    secd = {}
    for c in range(0, len(a)):
        secd[a[c]] = alfa[c]
    return secd


def menu():
    print('Ferramenta de descriptografia')
    print('Created by: zzAlfa')
    print('')
    nome = str(input('Digite aqui o que deseja descriptografar: ')).lower().strip()
    k1 = int(input('Digite o valor da primeira chave [0 para padrão]: '))
    k2 = int(input('Digite o valor da segunda chave [0 para padrão]: '))
    ran1 = int(input('Digite o valor da terceira chave: '))
    ran2 = int(input('Digite o valor da quarta chave: '))
    if k1 == 0:
        k1 = 2
    if k2 == 0:
        k2 = 6
    print(f'Descriptografado fica: {descrip(nome, k1, k2, ran1, ran2)}')
    keep = str(input('Deseja descriptografar mais alguma coisa? [S/N]')).upper().strip()
    if keep == 'S':
        menu()
    else:
        print('Programa encerrado')


menu()
