import csv
import random
import sys


class Profile():
    def __init__(self, name, level=1, rolls=1):
        self._name = name
        self._rolls = int(rolls)
        self._level = int(level)


    def __str__(self):
        return f"Profile name: {self._name}, Level: {self._level}, Rolls available: {self._rolls}"


    def generate_level(self): # GENERATE LEVELS
        try:
            while True:
                operators = ['+','-']
                if self._level > 10:
                    print('Congratulations! On LEVEL 10 you unlocked new operator: ^ (Exponentiation)')
                    operators = ['+','-', '*', '^']
                elif self._level > 5:
                    print('Congratulations! On LEVEL 5 you unlocked new operator: * (Multiplication)')
                    operators = ['+','-', '*']


                randomOperator = random.choice(operators)
                if randomOperator == '+':
                    expressionOne = random.randint(0, (15 * self._level))
                    expressionTwo = random.randint(0, (15 * self._level))
                    try:

                        print(f'\n\nLevel:{self._level}     Solve: {expressionOne} + {expressionTwo} = ')

                        userInput = input(f'Rolls Available:{self._rolls} (Type ROLL to generate new level) \nNumber:').strip().lower()
                        if userInput == 'roll' and self._rolls > 0 :
                            self._rolls -= 1
                            pass

                        elif int(userInput) == expressionOne + expressionTwo:
                            self._level += 1
                            save(2, self._name, self._level, self._rolls)

                        else:
                            delete('YOU LOST! YOUR PROFILE IS TERMINATED!', obj=self._name)
                            sys.exit()

                    except ValueError:
                        print('\nPlease type in only numbers!')
                        raise KeyboardInterrupt

                elif randomOperator == '-':
                    expressionOne = random.randint(0, (12 * self._level))
                    expressionTwo = random.randint(0, (12 * self._level))
                    if expressionOne > expressionTwo:
                        try:

                            print(f'\n\nLevel:{self._level}     Solve: {expressionOne} - {expressionTwo} = ')

                            userInput = input(f'Rolls Available:{self._rolls} (Type ROLL to generate new level) \nNumber:').strip().lower()
                            if userInput == 'roll' and self._rolls > 0 :
                                self._rolls -= 1
                                pass

                            elif int(userInput) == expressionOne - expressionTwo:
                                self._level += 1
                                save(2, self._name, self._level, self._rolls)

                            else:
                                delete('YOU LOST! YOUR PROFILE IS TERMINATED!', obj=self._name)
                                sys.exit()

                        except ValueError:
                            print('\nPlease type in only numbers!')
                            raise KeyboardInterrupt
                    else:
                        continue
                elif randomOperator == '*':
                    expressionOne = random.randint(0, (3 * self._level))
                    expressionTwo = random.randint(0, (3 * self._level))
                    try:

                        print(f'\n\nLevel:{self._level}     Solve: {expressionOne} x {expressionTwo} = ')

                        userInput = input(f'Rolls Available:{self._rolls} (Type ROLL to generate new level) \nNumber:').strip().lower()
                        if userInput == 'roll' and self._rolls > 0 :
                            self._rolls -= 1
                            pass

                        elif int(userInput) == expressionOne * expressionTwo:
                            self._level += 1
                            save(2, self._name, self._level, self._rolls)

                        else:
                            delete('YOU LOST! YOUR PROFILE IS TERMINATED!', obj=self._name)
                            sys.exit()

                    except ValueError:
                        print('\nPlease type in only numbers!')
                        raise KeyboardInterrupt

                elif randomOperator == '^':
                    try:
                        expressionOne = random.randint(0, (2 * self._level))

                        print(f'\n\nLevel:{self._level}     Solve: {expressionOne} ^ {2} = ')

                        userInput = input(f'Rolls Available:{self._rolls} (Type ROLL to generate new level) \nNumber:').strip().lower()
                        if userInput == 'roll' and self._rolls > 0 :
                            self._rolls -= 1
                            pass

                        elif int(userInput) == expressionOne ** 2:
                            self._level += 1
                            save(2, self._name, self._level, self._rolls)

                        else:
                            delete('YOU LOST! YOUR PROFILE IS TERMINATED!', obj=self._name)
                            sys.exit()

                    except ValueError:
                        print('\nPlease type in only numbers!')
                        raise KeyboardInterrupt

        except KeyboardInterrupt:
            print()
            print(r'GAME INTERRUPTED. Do you wish to go back to main menu?')
            if input(r'(Y\N): ').strip().upper() == 'Y':
                return
            else:
                sys.exit('GAME CLOSED SUCCESFULLY')


def save(type, name, level, rolls):    # SAVE PROFILE
    if type == 1:     # SAVE FROM MENU
        with open('profiles.csv', 'a') as file:
            field = ['name', 'level', 'rolls']
            profileWriter = csv.DictWriter(file, fieldnames=field)
            profileWriter.writerow({'name': name, 'level': level, 'rolls': rolls})

    if type == 2:      # LEVEL UP!
        profileAll = []
        with open('profiles.csv', 'r') as file:
            field = ['name', 'level', 'rolls']
            profileReader = csv.DictReader(file, fieldnames=field)
            for row in profileReader:
                profileAll.append(row)
                if row['name'].lower() == str(name).lower():
                    profileAll.remove(row)

        with open('profiles.csv', 'w') as file2:
            field = ['name', 'level', 'rolls']
            profileWriter = csv.DictWriter(file2, fieldnames=field)
            profileWriter.writerows(profileAll)
            profileWriter.writerow({'name': name, 'level': level, 'rolls': rolls})



def load(chosenProfile):                       #LOAD PROFILE
    with open('profiles.csv', 'r') as file:
        field = ['name', 'level', 'rolls']
        profileReader = csv.DictReader(file, fieldnames=field)
        for row in profileReader:
            if row['name'].lower() == chosenProfile:
                name = row['name']
                level = row['level']
                rolls = row['rolls']
    print('\nProfile loaded succesfully')
    return (name,level,rolls)



def delete(message=None, obj=None):                      #DELETES PROFILE
        profileAll = []
        with open('profiles.csv', 'r') as file:
            field = ['name', 'level', 'rolls']
            profileReader = csv.DictReader(file, fieldnames=field)
            for row in profileReader:
                profileAll.append(row)
                if row['name'].lower() == obj:
                    profileAll.remove(row)

        with open('profiles.csv', 'w') as deletedFile:
            field = ['name', 'level', 'rolls']
            profileWriter = csv.DictWriter(deletedFile, fieldnames=field)
            profileWriter.writerows(profileAll)
        print(message)


def menu():                                                     #LOADS MAIN MENU
    print('\nWelcome to THE GAME. \nLoad your profile, please \nIf you lose it WILL get DELETED! \nAvailable commands: NEW / LOAD / DELETE')
    while True:
        userInput = input('\n|MAIN MENU| Enter command: ').strip().lower()
        try:
            match userInput:
                case 'new':
                    profile = Profile(input('Enter profile name: ').strip())
                    save(1, profile._name, profile._level, profile._rolls)
                    print('\nProfile created succesfully')
                    print(profile)


                case 'delete':
                    with open('profiles.csv', 'r') as file1:
                        field = ['name', 'level', 'rolls']
                        profileReader = csv.DictReader(file1, fieldnames=field)
                        profileList = []
                        for row in profileReader:
                            profileList.append(row['name'])

                    print('\nPlease choose one profile: ', profileList)
                    chosenProfile = input('Enter profile name: ').strip().lower()

                    delete('Profile deleted', obj=chosenProfile)

                case 'load':
                    with open('profiles.csv', 'r') as file:
                        field = ['name', 'level', 'rolls']
                        profileReader = csv.DictReader(file, fieldnames=field)
                        profileList = []
                        for row in profileReader:
                            profileList.append(row['name'])

                    print('\nPlease choose one profile: ', profileList)

                    profile = Profile(*load(input('Enter profile name: ').strip().lower()))
                    print(profile)
                    print('Do you wish to start?')
                    if input('(Y/N): ').upper() == 'Y':
                        break

                case other:
                    print('Wrong command')
                    continue

        except UnboundLocalError:
                print('No profile currently loaded')
                continue
    return profile


def main():
    try:
        while True:
            profile = menu()
            profile.generate_level()


    except KeyboardInterrupt:
        print()
        sys.exit('GAME CLOSED SUCCESFULLY')


if __name__ == '__main__':
    main()
