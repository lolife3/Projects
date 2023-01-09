# CS50x credit card validator

def main():
    # cardNumber = 400360000000014
    while True:
        cardNumber = input('Input card number: ').strip()
        try:
            if int(cardNumber):
                break
        except ValueError:
            continue
    validateCardNumber(cardNumber)


def validateCardNumber(cardNumber):
    number = []
    for a in str(cardNumber):
        number.append(a)
    number.reverse()

    odd = 0
    even = 0
    for i in range(len(number)):
        if (i + 1) % 2 == 0:
            product = int(number[i]) * 2
            if product >= 10:
                x = str(product)[slice(1)]
                y = str(product)[slice(1, 2)]
                odd += int(x) + int(y)
            else:
                odd += product
        else:
            even += int(number[i])

    if not (odd + even) % 10 == 0:
        print('invalid')
    else:
        print('valid')


if __name__ == '__main__':
    main()
