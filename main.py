numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #30

soma_pares = 0
soma_impares = 0

for numero in numeros:
    if numero % 2 == 0:
      soma_pares += numero
    elif numero % 2 != 0:
      soma_impares += numero

print(f"A soma dos números pares na lista é: {soma_pares} e a soma dos números ímpares é: {soma_impares}!")