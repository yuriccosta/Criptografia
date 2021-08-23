alfa = 'abcdefghijklmnopqrstuvwxyz0123456789 '


def glis(name, key1, key2):
    secl = []
    for i in range(0, len(name)):
        a = name[i]

        alfa1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for c in range(0, 36):
            if a == alfa1[c]:
                a = 5 + c
                a = (a ** key1 + key2 ** 2) / 230
                b = (a * 3) - 1 / 4
                a = int(a)
                b = int(b)
                b = str(b)
                a = str(a)
                a = a + alfa1[c - 3] + b + alfa1[c - 15]

        secl.append(a)
    return secl


def descrip(name, k1, k2):
    mainl = glis(alfa, k1, k2)
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
    if k1 == 0:
        k1 = 2
    if k2 == 0:
        k2 = 6
    print(f'Descriptografado fica: {descrip(nome, k1, k2)}')
    keep = str(input('Deseja descriptografar mais alguma coisa? [S/N]')).upper().strip()
    if keep == 'S':
        menu()
    else:
        print('Programa encerrado')


menu()
