import random

# ==================================================
#        🃏 JOGO DA MEMÓRIA 🃏
# ==================================================

def criar_cartas(nivel):
    if nivel == 1:
        simbolos = ["🍎", "🍌", "🍇", "🍓"]
    elif nivel == 2:
        simbolos = ["🍎", "🍌", "🍇", "🍓", "🍉", "🍒"]
    else:
        simbolos = ["🍎", "🍌", "🍇", "🍓",
                    "🍉", "🍒", "🥝", "🍍"]

    cartas = simbolos + simbolos
    random.shuffle(cartas)

    return cartas


def mostrar_tabuleiro(cartas, descobertas, escolhidas):
    print("" + "=" * 45)
    print("              🃏 TABULEIRO 🃏")
    print("=" * 45)

    linhas = []

    for i in range(len(cartas)):
        if i in descobertas or i in escolhidas:
            valor = " " + cartas[i] + " "
        else:
            valor = " ❓ "

        linhas.append("[" + str(i + 1) + "]" + valor)

    # Tabuleiro com 4 cartas por linha
    for i in range(0, len(linhas), 4):
        print("   ".join(linhas[i:i + 4]))

    print("=" * 45)


def escolher_nivel():
    print("\n╔════════════════════════════════════╗")
    print("║        🎮 ESCOLHA O NÍVEL 🎮       ║")
    print("╠════════════════════════════════════╣")
    print("║  1 - Fácil     🍎 4 pares          ║")
    print("║  2 - Médio     🍓 6 pares          ║")
    print("║  3 - Difícil   🍍 8 pares          ║")
    print("╚════════════════════════════════════╝")

    while True:
        escolha = input("\nDigite o nível: ")

        if escolha in ["1", "2", "3"]:
            return int(escolha)

        print("❌ Opção inválida! Escolha 1, 2 ou 3.")


def escolher_carta(mensagem, cartas, descobertas, escolhidas):
    while True:
        try:
            numero = int(input(mensagem))

            posicao = numero - 1

            if posicao < 0 or posicao >= len(cartas):
                print("❌ Essa posição não existe!")
                continue

            if posicao in descobertas:
                print("⚠️ Essa carta já foi encontrada!")
                continue

            if posicao in escolhidas:
                print("⚠️ Você já escolheu essa carta!")
                continue

            return posicao

        except ValueError:
            print("❌ Digite apenas números!")


def jogar():

    print("\n" + "=" * 45)
    print("          🧠 JOGO DA MEMÓRIA 🧠")
    print("=" * 45)

    nivel = escolher_nivel()

    cartas = criar_cartas(nivel)

    descobertas = []
    tentativas = 0
    pontos = 0

    while len(descobertas) < len(cartas):

        print("\n" * 2)

        mostrar_tabuleiro(cartas, descobertas, [])

        print("\n⭐ Pontos:", pontos)
        print("🎯 Tentativas:", tentativas)

        primeira = escolher_carta(
            "\n🔎 Escolha a primeira carta: ",
            cartas,
            descobertas,
            []
        )

        mostrar_tabuleiro(
            cartas,
            descobertas,
            [primeira]
        )

        print("\n⭐ Pontos:", pontos)
        print("🎯 Tentativas:", tentativas)

        segunda = escolher_carta(
            "🔎 Escolha a segunda carta: ",
            cartas,
            descobertas,
            [primeira]
        )

        tentativas += 1

        print("\n" + "=" * 45)
        print("              🔍 RESULTADO")
        print("=" * 45)

        print("\nPrimeira carta:", cartas[primeira])
        print("Segunda carta:", cartas[segunda])

        if cartas[primeira] == cartas[segunda]:

            print("\n🎉 PARABÉNS! VOCÊ ENCONTROU UM PAR! 🎉")

            descobertas.append(primeira)
            descobertas.append(segunda)

            pontos += 100

        else:

            print("\n😢 As cartas são diferentes!")

            if pontos >= 20:
                pontos -= 20

        print("\n⭐ Pontuação:", pontos)
        print("🎯 Tentativas:", tentativas)

        input("\n➡️ Pressione ENTER para continuar...")

    # Tela final
    print("\n" * 3)

    print("╔════════════════════════════════════╗")
    print("║                                    ║")
    print("║        🏆 VOCÊ VENCEU! 🏆          ║")
    print("║                                    ║")
    print("║     🧠 MEMÓRIA INCRÍVEL! 🧠       ║")
    print("║                                    ║")
    print("╚════════════════════════════════════╝")

    print("\n🎯 Total de tentativas:", tentativas)
    print("⭐ Pontuação final:", pontos)

    if tentativas <= len(cartas) // 2 + 2:
        print("\n🌟 Excelente! Você foi muito rápido!")
    elif tentativas <= len(cartas):
        print("\n👏 Muito bom! Você encontrou todos os pares!")
    else:
        print("\n💪 Parabéns! Continue treinando sua memória!")

    print("\n")


# ==================================================
#                 MENU PRINCIPAL
# ==================================================

while True:

    print("\n")
    print("╔════════════════════════════════════╗")
    print("║                                    ║")
    print("║       🃏 JOGO DA MEMÓRIA 🃏        ║")
    print("║                                    ║")
    print("║       🧠 TESTE SUA MEMÓRIA!        ║")
    print("║                                    ║")
    print("╠════════════════════════════════════╣")
    print("║                                    ║")
    print("║        1 - 🎮 Jogar                ║")
    print("║        2 - ❌ Sair                 ║")
    print("║                                    ║")
    print("╚════════════════════════════════════╝")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":

        jogar()

        continuar = input("\n🔄 Deseja jogar novamente? (s/n): ")

        if continuar.lower() != "s":
            print("\n👋 Obrigado por jogar!")
            print("Até a próxima! 🃏")
            break

    elif opcao == "2":

        print("\n👋 Obrigado por jogar!")
        print("Até a próxima! 🃏")
        break

    else:

        print("\n❌ Opção inválida!")
