import os
import time
time.sleep(1)
os.system('clear')
#
def main():
  volume = (4/3) * 3.14159265359 * (raio**3)
  print(f"O volume da esfera é {volume:.2f}")
  print("-"*30)
#
while True:
  raio = input("Digite o raio da esfera: ")
  try:
    raio = float(raio)
  except ValueError:
    print("Digite um valor válido!")
    print("-"*30)
    time.sleep(1)
    continue
  main()
