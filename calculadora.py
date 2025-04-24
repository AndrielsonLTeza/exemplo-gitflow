# calculadora.py 
def soma(a, b):
    """Realiza a soma de dois números"""
    return a + b

def subtracao(a, b):
    """Realiza a subtração de dois números"""
    return a - b

# Função principal
if __name__ == "__main__":
    print("Calculadora simples")
    print("Soma 5 + 3 =", soma(5, 3))
    print("Subtração 10 - 4 =", subtracao(10, 4))