palavra_secreta = 'projetos'
digitadas = []
chances = 5
while True:
    if chances <= 0:
        print('Você perdeu!')
        break
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Opa opa, isso não está certo! Você só pode digitar uma LETRA por vez.')
        continue

    digitadas.append(letra)

    if letra in palavra_secreta:
        print(f'Boa! A letra "{letra}" existe na palavra secreta!')
    else:
        print(f'ERROUUUUUU! A letra "{letra}" não existe na palavra secreta!')
        digitadas.pop()
    
    secreto_temporario = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'    
    if secreto_temporario == palavra_secreta:
        print('Parabéns, você acertou a palavra secreta do dia!')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')
    if letra not in palavra_secreta:
        chances -= 1
    print(f'Você ainda tem {chances} chances.')
    print()