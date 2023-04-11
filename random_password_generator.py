import secrets


def main():
    ls = [chr(i) for i in range(33, 123)]
    
    
    while True:
        while True:
            user_input = input("Input password length (integer only): ")
            if user_input.isdigit():
                break
    
            
        password = ""    
        for i in range(int(user_input)):
            password += str(secrets.choice(ls))
            
        print(password)
    
        
if __name__ == "__main__":
    main()