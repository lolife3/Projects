def main():
    while True:
        try:
            userInput = int(input('How many Fibonacci Numbers?\n').strip())
            print(fib(userInput-2))
        except ValueError:
            continue



def fib(n):
    fib = [0,1]
    while n > 0:
        fib.append(sum(fib[-2:]))
        n -= 1
    return fib



if __name__ == '__main__':
    main()