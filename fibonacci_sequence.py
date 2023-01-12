def main():
    while True:
        try:
            userInput = int(input('How many Fibonacci Numbers?\n').strip())
            print('Index_Number: ')
            for i,v in fib(userInput-2):
                print(i + 1, ' ', v)
        except ValueError:
            continue



def fib(n):
    fib = [0,1]
    while n > 0:
        fib.append(sum(fib[-2:]))
        n -= 1
    return list(enumerate(fib))



if __name__ == '__main__':
    main()
