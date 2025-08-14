# region SUT interativo não adequado para testes unitários

"""Nesse aquivo temos o nosso SUT. Uma sistema simples de calculadora.

def add (a,b): return a+b
def sub (a,b): return a-b
def div (a,b): return a/b
def mul (a,b): return a*b

operations = {
    "1": add,
    "2": sub,
    "3": mul,
    "4": div
}

input_a = float(input("Para calcularmos precisaremos de 2 números.\n Insira o 1º:\t  "))
input_b = float(input("\nPara calcularmos precisaremos de 2 números.\n Insira o 2º:\t  "))

print(f'\nEscolha a operação desejada:\n'
      '\t1 - Adição\n'
      '\t2 - Subtração\n'
      '\t3 - Multiplicação\n'
      '\t4 - Divisão\n')

op = input("Digite o número da operação desejada: \n")

operation = operations.get(op)

if operation:
    print(f'Resultado: {operation(input_a, input_b)}')
else:
    print("operação inválida.")
"""
#endregion

#region Os testes unitários devem ser automatizados e não interativos. Essa versão do SUT é, portanto, a mais adequada
def add (a,b): return a+b
def sub (a,b): return a-b
def div (a,b): return a/b
def mul (a,b): return a*b

def calculate(a,b,op):
    operations = {
        "1": add,
        "2": sub,
        "3": mul,
        "4": div
    }
    operation = operations.get(op)
    if operation: 
        return operation(a, b)
    else:
        raise ValueError("Operação inválida")
#endregion    

