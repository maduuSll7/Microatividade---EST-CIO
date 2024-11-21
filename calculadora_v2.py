saida =''

def adicao(x,y):
    return (x + y)

def subtracao(m,n):
    return (m - n)

def multiplicacao(f,j):
    return (f * j)

def divisao(a,b):
    return (a / b)
if divisao == '0':
    print('Não foi possível realizar a divisão por 0.')

def calculadora(num1,num2,result):

    print("Selecione  operação desejada:")

    print("1.Adição")
    print("2.Subtração")
    print("3.Multiplicação")
    print("4.Divisão")

    while True: 
        choice = input("Selecione a operação (1/2/3/4:)")
        if choice in ('1','2','3','4'):
            try:
                num1 = float(input('Digite o primeiro número:'))
                num2 = float(input('Digite o segundo número:'))
                result = '='
            except ValueError:
                print('Número invalido, por favor digite outro numero.')
                continue
        if choice == '1':
            print(num1, '+', num2, '=', adicao(num1,num2))
        elif choice == '2':
            print(num1,'-', num2, '=', subtracao(num1,num2))
        elif choice == '3':
            print(num1, '*', num2, '=', multiplicacao(num1,num2))
        elif choice == '4':
            print(num1, '/', num2, '=', divisao(num1,num2))
            print(result)
        
        proximo_calculo = input('Deseja fazer um novo calculo ? (S/N):')
        if proximo_calculo == 'N':
            break
        else:
            print('Opção inválida.')

calculadora('num1','num2','result')