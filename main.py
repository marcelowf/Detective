import time

# Listagem de Dicas
dicas = [
    """Você está prestes a acusar alguém. Suas opções são (pai) (mãe) (irmão) (irmã)""",
    """Seu pai disse ter passado a madrugada toda dentro do escritório e que, por volta da meia-noite, escutou um barulho esquisito vindo de um cômodo próximo.""",
    """Você dorme em um quarto junto ao de seu irmão.""",
    """Sua mãe disse ter estado na sala de estar até a uma hora da manhã assistindo novela até sua irmã chegar, diz não ter ouvido barulho nenhum.""",
    "A cozinha e o escritório são divididos por paredes bem finas.",
    "Sua irmã diz ter chegado em casa à meia-noite e ter escutado um barulho esquisito vindo da cozinha.",
    "Seu irmão está em uma viagem para fora do país.",
    "Sua irmã diz ter visto as luzes do escritório acesas e que não encontrou ninguém aquela noite.",
    "O quarto de seus pais é uma suíte.",
    "O quarto de seu irmão fica ao lado do escritório.",
    "O quarto da sua irmã é ao lado da sala.",
    "A entrada da casa é a sala de estar."
]

# Mapa da Casa
mapa = """
MAPA DA CASA:
          ╔═  ═╗
╔═════════╝    ╚════════╦════════════╦════╦════╦═════════════════════════╗
║                       ║            ║    ║                              ║
║                       ║            ║    ║    ║                         ║
║                       ║            ║    ║    ║                         ║
║                       ║            ║    ║    ║                         ║
║                     ╔═╩═════  ═════╬═  ═╬════╩═════════╗               ║
║                                                                        ║
╠════  ════╤════  ════╬════════════════  ════════════════╬═══════════════╝
║          │          ║              ╔═  ═╗              ║
║          │          ║              ║    ║              ║
║          │          ║              ║    ║              ║
║          │          ║              ║    ║              ║
╚══════════╧══════════╩══════════════╩════╩══════════════╝
"""

# Função para imprimir as opções de escolha
def imprimir_opcoes():
    print("""
Trabalho realizado por Marcelo Wzorek Filho e Luigi Dalarme
""")
    time.sleep(2.5)
    print("Iniciando...\n")
    time.sleep(2.5)
    print("Carlitos certa noite decidiu preparar uma deliciosa Quiche Lorreine, receita francesa ensinada por sua avó, para poder degustar no dia seguinte. No outro dia após uma ótima noite de sono, Carlitos não mais encontra sua quiche onde havia deixado-a. Nervoso e apavorado, ele decide investigar tudo e todos para descobrir o verdadeiro culpado por esta tragédia.\n\nAcha que tem o que é preciso para desvendar este mistério? Se sim, então escolha uma opção para começar a caçada:\n{-1} = ver mapa da casa\n{0} = fazer uma acusação (você só tem uma chance)\n{1}   {2}   {3}   {4}   {5}   {6}   {7}   {8}   {9}   {10}   {11}   {12}
    """)

# Função para obter a acusação do jogador
def fazer_acusacao():
    print(dicas[0])
    suspeito = input("Escolha um suspeito (pai, mãe, irmão, irmã): ").lower()
    
    if suspeito == "mãe":
        print("""Você finalmente encontrou o culpado! Sua mãe foi a responsável por destruir sua torta de seus sonhos! Após o incidente, ela pediu desculpas e lhe recompensou com uma nota de cinquenta reais.""")
        return True
    else:
        print(f"""Errado, este não é o verdadeiro culpado! Você ficou de castigo por uma semana após acusar {suspeito} injustamente.""")
        return False

# Função principal do jogo
def jogar_detetive():
    imprimir_opcoes()
    contador = 0
    
    while contador == 0:
        escolha = int(input("Escolha: "))
        
        if escolha == -1:
            print(mapa)
        elif escolha == 0:
            if fazer_acusacao():
                contador += 1
            else:
                contador += 1
        elif 0 < escolha < 13:
            print(dicas[escolha])
        else:
            print("Este não é um valor válido")

    print("FIM, obrigado pela atenção")
    time.sleep(12)

# Execução do jogo
jogar_detetive()
