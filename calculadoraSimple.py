import os

def somaSub(operador, num1, num2):
    if operador in '+':
        return float(num1) + float(num2)
    else:
        return float(num1) - float(num2)


def multDiv(operador, num1, num2):
    if operador in '*':
        return float(num1) * float(num2)
    else:
        return float(num1) / float(num2)


operadores = []
numeros = []
#tmp = ''


def calculadora(operador='*/'):
    global operadores
    global numeros
    bol = False
    if operador in '*/':
        bol = True
    i=0
    result = 0
    while i < len(operadores):
        if operadores[i] in operador:
            try:
                if bol:
                    print(numeros, operadores)
                    result = numeros[i+1] = multDiv(operadores[i],numeros[i],numeros[i+1])
                else:
                    result = numeros[i+1] = somaSub(operadores[i],numeros[i],numeros[i+1])
            except (ValueError, IndexError):
                #os.system("clear")
                print('Operação invalida!\nPor favor informe uma operação valida\n')
                break            
            numeros.remove(numeros[i])
            operadores.remove(operadores[i])
            print(numeros,operadores)
            i-=1
        i+=1
    
    if operadores:
        return calculadora(operador='+-')

    return result

operation='5*5+(5*(5+5))'

def precedence():
    global operation
    opening = -1
    closing = -1
    par = False
    nexting = False
    for i, value in enumerate(operation):
        if not value.isdigit():
            if value in '()' :
                if value in '(':
                    if i != -1:
                        nexting = True
                    opening = i
                else:
                    closing = i
                    if opening != -1 and closing > opening:
                        par = True
                if par:
                    break
    #os.system("clear")
    if par:
        validation = True
        global operadores
        global numeros
        #global tmp
        tmp = operation[opening+1: closing]
        print(operation, numeros, operadores,tmp)
        for i in tmp:
            if not i.isdigit():
                if i in '+-*/':
                    operadores.append(i) # adiciono um operador na lista
                    tmp = tmp.replace(i,' ')
                elif i in ',.':
                    tmp = tmp.replace(i,'.')
                else:
                    os.system("clear")
                    print('Operação invalida!\nSomente os operados +/*- são permitidos\n')
                    validation = False
                    break
                
        if validation:
            result = 0
            numeros = tmp.split(' ') # crio uma  lista contendo somente os numeros 
            print(numeros,operadores)
            result = calculadora()
            operation = operation.replace(operation[opening:closing+1],str(result))
            print('Resultado: ',operation)
            numeros = []
            operadores = []
            if nexting:
                precedence()
            




def main():
    global operation
    operation = input('Digite a operação:\n')
    if operation.find('('):
        precedence() # chamo a funcao de verificação e tratamento de expresoes com parentes ( )
    
    global operadores
    global numeros
    validation = True

    for i in operation:
        if not i.isdigit():
            if not i in ',.' and i in '+-*/':
                operadores.append(i) # adiciono um operador na lista
                operation = operation.replace(i,' ')
            elif i in ',.':
                operation = operation.replace(i,'.')
            else:
                os.system("clear")
                print('Operação invalida!\nSomente os operados +/*- são permitidos\n')
                validation = False
                break
                
    if validation:
        os.system("clear")
        numeros = operation.split(' ') # crio uma  lista contendo somente os numeros 
        print(numeros,operadores)
        result = calculadora('*/')
        if operadores: # se a lista nao esitiver vazia
            result = calculadora('+-')
        print(result)
    else:
        os.system("python calculadoraSimple.py")


os.system('clear')
main()
