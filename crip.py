import random


alfa = ['n', 'w', 'r', 'x', '7', 'o', '2', 'z', '6', 'v', 'f',
        '8', 'k', 'a', 'm', 'q', '1', 'c', 'y', '4', 'd', 'j',
        'b', 'u', '9', 's', '0', 'p', 'g', '3', 't', '5', 'i', 'e', 'l', 'h']


def cript(name, key1, key2, rkey1, rkey2):
    newname = ''
    for i in range(0, len(name)):
        a = name[i]
        for c in range(0, 36):
            if a == alfa[c]:
                a = 5 + c
                a = (a ** key1 + key2 ** 2) * rkey1 / rkey2
                b = (a * rkey2) - 1 / (a / 2)
                a = int(a)
                b = int(b)
                b = str(b)
                a = str(a)
                a = a + alfa[c - rkey2] + b + alfa[c - rkey1]
        newname = newname + a
    return newname


def menu():
    print('Ferramenta de criptografia')
    print('Created by: zzAlfa')
    print('')
    nome = str(input('Digite aqui o que deseja criptografar: ')).lower().strip()
    k1 = int(input('Digite um número para ser o primeiro chave [0 para padrão]: '))
    k2 = int(input('Digite um número para ser o segundo valor da chave [0 para padrão]: '))
    if k1 == 0:
        k1 = 2
    if k2 == 0:
        k2 = 6
    esc = str(input('Deseja que as duas últimas chaves sejam aleatórias? [S/N] ')).lower()
    while True:
        if esc == 's':
            ran1 = random.randint(1, len(alfa))
            ran2 = random.randint(1, len(alfa))
            break
        elif esc == 'n':
            ran1 = int(input('Digite um número para ser o terceiro valor da chave [0 para padrão]: '))
            ran2 = int(input('Digite um número para ser o quarto valor da chave [0 para padrão]: '))
            if ran1 == 0:
                ran1 = 1
            if ran2 == 0:
                ran2 = 2
            break
        else:
            print('Digite novamente, tente digitar apenas s ou n')
            esc = str(input('Deseja que as duas últimas chaves sejam aleatórias? [S/N] ')).lower()
    print(f' Criptografado fica: {cript(nome, k1, k2, ran1, ran2)} \nAs chaves são {k1}-{k2}-{ran1}-{ran2}')
    print('---!!!Lembre-se de salvar essas chaves em algum lugar!!!---')
    keep = str(input('Deseja criptografar mais alguma coisa? [S/N]')).upper().strip()
    if keep == 'S':
        menu()
    else:
        print('Programa encerrado')


menu()
