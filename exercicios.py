"""LEARNING PYTHON"""

#PALAVRAS RESERVADAS PELO PYTHON
'''33 palavras reservadas em payton == and, as, assert, break, class, continue, for, del, elif, else, except, false, finaly
lambda, form, global, if, import, in, is, return, none, nonlocal, not, or, pass, raise, true, try, while, with, yield, def''' 

#INSTALANDO BIBLIOTECAS
"""No teminal devera ser usado o seguinte exemplo: pip install pysimplegui"""

#IMPRIMIR NA TELA

"""STRING = TEXTO DENTRO DE ASPAS SIMPLES OU ASPAS DUPLA"""

print("Hello World") 

#IMPRIMIR NA TELA COM QUEBRA DE LINHA \n

print("Hello\nWorld")

"""VARIÁVEL SIMPLES UMA CHAMADE DE A OUTRA CHAMADA DE B""" 
a = 5
b = 3
print(a + b) #somou a + B 


a = 5
b = 3
print(a, b)  #concatenou a, b

a = 1 # esse argumento esta servindo como estrutura para os comando abaixo
b = 2 # esse argumento esta servindo como estrutura para os comando abaixo

"""FUNÇÃO TYPE"""
print(type("Hello World!")) #STR
print(type(2)) #INT
print(type(2.3)) #FLOAT
print(type(True)) #BOOL
print(type(2 +3j)) #COMPLEXO ???
print(type("2")) #STR - - NESTE CASO ESTA O VALOR DELIMITADO POR ASPAS, ENTÃO PYTHON ENTENDE QUE É UMA STR

"""VARIÁVEL"""
mensagem = "OLÁ MUNDO"
print(mensagem)

numero = 5
print(numero)

numero_flutuante = 5.5550000054343 
print(numero_flutuante) 

#nomes de variaveis são separados por _ e chamados de SNAKE CASE  
# *NÃO PODEM SER USADOS NUMEROS NEM CARACTERES ESPECIAIS EM NOMES DE VARIAVEIS 

"""OPERADORES ARITMÉTICOS"""
print(1 + 1) # + ADIÇÃO
print(2 - 1) # - SUBTRAÇÃO
print(2 * 2) # * MULTIPLICAÇÃO
print(4 // 2) # // DIVISÃO INTEIRA
print(7 / 3) # / DIVISÃO 
print(7 % 3) # % RESTO DA DIVISÃO
print(2 ** 2) # ** POTENCIAÇÃO

texto = ("olá ") #Caso não haja o espaço no final da str a palavra olá ficará toda grudada
print(texto * 20) # replica a str por quantas vezes for informado

texto1 = ("olá") #metodo UPPER retorna o texto em letras maiusculas
print(texto1.upper())

texto = ("olá ") #metodo CAPITALIZE retorna a primeira letra maiuscula
print(texto.capitalize())

"""OPERADORES DE COMPARAÇÃO"""
print(a < b) # se um é menor que o outro 
print(a > b) #se um é maior que o outro 
print(a == b) #se um é igual ao outro 
print(a != b) #se um é diferente do outro
print(a <= b) #se um é menor ou igual ao outro
print(a >= b) #se um é maior ou igual ao outro

"""OPERADORES QUE REPRESENTAM VALORES BOOLEANOS"""
# a is b - - TRUE se A e B são identicos 
# a is not b - - TRUE se A e B não são idênticos
# a in b  - - TRUE se A é membro de B
# a not in b - - TRUE se a não é membro de B
x = [1, 2, 3]
y = [1, 2, 2]
print(x == y)
print(x is y)

"""ENTRADA DE USUÁRIO"""
#segue abaixo alguma formar de input mais elegante é a ultima
nome = input("digite seu nome: ")
print(nome) #quando o nome for digitado e clicar en enter o programa continuara a rodar

numero = input("digite um numero: ")
print("o numero digitado foi: " + numero) 

numero = input("digite um numero: ")
print("o numero digitado foi {} " .format(numero)) 

nome = input("digite seu nome: ")
idade = input("digite sua idade: ")
print ("seu nome é {}" "e sua idade é {}".format(nome, idade)) 
#a função format() vai substituir o {} pela variavel numero.

x = 245.6453
print("{:.2f}".format(x))
# O :.2f diz que queremos apenas 2 casas decimais para a variavel x

"""CONSTANTES"""

# True, false e none 




























if b > a:
    print("B é maior que A") #se B for maior que A vai imprimir B é maior que A
else:
    print("Bug") #se B for menor que A vai imprimir  bug

print

if 1 > 2:
    print("1 é maior que 2") #se 1 for maior que 2 vai imprimir a palavra errado, pq a primeira checagem viu que é false então pulou para segunda checagem

else:
    print("errado")








