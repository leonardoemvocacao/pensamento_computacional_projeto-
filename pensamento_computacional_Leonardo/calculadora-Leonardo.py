print('\n Calculadora simples - Python Vocação\n')

numb_hum = input('Digite o primeiro número:')
numb_dois = input('Digite o segundo número:')

operar_numb = input('Escolha a operação: 1 ->, 2 -> -,, 3 -> *, 4 -> /')

if operar_numb  == '4':
    result = int(numb_hum) / int(numb_dois)
    print(f'o resultado é: {result}')

elif operar_numb == '3':
     result = int(numb_hum) * int(numb_dois)
     print(f'O resultado é: {result}')

elif operar_numb == '4':
     
    if int (numb_dois) != 0:
        result = int(numb_hum) / int(numb_dois)
        print(f'O resultado da divisão é {result}')
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
     print("Número não é válido, tente novamente!")



     frutas = ['maçã','banana','laranja','abacaxi']

     frutas.append('amora')
     frutas.append('mirtilo')
     frutas.append('melancia')


     print(frutas[5])