for number in range(56, 1985):
    addad = []
    for divisor in range(2, number):
        if number % divisor == 0:
            addad.append(divisor)
    if len(addad) > 0:
        print(number, addad)
