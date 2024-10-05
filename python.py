print ('==== Mini Calculadora ====\n')

#1 alteração

a = int(input('Informe um número: '))
b = int(input('Informe outro número: '))
resp = 0

#2 alteração
while resp == 0:
    operacao = input ('Informe a operação (+,-,*,/): ')
    if operacao == '+':
        print(a+b)
    elif operacao == '-':
        print(a-b)
    elif operacao == '*':
        print (a*b)
    elif operacao == '/':
        print (a/b)
    else:
        print('Não foi possível identificar a operação!')
    resp = int(input ('\nDesejas continuar? (sim = 0, não = 1): '))
