import random
continuar = True
tentativas = 6
aleatorio = int(random.randint(0,20))
print("--------GUESS THE NUMBER--------")
nome = input("\nEscreva o seu nome: ")
while tentativas > 0:
  num = int(input("\nInsira o seu valor: "))
  if num < aleatorio:
    print("\nÉ maior.")
    tentativas -= 1
    print(f"\nAinda tens {tentativas} tentativas!")
  elif num > aleatorio:
    print("\nÉ menor.")
    tentativas -= 1
    print(f"\nAinda tens {tentativas} tentativas!")
  elif num == aleatorio:
    print(f"\nVitória! Parabéns {nome}! Conseguiste acertar o número em {tentativas} tentativas.")
    break
  if tentativas == 0:
    print(f"\nEsgotaste as tuas tentativas! O número correto era {aleatorio}. Tavas tão perto!!!")
    while continuar:
      resposta = input("\nQueres jogar de novo? (Sim (S) | Não (N)): ")
      if resposta == "S":
            continuar = False
      elif resposta == "N":
        quit()
