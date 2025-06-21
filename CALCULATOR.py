#Calculadora simples <3

#Utilizado para formatar os valores, converte se o número for inteiro e mantém se ele for decimal.
def formatar_resultado(valor):
    if isinstance(valor, str):
        return valor
    return int(valor) if valor.is_integer() else valor

# Isolando as operações matemáticas aplicando o conceito de funções e suas responsábilidades únicas.
# Cada função deve fazer uma única coisa e fazê-la bem.
# Se em algum momento você precisar modificar uma função, você só precisa modificar o código da função e não afetar o resto do código.
# Isso é uma boa prática para manter o código mais organizado e fácil de manter.

#perceba que nessas funções não há nenhum print, apenas o retorno do valor da operação matemática.
def soma(num1, num2): # ex.: essa função é responsável apenas por somar dois números.
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Erro: Divisão por zero não é permitida!"
    return num1 / num2

def calcular(num1, num2, opcao):
    if opcao == '1':
        return soma(num1, num2)
    elif opcao == '2':
        return subtracao(num1, num2)
    elif opcao == '3':
        return multiplicacao(num1, num2)
    elif opcao == '4':
        return divisao(num1, num2)
    else:
        return "Opção inválida, fofo(a)!"

def obter_simbolo_operacao(opcao):
    simbolos = {
        '1': '+',
        '2': '-',
        '3': '*',
        '4': '/'
    }
    return simbolos.get(opcao, '?')

# Função principal que controla o fluxo do programa.
# Aqui é onde o usuário interage com o programa.
# Por padrão python usa o nome main para a função principal.
# Apenas na função principal eu estou usando o "print", pois é a única função que interage com o usuário.
def main():
    while True:
        print("Kawaii Calculator")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        opcao = input("Escolha um comando (1/2/3/4/5): ")
        if opcao == '5':
            print("Até mais, fofo(a)!")
            break
        if opcao in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = calcular(num1, num2, opcao)
                if isinstance(resultado, str):
                    print(resultado)
                else:
                    simbolo = obter_simbolo_operacao(opcao)
                    print(f"Resultado: {formatar_resultado(num1)} {simbolo} {formatar_resultado(num2)} = {formatar_resultado(resultado)}")
            except ValueError:
                print("Por favor, insira números válidos! Não esqueça de colocar ponto para números decimais.")
        else:
            print("Opção inválida, fofo(a)!")

if __name__ == "__main__":
    main()
