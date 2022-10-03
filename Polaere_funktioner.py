import math
svar = int(input("Har du x og y? Skriv 1 hvis ja, Skriv 0 hvis nej" ))
if bool(svar):
    x = float(input("Hvad er x"))
    y = float(input("hvad er y"))
    if x > 0:
        y_over_x = y/x
    if x < 0:
        y_over_x = y/x
    if x < 0:
        print("epsilon = 1")
        print(f"Kordinatsættet er {x},{y}")
        theta = math.atan(y_over_x)+math.pi
        print(f"theta er = {theta}")
        r = math.sqrt(x**2+y**2)
        print(f"r = {r}")
    elif x == 0:
        if y > 0:
            print("da y er positiv er theta = pi/2")
        if y < 0:
            print("da y er negativ er theta = 3*pi/2")
        if y == 0:
            print("da y er 0 er then 0")
    if x > 0:
        print("epsilon = 0")
        print(f"Kordinatsættet er x={x} y={y}")
        theta = math.atan(y_over_x) + 0 *math.pi
        print(f"theta er = {theta}")
        r = math.sqrt(x ** 2 + y ** 2)
        print(f"r = {r}")
else:
    r = float(input("Hvad er r"))
    theta = float(input("hvad er theta"))
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    print(f"x = {x}, y = {y}")
    svar = int(input("Kender du nu x og y? tryk 1 hvis ja tryk 0 hvis nej"))
    if bool(svar):
        x = float(input("Hvad er x"))
        y = float(input("hvad er y"))
        if x > 0:
            y_over_x = y / x
        if x < 0:
            y_over_x = y / x
        if x < 0:
            print("epsilon = 1")
            print(f"Kordinatsættet er {x},{y}")
            theta = math.atan(y_over_x) + math.pi
            print(f"theta er = {theta}")
            r = math.sqrt(x ** 2 + y ** 2)
            print(f"r = {r}")
        elif x == 0:
            if y > 0:
                print("da y er positiv er theta = pi/2")
            if y < 0:
                print("da y er negativ er theta = 3*pi/2")
            if y == 0:
                print("da y er 0 er then 0")
        if x > 0:
            print("epsilon = 0")
            print(f"Kordinatsættet er x={x} y={y}")
            theta = math.atan(y_over_x) + 0 * math.pi
            print(f"theta er = {theta}")
            r = math.sqrt(x ** 2 + y ** 2)
            print(f"r = {r}")

