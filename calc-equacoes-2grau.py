import os
import time
import math
time.sleep(1)
while True:
  os.system('clear')
  #
  print("Calcular equações de segundo grau.")
  print("Sua equação é completa ou incompleta?")
  print("1 - Completa")
  print("2 - Incompleta")
  print("3 - Sair")
  #
  opcao = int(input("Digite a opção: "))
  if opcao == 1:
    os.system('clear')
    print("Calcular equações de segundo grau completa.")
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    delta = (b**2) - (4*a*c)
    print(f"O valor de delta é {delta}.")
    if delta < 0:
      print("Não existem raízes reais.")
      time.sleep(3)
      input("Pressione qualquer tecla.")
      os.system('clear')
      continue
    elif delta == 0:
      x = (-b)/(2*a)
      print("A equação possui apenas uma raiz real.")
      print("x = ", x)
      time.sleep(3)
      input("Pressione qualquer tecla.")
      os.system('clear')
      continue
    else:
      x1 = ((-b) + (delta**0.5))/(2*a)
      x2 = ((-b) - (delta**0.5))/(2*a)
      print("A equação possui duas raízes reais.")
      print("x1 = ", x1)
      print("x2 = ", x2)
      time.sleep(3)
      input("Pressione qualquer tecla.")
      os.system('clear')
      continue
  elif opcao == 2:
    os.system('clear')
    print("Calcular equações de segundo grau incompleta.")
    print("Em qual termo sua equação é incompleta?")
    print("1 - Termo A")
    print("2 - Termo B")
    print("3 - Termo C")
    print("4 - Termo B e C")
    print("5 - Sair")
    opcao2 = int(input("Digite a opção: "))
    if opcao2 == 1:
      os.system('clear')
      print("Uma equação incompleta no termo A se torna uma equação de primeiro grau.")
      b = float(input("Digite o valor de b: "))
      c = float(input("Digite o valor de c: "))
      x = (-c)/b
      print("x = ", x)
      input("Pressione qualquer tecla.")
      time.sleep(3)
      os.system('clear')
      continue
    elif opcao2 == 2:
      os.system('clear')
      print("Uma equação de segundo grau incompleta em B se resolve isolando a variável, realizando divisão e raiz quadrada.")
      a = float(input("Digite o valor de a: "))
      c = float(input("Digite o valor de c: "))
      x = (-c)/a
      x = math.sqrt(x)
      print("x = ", x)
      time.sleep(3)
      input("Pressione qualquer tecla.")
      os.system('clear')
      continue
    elif opcao2 == 3:
      os.system('clear')
      print("Uma equação de segundo grau incompleta em C se resolve através do método de evidência.")
      a = int(input("Digite o valor de a: "))
      b = int(input("Digite o valor de b: "))
      c = 0
      x1 = (-b + math.sqrt((b*b) - (4*(a*c))))/(2*a)
      x2 = (-b - math.sqrt((b*b) - (4*(a*c))))/(2*a)
      print("x1 = ", x1)
      print("x2 = ", x2)
      time.sleep(3)
      input("Pressione qualquer tecla.")
      os.system('clear')
      continue
    elif opcao2 == 4:
      os.system('clear')
      print("Uma equação de segundo grau incompleta em B e C sempre recebe o valor 0 em x")
      print("x1 = 0")
      print("x2 = 0")
      input("Pressione qualquer tecla.")
    elif opcao2 == 5:
      os.system('clear')
      continue
    else:
      print("Opção inválida.")
      time.sleep(3)
      os.system('clear')
      continue
  elif opcao == 3:
    os.system('clear')
    print("Saindo...")
    time.sleep(1)
    break
