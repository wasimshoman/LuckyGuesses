# 

import datetime, random


class name_age_check:
    '''here we handle the palyer's name and age
    we ask for a valid name and last name
    we also ask for a birthday and conder it to age'''
    def __init__(self):
        self.player_name= None
        self.player_birthdate= None
        self.player_age = None

    def start_validation(self):
        # run the valuidation sequence
        self.validate_name()
        self.validate_age()

    def validate_name(self):
        # check valid name for the player
        valid_name = False
        while not valid_name:
            try:
                self.player_name = input("Enter your fist and last name : ").strip()
                if not self.player_name:
                    print("Name cannot be empty.")
                    continue
                if not isinstance(self.player_name, str):
                    print("Name is not valid (letters and spaces only).")
                    continue
                if not len(self.player_name.split(' ')) == 2:
                    print("Enter your first and last name only.")
                    continue
                valid_name = True # here we break the loop
            except Exception as e:
                print(f"An error occurred: {e}")
                continue
    def validate_age(self):
        # check for a valid birthday for the player
        valid_birthday = False
        while not valid_birthday:
            try:
                self.player_birthdate = input("Enter your birthdate (YYYYMMDD): ").strip()
                if not self.player_birthdate.isdigit() or len(self.player_birthdate) != 8:
                    print("Birthdate is not valid.")
                    continue
                if not int(self.player_birthdate[0:4]) > 1900:
                    print("Your year is not valid!")
                    continue
                if not 1 <= int(self.player_birthdate[4:6]) <= 12:
                    print("Your month is not valid!")
                    continue
                if not 1 <= int(self.player_birthdate[6:8]) <= 31:
                    print("Your day is not valid!")
                    continue
                # calculate age
                self.player_age = self.calculate_age()
                # check age
                if self.player_age < 18:
                    print("You must be at least 18 years old to play.")
                    continue
                print(f"Welcome {self.player_name}, age {self.player_age}, to the Lucky Number Game!", end='\n')
            except Exception as e:
                print(f"An error occurred: {e}")
                continue
            valid_birthday = True
    def calculate_age(self) -> int:
        # calculate the age based on the given birthday in (YYYYMMDD) format
        # today year - birthday year plus check if the birthday happened or not
        try:
            today = datetime.date.today()
            birth_year = int(self.player_birthdate[0:4])
            birth_month = int(self.player_birthdate[4:6])
            birth_day = int(self.player_birthdate[6:8])
            birth_date = datetime.date(birth_year, birth_month, birth_day)
            self.age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day)) # check if the birthday happened or not
            return self.age
        except Exception as e:
            print(f"An error occurred: {e}\n")

class main_game:
    '''
    Here we start the guessing game
    '''
    def __init__(self):
        self.tries_count=None
        self.lucky_list=[]
        self.lucky_number=None
        self.player_input=None
        self.continue_game=None

    def main_loop(self):
        while True:
            # main game loop
            # Reset tries count for each new game
            # generate the lucky number list with the lucky number
            self.tries_count=0
            self.lucky_list=self.generate_lucky_list()
            self.lucky_number = random.sample(range(1, 101),1)[0]
            self.lucky_list.append(self.lucky_number)
            self.lucky_list.sort()
            print (f'Lucky list is {self.lucky_list}')
            game_won = False
            while not game_won:
                try:
                    self.player_input = input("Choose the lucky number from the list: ").strip()
                    if not self.player_input.isdigit():
                        print("Input is not valid.")
                        continue
                    self.player_input= int(self.player_input)
                    if self.player_input not in self.lucky_list:
                        print("Input is not in the lucky list.")
                        continue
                    self.tries_count += 1

                    if self.player_input == self.lucky_number:
                        print(f"Congrats, game is over! And you got lucky number from try #{self.tries_count} \n:) ", end='\n')
                        game_won = True

                    else:
                        print("Sorry, wrong guess. Try again!")
                        min_bound= self.lucky_number-10
                        max_bound= self.lucky_number+10
                        shorter_lucky_list = [x for x in self.lucky_list if x > min_bound and x < max_bound]
                        print(f'this is try#{self.tries_count} and new list is:{shorter_lucky_list}, choose the lucky number!\n')

                        if len(shorter_lucky_list) < 3:
                            print(f'The new list is too small, we end the game here!\n', end='\n')
                            break
                        
                        continue
                except Exception as e:
                    print(f"An error occurred: {e}")
                    continue
            # game finished but we can check if the player wants to play again
            while True:
                self.continue_game = input("Do you like to play again? (Input y: Yes, and n: NO) ").strip().lower()
                
                if self.continue_game == 'y':
                    break  # Break out of the 'play again' loop, returning to the start of the outer 'while True' game loop
                elif self.continue_game == 'n':
                    print("Thank you for playing. Goodbye!\n", end='\n')
                    break 
                else:
                    print("Invalid input. Please enter 'y' or 'n'.\n", end='\n')
                    continue
            if self.continue_game == 'n':
                break  # Exit the main game loop to exit the game

    def generate_lucky_list(self):
        # generate a list of numbers to choose from
        self.lucky_list = random.sample(range(1, 101), 9)
        return self.lucky_list


if __name__ == "__main__":
    # start the game 
    checker = name_age_check()
    checker.start_validation()
    main_game=main_game()
    main_game.main_loop()