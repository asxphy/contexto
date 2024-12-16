from src.game import Game 


game = Game()
# game.get_similar_words()
while True: 
    guess_input = input("Enter the word: ")
    if guess_input == game.today_word:
        print("You Won")
        break
    game.accept_the_guess(guess_input)