#Codigo otimizado
print('='*20)
print("calculadora")
print('='*20)

print('[ MENU ]'.center(20, '='))
print('[1] = SOMA')
print('[2] = SUBTRAÇÃO')
print('[3] = DIVISÃO')
print('[4] = MULTIPLICAÇÃO')
print('[5] = EXPODENCIAÇÃO')
print('[0] = SAIR')
try:
    Op = int(input('Digite sua opção: '))
    if (Op >= 0 and Op <=5):

        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite o segundo número: '))

        match(Op):
            case 1:
                print(f'A soma entre {n1} + {n2} = [{n1 + n2}]')
            case 2:
                print(f'A subtração entre {n1} - {n2} = [{n1 - n2}]')
            case 3:
                print(f'A multiplicação entre {n1} x {n2} = [{n1 * n2}]')
            case 4:  
                if n2 != 0:
                    print(f'A divisão entre {n1} / {n2} = [{n1 / n2:.2f}]')
                else:
                    print('ERRO : Divisão por zero!')
            case 5: 
                print(f'A exponenciação de {n1} ** {n2} = [{n1**n2}]')
            case 0: 
                print("Você saiu do programa")
    else:
        print('Opção invalida!')
except ValueError: 
    print('ERRO ! Digite um número')