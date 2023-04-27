#Atividade de ponto extra para P1 de Matemática Discreta 2.
#Integrantes: 
    #Artur Rodrigues Sousa Alves - 211043638
    #Guilherme Soares Rocha - 211039789
    #João Manoel Barreto Neto - 211039519

#Código: 

#Função para melhorar a organização e coerência da saída do código
def organiza():
    print('---------------------------------------------------------')

#Função para o MDC
def MDC(a,b):

    if(b!=0): #Onde o MDC depende tanto de A quanto de B

        #Passos para definir o MDC dos números de entrada
        resto = (a%b)
        d,z,w = MDC(b,resto)
        x = w #Atribuindo o valor de x que será retornado para a função principal
        y = z-w * (a//b) #Atribuindo o valor de y que será retornado para a função principal

    elif(b==0): #Onde o MDC depende exclusivamente de A
        d,x,y = a,1,0 #Atribuindo os valores que serão retornados para a função principal

    #Retorna os valores do divisor, do primeiro x e primeiro y, repectivamente
    return(d,x,y) 

#Função MAIN
organiza()
print('Vamos resolver uma equação no formato "ax + by = c". Para isso: ')

a = int(input("Digite o valor de A: "))
organiza()
b = int(input("Digite o valor de B: "))
organiza()
#Loop para não permitir que o usuário imprima um valor inválido para a equação
while(a==0 and b==0):
    print('ATENÇÃO!')
    print('Para que haja solução para equação, A e B não podem ser simultaneamente nulos! Insira os daods novamente: ')
    a = int(input("Digite o valor de A: "))
    organiza()
    b = int(input("Digite o valor de B: "))
    organiza()

c = int(input("Digite o valor de C: "))
organiza()
print(f'A equação inserida foi: {a}x + {b}y = {c}')
organiza()

#Atribuindo valores da função MDC que serão utilizados na MAIN
mdc, x0, y0 = MDC(a,b) 

if((c % mdc) != 0): 

    print(f'O MDC de {a} e {b} não divide {c}! Portanto não há soluções inteiras para a equação informada!')

else:
    #Criando uma razão para ser possível imprimir as N soluções desejadas pelo usuário a partir de soluções particulares
    z = c // mdc 
    x0 = x0 * z #Sol. particular de 'x'
    y0 = y0 * z #Sol. particular de 'y'
    print(f'A solução geral para a equação: {a}x + {b}y = {c} é:')
    print(f'x = {x0} + {b}t;')
    print(f'y = {y0} - {a}t;')
    organiza()
    N = int(input('Agora, digite o número de soluções desejadas: '))
    organiza()
    for i in range(N):
        #Cálculo das N soluções
        x = x0 + (b // mdc) * i 
        y = y0 - (a // mdc) * i 
        print(f'solução {i+1} => x = {x}; y = {y}')
        organiza()