# Program to play rock, paper and scissors.
import random
import sys;
def play_game():
    your_score = 0;
    ai_score = 0;
    while True:
        user_move = input("Input Rock, Paper, Scissors? >>").lower();
        moves = {'rock':'🪨', 'paper':'📜','scissor':'✂'};
        valid_moves = list(moves.keys()); # Contains rock, paper,scissors
        if user_move == "exit":
            print("Thanks For Playing 😂😂😂")
            print("Score:");
            print("Your Score: ",your_score);
            print("AI Score: ",ai_score);
            sys.exit();
        if user_move not in valid_moves:
            print("Invalid Move 😥😥😥")
        else:
            ai_move = random.choice(valid_moves);
            print("-----");
            print("Your Move >>", user_move);
            print("AI Move >>", moves.get(ai_move));
            print("-----");
            if user_move == ai_move:
                print("Tie");
            elif user_move == 'rock' and ai_move == 'paper':
                your_score +=1;
                print("You won");
            elif user_move == 'paper' and ai_move == 'scissor':
                your_score += 1;
                print("You won");
            else:
                print("AI won");
                ai_score += 1;

play_game();
