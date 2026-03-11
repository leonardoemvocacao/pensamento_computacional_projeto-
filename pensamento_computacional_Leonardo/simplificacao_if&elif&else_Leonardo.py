print = ('Qual a sua idade?')


idade = int(input())

if idade <= 18:
    print('Vocé é menor de idade')

elif idade <=65:
    print('Vocé é adulto')

else:
    print('Vocé é Idoso de idade')