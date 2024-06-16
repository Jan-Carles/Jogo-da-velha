def inicializar_tabuleiro():
    return [[' ' for _ in range(3)] for _ in range(3)]

def exibir_tabelas(tabuleiro, referencia):
    print("Referência           Jogo Atual")
    for i in range(3):
        linha_referencia = ' | '.join(referencia[i])
        linha_tabuleiro = ' | '.join(tabuleiro[i])
        print(f" {linha_referencia}         {linha_tabuleiro}")
        if i < 2:
            print("---+---+---        ---+---+---")

def jogada_valida(tabuleiro, posicao):
    linha, coluna = posicao // 3, posicao % 3
    if 0 <= posicao < 9 and tabuleiro[linha][coluna] == ' ':
        return True
    return False

def fazer_jogada(tabuleiro, posicao, jogador):
    linha, coluna = posicao // 3, posicao % 3
    tabuleiro[linha][coluna] = jogador

def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)):  # Linhas
            return True
        if all(tabuleiro[j][i] == jogador for j in range(3)):  # Colunas
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:  # Diagonal principal
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:  # Diagonal secundária
        return True
    return False

def verificar_empate(tabuleiro):
    return all(tabuleiro[i][j] != ' ' for i in range(3) for j in range(3))

def jogar_jogo_da_velha():
    tabuleiro = inicializar_tabuleiro()
    referencia = [[str(i * 3 + j) for j in range(3)] for i in range(3)]
    jogador_atual = 'X'
    
    while True:
        exibir_tabelas(tabuleiro, referencia)
        print(f"Jogador {jogador_atual}, é a sua vez.")

        posicao = int(input("Escolha uma posição (0 a 8): "))

        if jogada_valida(tabuleiro, posicao):
            fazer_jogada(tabuleiro, posicao, jogador_atual)
            
            if verificar_vitoria(tabuleiro, jogador_atual):
                exibir_tabelas(tabuleiro, referencia)
                print(f"Parabéns, jogador {jogador_atual}! Você venceu!")
                break
            
            if verificar_empate(tabuleiro):
                exibir_tabelas(tabuleiro, referencia)
                print("O jogo terminou em empate!")
                break

            jogador_atual = 'O' if jogador_atual == 'X' else 'X'
        else:
            print("Jogada inválida! Tente novamente.")

# Executa o jogo
jogar_jogo_da_velha()
