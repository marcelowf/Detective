# Detetive
#game
import time
#listagemDeDicas
dicas = ["""você está prestes a acusar alguém.
Suas opções são (pai) (mãe) (irmão) (irmã)
""",
"""seu pai disse ter passado a madrugada toda dentro do escritório e que por volta 
da meia-noite escutou um barulho esquisito vindo de um comodo próximo.""",
"você dorme em um quarto junto ao de seu irmão.",
"""sua mãe disse ter estado na sala de estar até a uma hora da manhã assistindo 
novela até sua irmã chegar, diz não ter ouvido barulho nenhum.""",
"a cozinha e o escritório são divididas por paredes bem finas.",
"sua irmã diz ter chegado em casa a meia-noite e ter escutado um barulho esquisito vindo da cozinha.",
"seu irmão está em uma viagem para fora do país.",
"sua irmã diz ter visto as luzes do escritório acesas e que não encontrou ninguém aquela noite",
"o quarto de seus pais é uma suite.",
"o quarto de seu irmão fica ao lado do escrítorio.",
"o quarto da sua irmã é ao lado da sala.",
"a entrada da casa é a sala de estar."]
#MapaDaCasa
mapa = """MAPA DA CASA:
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
#interface
print("""
Trabalho realisado por Marcelo Wzorek Filho e Luigi Dalarme
""")
time.sleep(2.5)
print("""inicando...
""")
time.sleep(2.5)
print("""Carlitos certa noite decidiu preparar uma deliciosa Quiche Lorreine, receita  
francesa ensinada por sua vó, para poder degustar no dia seguinte. No outro  
dia após uma ótima noite de sono Carlitos não mais encontra sua quiche        
onde avia deixado-a, nervoso e apavorado ele decide investigar tudo e todos   
para descobrir o verdadeiro culpado por está tragedia.                        
                                                                            
Acha que tem oque é preciso para desvendar este mistério? Se sim, então       
escolha um local para começar a caçada:                                       
{-1} = ver mapa da casa               
{0} = fazer uma acusação (você só tem uma chance)                                                    
                                                                              
{1}   {2}   {3}   {4}   {5}   {6}   {7}   {8}   {9}   {10}   {11}   {12}
 """)
#SistemaDeDicasEResultado
contador = 0
while contador == 0:
    escolha = int(input("escolha: "))
    if int(escolha) < 13 and int(escolha) > 0:
        print(dicas[escolha])
    elif escolha == 0:
        print(dicas[0])
        suspeito = str(input("escolha um suspeito: "))
        if suspeito == str("mãe") or suspeito == str("mae") or suspeito == str("MAE"):
            print("""Você finalmente encontrou o culpado! sua mãe foi a responsável 
por destruir sua torta de seus sonhos!
Após o incidente ela pediu desculpas e lhe recompensou com uma nota de cinquenta reais.""")
            contador += 1
        else:
            print("""errado, este não é o verdadeiro culpado!
Você ficou de castigo por uma semana após acusar {} injustamente""".format(suspeito))
            contador += 1
    elif escolha == -1:
        print(mapa)
    else:
        print("este não é um valor valido")
print("FIM, obriga pela atenção")
time.sleep(12)
