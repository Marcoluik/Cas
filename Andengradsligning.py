import math

a = float(input("hvad er a"))
b = float(input("Hvad er b"))
c = float(input("hvad er c"))

andengradsligning = f"Denne andengrads ligning vil nu blive beregnet {int(a)}*x^2+{int(b)}*x+{int(c)}"
print(andengradsligning)
d = b**2-4*a*c
print(f"diskriminanten er {d}")

if d > 0:
    x_1 = (-b + math.sqrt(d))/(2*a)
    x_2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"Første løsning er {x_1}")
    print(f"Anden løsning er{x_2}")
elif d == 0:
    x = (-b) / (2 * a)
    print(f"Den eneste løsning{x}")
else:
    print("Der er ingen løsninger")
