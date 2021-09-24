for number1 in range(999, 0, -1):
    for number2 in range(999, number1 - 1, -1):
        product = str(number1 * number2)
        if product == product[::-1]:
            print(product)