import random

def escolher_palavra():
    palavras = ["desenvolvimento", "tecnologia", "programacao", "tendencias", "computador", "internet"]
    return random.choice(palavras)

def exibir_forca(tentativas):
    estagios_forca = [
        """
           _______
          |       |
                  |
                  |
                  |
                  |
        ============
        """,
        """
           _______
          |       |
          O       |
                  |
                  |
                  |
        ============
        """,
        """
           _______
          |       |
          O       |
          |       |
                  |
                  |
        ============
        """,
        """
           _______
          |       |
          O       |
         /|       |
                  |
                  |
        ============
        """,
        """
           _______
          |       |
          O       |
         /|\      |
                  |
                  |
        ============
        """,
        """
           _______
          |       |
          O       |
         /|\      |
         /        |
                  |
        ============
        """,
        """
           _______
          |       |
          O       |
         /|\      |
         / \      |
                  |
        ============
        """
    ]
    print(estagios_forca[tentativas])

def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ["_"] * len(palavra)
    tentativas = 0
    letras_tentadas = []

    print("Bem-vindo ao jogo da forca!")
    print("Adivinhe a palavra oculta.")

    while tentativas < 6:
        print("\nPalavra:", " ".join(palavra_oculta))
        letra = input("Digite uma letra: ").lower()

        if letra in letras_tentadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_tentadas.append(letra)

        if letra in palavra:
            print("Letra correta!")
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
        else:
            print("Letra incorreta!")
            tentativas += 1
            exibir_forca(tentativas)

        if "_" not in palavra_oculta:
            print("\nParabéns! Você venceu!")
            break

    if tentativas == 6:
        print("\nVocê perdeu! A palavra era:", palavra)

    print("\nObrigado por jogar!")

if __name__ == "__main__":
    jogar()