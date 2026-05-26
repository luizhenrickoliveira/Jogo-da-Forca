# README Antiga:
# Jogo da Forca - Versão Base 

Este é um projeto pedagógico desenvolvido para a disciplina de **Programação no Desenvolvimento de Sistemas** do **3º Ano do Ensino Médio Técnico**. 

O objetivo deste código é servir como uma **estrutura inicial (boilerplate)** em Python para que os alunos compreendam a lógica de um jogo em terminal e apliquem seus conhecimentos para customizar, otimizar e expandir as funcionalidades do sistema.

##  Funcionalidades Atuais

* **Sorteio Aleatório:** Escolha automatizada de palavras utilizando a biblioteca nativa `random`.
* **Validação de Entrada (Input):** Sistema que impede o usuário de digitar mais de uma letra, caracteres numéricos/especiais ou repetir letras já tentadas.
* **Sistema de Pontuação:** Ganho de pontos a cada acerto (+10) e penalidade a cada erro (-2).
* **Controle de Vidas:** O jogador inicia com 6 vidas para tentar adivinhar a palavra secreta.

##  Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Bibliotecas:** `random` (nativa)

##  Missão dos Alunos (Propostas de Aprimoramento)

O código foi construído de forma simples para que você, estudante, possa implementar melhorias. Aqui estão os desafios propostos para a evolução do projeto:

1.  **Categorização por Temas:** Modificar a estrutura de dados das palavras para que o jogador possa escolher um tema antes de começar (ex: *Jogos, Tecnologia, Escola, Filmes*).
2.  **Interface Gráfica no Terminal (Ascii Art):** Desenhar o boneco da forca (cabeça, tronco, braços e pernas) mudando conforme o jogador perde vidas.
3.  **Tratamento de Strings:** Adicionar suporte a palavras com acentos ou caracteres especiais (ex: tratar "programacao" e "programação" corretamente).
4.  **Sistema de Ranking:** Salvar a pontuação final do jogador em um arquivo de texto (`.txt`) ou JSON para manter um histórico dos melhores jogadores.
5.  **Loop de Reinicialização:** Permitir que o jogador inicie uma nova partida sem precisar rodar o script novamente.

---
## 💻 Como Executar o Projeto

Certifique-se de ter o Python instalado em sua máquina.

1. Baixe o arquivo de código (`forca.py`).
2. Abra o terminal ou prompt de comando na pasta onde o arquivo foi salvo.
3. Execute o comando:
´
   python forca.py

# README NOVA:

#  Jogo da Forca em Python

##  O que foi Melhorado

- Interface mais limpa e organizada
- Agora é possível chutar a palavra inteira
- Pode jogar novamente sem fechar o programa
- Mensagens mais claras com emojis
- Letras tentadas aparecem em ordem alfabética
- Sistema de pontuação mais justo (não fica negativo)
- Mais palavras disponíveis
- Código mais limpo e fácil de entender

---

##  Funcionalidades

- Sorteio aleatório de palavras
- 6 vidas para o jogador
- Validação de entrada (só aceita letras)
- Sistema de pontuação
- Opção de chutar a palavra completa

---

##  Como Executar

1. Tenha o Python instalado
2. Salve o arquivo como `forca.py`
3. Abra o terminal na pasta e digite:

python forca.py
