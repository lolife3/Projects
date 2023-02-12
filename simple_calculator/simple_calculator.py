import datetime
def main():
    while True:
        user_input = input('|CALCULATOR|: ').strip()
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        
        
        symbols = ['+', '-', '*', '/']
        if not any(symbol in user_input for symbol in symbols):
            print('Wrong symbol!')
            continue
        
        
        try:        
            for element in user_input:
                if element == '+':
                    x, y = user_input.split('+')
                    print(f'{user_input} =', int(x) + int(y))
                    with open('history.txt', 'a') as file:
                        file.write(f'{current_time}, OUTPUT: {user_input} = {int(x) + int(y)}\n')
                        file.close()
                    continue
                
                                    
                elif element == '-':
                    x, y = user_input.split('-')
                    print(f'{user_input} =', int(x) - int(y))
                    with open('history.txt', 'a') as file:
                        file.write(f'{current_time}, OUTPUT: {user_input} = {int(x) - int(y)}\n')
                        file.close()
                    continue
                
                
                elif element == '*':
                    x, y = user_input.split('*')
                    print(f'{user_input} =', int(x) * int(y))
                    with open('history.txt', 'a') as file:
                        file.write(f'{current_time}, OUTPUT: {user_input} = {int(x) * int(y)}\n')
                        file.close()
                    continue
                
                
                elif element == '/':
                    x, y = user_input.split('/')
                    print(f'{user_input} =', round(int(x) / int(y), 5))
                    with open('history.txt', 'a') as file:
                        file.write(f'{current_time}, OUTPUT: {user_input} = {round(int(x) / int(y), 5)}\n')
                        file.close()
                    continue
                
                
        except:
            print('Wrong value!')
            continue    
    
    
if __name__ == '__main__':
    try:
        main()
    except EOFError:
        print('\nProgram closed succesfully!')
    except KeyboardInterrupt:
        print('\n\nProgram closed succesfully!')