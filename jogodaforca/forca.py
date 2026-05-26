import random

# Lista de palavras
palavras = [
    "python", "programacao", "computador", "internet", "teclado",
    "algoritmo", "software", "desenvolvedor", "sistema", "terminal",
    "celular", "escola", "professor", "aluno", "livro", "janela",
    "mouse", "tela", "codigo", "funcao"
]

def escolher_palavra():
    return random.choice(palavras).upper()

def mostrar_palavra(palavra, letras_acertadas):
    return " ".join([letra if letra in letras_acertadas else "_" for letra in palavra])

def jogar():
    while True:
        palavra_secreta = escolher_palavra()
        letras_acertadas = []
        letras_tentadas = []
        vidas = 6
        pontos = 0

        print("\n" + "="*45)
        print("        🎮 JOGO DA FORCA 🎮")
        print("="*45)
        print("Dica: Você pode tentar uma letra ou a palavra inteira!\n")

        while vidas > 0:
            print("Palavra:", mostrar_palavra(palavra_secreta, letras_acertadas))
            print("Letras tentadas:", " ".join(sorted(letras_tentadas)) or "Nenhuma")
            print(f"Vidas restantes: {vidas} | Pontos: {pontos}")
            print("-" * 45)

            chute = input("Digite uma letra (ou a palavra completa): ").strip().upper()

            if len(chute) == 0:
                print("Digite algo!")
                continue

            # Tentativa da palavra inteira
            if len(chute) > 1:
                if chute == palavra_secreta:
                    print("\n🎉 Parabéns! Você acertou a palavra!")
                    pontos += 30
                    break
                else:
                    print("❌ Palavra errada!")
                    vidas -= 2
                    continue

            # Tentativa de letra
            if len(chute) != 1 or not chute.isalpha():
                print("❌ Digite apenas uma letra!")
                continue

            if chute in letras_tentadas:
                print("⚠️  Você já tentou essa letra!")
                continue

            letras_tentadas.append(chute)

            if chute in palavra_secreta:
                letras_acertadas.append(chute)
                pontos += 10
                print("✅ Letra correta!")
            else:
                vidas -= 1
                pontos = max(0, pontos - 4)
                print("❌ Letra errada!")

            # Verifica se ganhou
            if all(letra in letras_acertadas for letra in palavra_secreta):
                break

        # Resultado final
        print("\n" + "="*45)
        if vidas > 0:
            print("🎉 PARABÉNS! VOCÊ VENCEU!")
        else:
            print("💀 FIM DE JOGO!")
        
        print(f"A palavra era: {palavra_secreta}")
        print(f"Pontuação final: {pontos}")
        print("="*45)

        # Jogar novamente
        novamente = input("\nQuer jogar novamente? (S/N): ").strip().upper()
        if novamente != "S":
            print("Obrigado por jogar! Até mais!")
            break


if __name__ == "__main__":
    jogar()