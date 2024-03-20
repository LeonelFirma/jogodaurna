import random

def main():
    print("Bem-vindo ao jogo de adivinhação!")
    print("Um número entre 1 e 20 será escolhido aleatoriamente como alvo.")
    print("Você precisa adivinhar o alvo antes que ele ultrapasse 100.")
    print("Boa sorte!\n")

    alvo = random.randint(1, 20)
    total = alvo

    while total <= 100:
        palpite = int(input("Digite seu palpite (entre 1 e 20): "))

        if palpite == alvo:
            print(f"Parabéns! Você acertou o alvo {alvo}. Você venceu!")
            break
        else:
            print("Você errou!")

        total += random.randint(1, 20)

        if total > 100:
            print(f"O alvo ultrapassou 100. O alvo era {alvo}. Você perdeu!")
            break
        else:
            print(f"O alvo atual é {total}.")
            print()

if __name__ == "__main__":
    main()
