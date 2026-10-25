import math

cateto1 = float(input("Introduce el primer cateto: "))
cateto2 = float(input("Introduce el segundo cateto: "))

hipotenusa = math.sqrt(math.pow(cateto1, 2) + math.pow(cateto2, 2))

print(f"La hipotenusa es: {hipotenusa:.2f}" )
