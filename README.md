# Jogo da Velha – Jogo em Python via Terminal CLI

Um clássico **Jogo da Velha** desenvolvido em Python para execução no **terminal (CLI)**.  
Dois jogadores se alternam, o tabuleiro é exibido a cada jogada, o sistema valida entradas, identifica vitória ou empate e mantém um **placar acumulado** entre as partidas.

---

## 🎯 Objetivo deste Jogo

Treinar a linguagem de programação **Python**, praticando:

- Estruturas de controle
- Funções
- Dicionários
- Laços de repetição
- Boas práticas de organização de código

---

## 🚀 Funcionalidades

* Dois jogadores (`X` e `O`)
* Tabuleiro exibido no terminal
* Validação de jogadas
* Alternância automática de jogadores
* Detecção de vitória ou empate
* Placar acumulado:
  * Vitórias do Jogador 1
  * Vitórias do Jogador 2
  * Quantidade de empates
* Opção de jogar novamente após cada partida

---

## 🧠 Regras do Jogo

* O tabuleiro possui 3 linhas e 3 colunas
* O **Jogador 1** utiliza `X`
* O **Jogador 2** utiliza `O`
* Ganha quem formar uma linha, coluna ou diagonal com sua marcação
* Caso todas as posições sejam preenchidas sem vencedor, ocorre **empate**

---

## 📦 Pré-requisitos

* Python 3 instalado
* Terminal / Prompt de Comando

---

## ▶️ Como executar

1. Clone o repositório:

```bash
git clone https://github.com/danielgois82/Python_jogo_da_velha.git
```

2. Acesse a pasta:

```bash
cd Python_jogo_da_velha
```

3. Execute o script:

```bash
python jogo_da_velha.py
```

---

## 🧩 Código
O programa funciona em um loop principal que:

**1.** Limpa a tela

**2.** Exibe o cabeçalho e o tabuleiro

**3.** Solicita a jogada do jogador atual

**4.** Valida a jogada

**5.** Atualiza o tabuleiro

**6.** Verifica se houve vitória ou empate

**7.** Atualiza o placar

**8.** Pergunta se deseja jogar novamente

---

## 🖥️ Exemplo de uso

```
---------------------
*** Jogo da Velha ***
---------------------

Jogador 1 = "X", venceu: 2 vez(es)
Jogador 2 = "O", venceu: 1 vez(es)
Quantidade de empates  : 1 vez(es)

  a   b   c
1 X | O | X
 ---|---|---
2 O | X | O
 ---|---|---
3   |   | X

*** O jogador 1 ganhou! ***

Jogar novamente(s/n)?

```
---

## 📜 Licença
Este projeto é de uso livre.
Sinta-se à vontade para **estudar, modificar, melhorar e reutilizar** o código.

---