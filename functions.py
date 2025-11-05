import datetime, random

def calculate_age(birthdate):
    # calculate the age based on the given birthday in (YYYYMMDD) format
    # today year - birthday year plus check if the birthday happened or not
    today = datetime.date.today()
    birth_year = int(birthdate[0:4])
    birth_month = int(birthdate[4:6])
    birth_day = int(birthdate[6:8])
    birth_date = datetime.date(birth_year, birth_month, birth_day)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day)) # check if the birthday happened or not
    return age
def generate_lucky_list():
    # generate a list of numbers to choose from
    lucky_list = random.sample(range(1, 101), 9)
    return lucky_list

def name_age_check():
    '''here we handle the palyer's name and age
    we ask for a valid name and last name
    we also ask for a birthday and conder it to age'''
    while True:
        # check valid name and age
        valid_name = False
        while not valid_name:
            try:
                player_name = input("Enter your name: ").strip()
                if not isinstance(player_name, str):
                    print("Name is not valid.")
                    continue
                elif not len(player_name.split(' ')) == 2:
                    print("Enter your first and last name only.")
                    continue
            
            except Exception as e:
                print(f"An error occurred: {e}")
                continue
            valid_name = True
        valid_birthday = False
        while not valid_birthday:
            try:
                player_birthdate = input("Enter your birthdate (YYYYMMDD): ").strip()
                if not player_birthdate.isdigit() or len(player_birthdate) != 8:
                    print("Birthdate is not valid.")
                    continue
                elif not int(player_birthdate[0:4]) > 1900:
                    print("Your year is not valid!")
                    continue
                elif not 1 <= int(player_birthdate[4:6]) <= 12:
                    print("Your month is not valid!")
                    continue
                elif not 1 <= int(player_birthdate[6:8]) <= 31:
                    print("Your day is not valid!")
                    continue
                # check age
                elif calculate_age(player_birthdate) < 18:
                    print("You must be at least 18 years old to play.")
                    continue
            except Exception as e:
                print(f"An error occurred: {e}")
                continue
            valid_birthday = True
        player_age = calculate_age(player_birthdate)
        print(f"Welcome {player_name}, age {player_age}, to the Lucky Number Game!", end='\n')
        break

def main_loop():
    # main game loop
    while True:
        # Reset tries count for each new game
        tries_count = 0
        lucky_list=generate_lucky_list()
        lucky_number = random.sample(range(1, 101),1)[0]
        lucky_list.append(lucky_number)
        lucky_list.sort()
        print (f'lucky list is {lucky_list}')
        game_won = False
        while not game_won:
            try:
                player_input = input("Choose the lucky number from the list: ").strip()
                if not player_input.isdigit():
                    print("Input is not valid.")
                    continue
                player_input= int(player_input)
                if player_input not in lucky_list:
                    print("Input is not in the lucky list.")
                    continue
                tries_count += 1

                if player_input == lucky_number:
                    print(f"Congrats, game is over! And you got lucky number from try #{tries_count} \n:) ", end='\n')
                    game_won = True

                else:
                    print("Sorry, wrong guess. Try again!")
                    min= lucky_number-10
                    max= lucky_number+10
                    shorter_lucky_list = [x for x in lucky_list if x > min and x < max]
                    print(f'this is try#{tries_count} and new list is:{shorter_lucky_list}, choose the lucky number?\n')

                    if len(shorter_lucky_list) < 3:
                        print(f'The new list is too small, we end the game here!\n', end='\n')
                        break

                    continue
            except Exception as e:
                print(f"An error occurred: {e}")
                continue
        # game finished but we can check if the player wants to play again
        while True:
            continue_game = input("Do you like to play again? (Input y: Yes, and n: NO) ").strip().lower()
            
            if continue_game == 'y':
                break  # Break out of the 'play again' loop, returning to the start of the outer 'while True' game loop
            elif continue_game == 'n':
                print("Thank you for playing. Goodbye!\n", end='\n')
                break 
            else:
                print("Invalid input. Please enter 'y' or 'n'.\n", end='\n')
                continue
        if continue_game == 'n':
            break  # Exit the main game loop to exit the game
if __name__ == "__main__":
    name_age_check()
    main_loop()