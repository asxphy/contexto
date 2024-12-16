from src.scorer import Scorer
from src.utils.word_list import get_word_of_the_day

class Game:
    def __init__(self):
        self.guesses = 0
        self.guessed_words = []
        self.today_word = get_word_of_the_day()
        self.model = Scorer()

    def accept_the_guess(self, guessed_word):
        similarity_score = self.model.get_similarity(self.today_word,guessed_word)
        self.guessed_words.append((guessed_word,similarity_score))
        print(f"{guessed_word} - {similarity_score}")

    def get_similar_words(self,n=100):
        similar_words = self.model.get_similar(self.today_word)
        for (name,score) in similar_words:
            print(name,score)
        