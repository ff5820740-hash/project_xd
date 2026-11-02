def criar_tabuleiro():
    tabuleiro = []

    for i in range(3):
        tabuleiro.append([" ", " ", " "])

    return tabuleiro

def mostrar_tabuleiro(tabuleiro):
    print("  1 2 3")

    for coluna in range(3):
        print(tabuleiro[linha][coluna], end="")