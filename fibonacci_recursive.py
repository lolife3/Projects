def main():
    try:
        user_input = int(input("Type in an int: "))
        result = [fib(x) for x in range(user_input)]
        print(result)
    
    
    except ValueError:
        main()
    
    
def fib(num):
    if num in {0,1}:
        return num
    return fib(num-2) + fib(num-1)
    
if __name__ == "__main__":
    main()