"""
Jogo da Velha
"""

import os

def limpar_tela() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho() -> None:
    print('---------------------')
    print('*** Jogo da Velha ***')
    print('---------------------\n')
    print(f'Jogador 1 = "X", venceu: {vitorias_jogador1} vez(es)')
    print(f'Jogador 2 = "O", venceu: {vitorias_jogador2} vez(es)')
    print(f'Quantidade de empates  : {quantidade_empates} vez(es)\n')

def exibir_tabuleiro() -> None:
    print("  a   b   c")
    print(f"1 {jogadas['a1']} | {jogadas['b1']} | {jogadas['c1']}")
    print(f' ---|---|---')
    print(f"2 {jogadas['a2']} | {jogadas['b2']} | {jogadas['c2']}")
    print(" ---|---|---")
    print(f"3 {jogadas['a3']} | {jogadas['b3']} | {jogadas['c3']}\n")

def validar_jogada(jogada: str) -> bool:
    if jogada.lower() not in jogadas.keys():
        return False

    if not jogadas[jogada.lower()] == VAGO:
        return False

    if jogadas[jogada.lower()] == VAGO:
        return True
    
    return False

def atualizar_tabuleiro(jogador: int, jogada: str) -> None:
    global jogadas
    if jogador == 1:
        jogadas[jogada.lower()] = MARCACAO_JOGADOR1
    else:
        jogadas[jogada.lower()] = MARCACAO_JOGADOR2

def venceu_partida(jogador_atual: int) -> str:
    marcacao = MARCACAO_JOGADOR1 if jogador_atual == 1 else MARCACAO_JOGADOR2

    if (marcacao == jogadas['a1'] and marcacao == jogadas['b1'] and marcacao == jogadas['c1']) or \
            (marcacao == jogadas['a2'] and marcacao == jogadas['b2'] and marcacao == jogadas['c2']) or \
            (marcacao == jogadas['a3'] and marcacao == jogadas['b3'] and marcacao == jogadas['c3']) or \
            (marcacao == jogadas['a1'] and marcacao == jogadas['a2'] and marcacao == jogadas['a3']) or \
            (marcacao == jogadas['b1'] and marcacao == jogadas['b2'] and marcacao == jogadas['b3']) or \
            (marcacao == jogadas['c1'] and marcacao == jogadas['c2'] and marcacao == jogadas['c3']) or \
            (marcacao == jogadas['a1'] and marcacao == jogadas['b2'] and marcacao == jogadas['c3']) or \
            (marcacao == jogadas['a3'] and marcacao == jogadas['b2'] and marcacao == jogadas['c1']):
        return SIM

    if VAGO not in jogadas.values():
        return EMPATE

    return NAO

def trocar_jogador() -> None:
    global jogador_atual
    if jogador_atual == 1:
        jogador_atual = 2
    else:
        jogador_atual = 1

def limpar_jogadas():
    global jogadas
    jogadas = {i: VAGO for i in jogadas}

def atualizar_placar(jogador: int, venceu: str) -> None:
    global vitorias_jogador1
    global vitorias_jogador2
    global quantidade_empates

    if venceu == EMPATE:
        quantidade_empates += 1
        return
    
    if venceu == SIM and jogador == 1:
        vitorias_jogador1 += 1
        return

    if venceu == SIM and jogador == 2:
        vitorias_jogador2 += 1
        return

# Programa principal
EMPATE = 'EMPATE'
SIM = 'SIM'
NAO = 'NAO'
VAGO = ' '
MARCACAO_JOGADOR1 = 'X'
MARCACAO_JOGADOR2 = 'O'

jogar = True
jogador_atual = 1
jogada_atual = ''
jogadas = {
    'a1': ' ',
    'a2': ' ',
    'a3': ' ',
    'b1': ' ',
    'b2': ' ',
    'b3': ' ',
    'c1': ' ',
    'c2': ' ',
    'c3': ' '
}
quantidade_empates = 0
venceu = ''
vitorias_jogador1 = 0
vitorias_jogador2 = 0

while jogar:
    limpar_tela()
    exibir_cabecalho()
    exibir_tabuleiro()
    jogada_atual = input(f'Jogador {jogador_atual}, faça sua jogada, ex.: "a1", ou "b2" ou outra combinação válida: ')

    while not validar_jogada(jogada_atual):
        limpar_tela()
        exibir_cabecalho()
        exibir_tabuleiro()
        jogada_atual = input(f'Jogador {jogador_atual}, jogada inválida, faça sua jogada, ex.: "a1", ou "b2" ou outra combinação válida: ')

    atualizar_tabuleiro(jogador_atual, jogada_atual)

    venceu = venceu_partida(jogador_atual)

    if venceu == NAO:
        limpar_tela()
        exibir_cabecalho()
        exibir_tabuleiro()
        trocar_jogador()

    if venceu == SIM or venceu == EMPATE:
        limpar_tela()
        exibir_cabecalho()
        exibir_tabuleiro()
        
        if venceu == SIM:
            print(f'*** O jogador {jogador_atual} ganhou! ***\n')
        else:
            print(f'*** O jogo empatou! ***\n')

        opcao = input('Jogar novamente(s/n)? ')
        opcao = opcao.lower()

        if opcao == 's':
            jogar = True

        if opcao == 'n':
            jogar = False

        while opcao != 's' and opcao != 'n':
            opcao = input('Opção inválida, Jogar novamente(s/n)? ')
            opcao = opcao.lower()

            if opcao == 's':
                jogar = True

            if opcao == 'n':
                jogar = False

        atualizar_placar(jogador_atual, venceu)

        if jogar:
            limpar_jogadas()

        if not jogar:
            limpar_tela()
            exibir_cabecalho()
            print('*** Fim do jogo! ***')
