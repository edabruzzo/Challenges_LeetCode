
def calcElementsArrayPlus1(arr):
    valores_unicos = set(arr)
    lista = []
    for valor in valores_unicos:
        if valor + 1 in arr:
            item_anotado = arr.count(valor)
            lista.append(item_anotado)
    return sum(lista)



'''

https://pythonprinciples.com/challenges/Thousands-separator/

Thousands separator
Write a function named format_number that takes a non-negative number as its only parameter.
Your function should convert the number to a string and add commas as a thousands separator.
For example, calling format_number(1000000) should return "1,000,000".

'''
def format_number(x):
   numero_formatado_string = None
   if x > 0:
       while x > 1000:
           x, resto = divmod(x,1000)
           numero_formatado_string = ',%03d%s' % (x, resto)
   return numero_formatado_string






def calPoints(ops) -> int:

    result = None

    lista = []
    if len(ops) >=1 and len(ops)<=1000:
        for valor in ops:
            try:
                valor = int(valor)
            except:
                pass
            if isinstance(valor,int) and int(valor) > -3*104 and int(valor)<3*104:
                lista.append(valor)
            else:
                if valor == 'C':
                    if(len(lista)>0):
                        lista.pop()
                if valor == 'D':
                    if(len(lista)>0):
                        lista.append(lista[-1]*2)

                if valor == '+':
                    if (len(lista) > 1):
                        elemento_anterior = lista[-1]
                        elemento_anterior_anterior = lista[-2]
                        resultado = elemento_anterior + elemento_anterior_anterior
                        lista.append(resultado)

        result = sum(lista)

        return result

def test(line):
    ops = line.strip().split()
    print(calPoints(ops))

def teste2(line):
    ops = line.strip().split()
    lista = [int(valor) for valor in ops]
    print(calcElementsArrayPlus1(lista))

if __name__ == '__main__':
    #line = input()
    line1 = "5 2 C D +"
    line2 = "5 -2 4 C D 9 + +"
    #test(line1)
    #test(line2)
    #test("1")


    linha4 = "1 1 3 3 5 5 7 7"
    linha5 = "1 3 2 3 5 0"
    linha6 = "1 1 2 2"
    linha7 = "1 1 2"
    linha8 = "1 1 2 3"

    teste2(linha8)
    teste2(linha7)
    teste2(linha6)