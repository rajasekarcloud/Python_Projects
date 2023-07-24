# Challenge: Rock, Paper, Scissors (*)
# The game should ask the user to enter an option (either "Rock", "Paper", or "Scissors").
# The player should play against the computer, which will select a random option.
# The computer's selection will be compared against the player's selection to determine who wins.
# A descriptive message should be displayed indicating if the player won, lost, or if the game ended in a tie.
# Basic Game Rules:
# Paper beats Rock
# Rock beats Scissors
# Scissors beat Paper.
# Sample Game 1:
# ====== Welcome to the game ======
# Please enter Rock, Paper, or Scissors below:
# Rock
# It's a tie! Try again.
# Sample Game 2:
# ====== Welcome to the game ======
# Please enter Rock, Paper, or Scissors below:
# Paper
# You lose! Your opponent chose 'Scissors'
import random;
computer = ['Rock', 'Paper', 'Scissors'];
while True:
    print(f'''====== Welcome to the game ====== \n
Please enter Rock, Paper, or Scissors below:
''');
    answer: str = str(input());
    system = random.choices(computer);
    if answer == "Rock" and system == "Scissors":
        print('You Win');
    elif answer == "Paper" and system == "Rock":
        print('You Win');
    elif answer == "Scissors" and system == "Paper":
        print('You Win');
    else:
        print(f'You Lose - {system}');
