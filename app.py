# Price exercise

price = 100
discount = 0.1

is_discounted = True
final_price = price - (price * discount)

# if is_discounted:
#   print(f'The price is {final_price}')
# else:
#   print('not discounted')


# Guess game exercise
# secret_number = 8
# counter = 0

# while counter < 3:
#   answer = int(input('Input number: '))
#   print('secret', secret_number, 'answer', answer)
#   counter += 1
#   if answer == secret_number:
#     print('Correct answer!')
#     break
# else:
#   print('Sorry, wrong answer')

# Car games exercise
is_active = True
is_car_started = False
help_info = """
start - to start the car
stop - to stop the car
quit - to quite the game
"""

while is_active:
    user_input = input(">").lower()
    if user_input == "help":
        print(help_info)
    elif user_input == "start":
        if is_car_started:
            print("Car already started")
        else:
            print("Car started")
            is_car_started = True
    elif user_input == "stop":
        if is_car_started:
            print("Car stropped")
            is_car_started = False
        else:
            print("Car hasn't started")
    elif user_input == "quit":
        is_active = False
        break
    else:
        print("Unknown command")

# Data types

# Primitive data types (immutable)
# str, int, float, bool

# Non primitive
# list
[1, 2, 3, 4, 5, 6]

# tuple (immutable list)
(1, 2, 3, 4, 5, 6)

# dictionary
{"test": "Data"}
