def cript(name, key1, key2):
    newname = ''
    for i in range(0, len(name)):
        a = name[i]

        alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for c in range(0, 36):
            if a == alfa[c]:
                a = 5 + c
                a = (a ** key1 + key2 ** 2) / 230
                b = (a * 3) - 1 / 4
                a = int(a)
                b = int(b)
                b = str(b)
                a = str(a)
                a = a + alfa[c - 3] + b + alfa[c - 15]

        newname = newname + a
    return newname


def menu():
    print('Ferramenta de criptografia')
    print('Created by: zzAlfa')
    print('')
    nome = str(input('Digite aqui o que deseja criptografar: ')).lower().strip()
    k1 = int(input('Digite um número para ser a chave [0 para padrão]: '))
    k2 = int(input('Digite um número para ser o segundo valor da chave [0 para padrão]: '))
    if k1 == 0:
        k1 = 2
    if k2 == 0:
        k2 = 6
    print(f' Criptografado fica: {cript(nome, k1, k2)} \nAs chaves são {k1}-{k2}')
    keep = str(input('Deseja criptografar mais alguma coisa? [S/N]')).upper().strip()
    if keep == 'S':
        menu()
    else:
        print('Programa encerrado')


menu()
