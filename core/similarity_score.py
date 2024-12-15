import gensim
import logging
from utils.downloader import download_model,round_similarity
import gensim.downloader as downloader
import os

# Model configuration
model_path = 'model/glove-twitter-25'
model_name = 'glove-twitter-25'

# Logging setup
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("contexto")


class UnknownWordException(Exception):
    def __init__(self, word):
        super().__init__(f"The word '{word}' is not in the model's vocabulary.")
        self.word = word



class SimilarityScorer:
    def __init__(self):
        log.info('Loading Word2Vec model...')
        download_model()  # Ensure the model is downloaded
        self.model = gensim.models.KeyedVectors.load(model_path)  # Load the saved model

    def get_similarity(self, today_word: str, guess: str):
        if today_word not in self.model.key_to_index:
            log.error(f"'{today_word}' is not in the model's vocabulary.")
            raise UnknownWordException(today_word)

        if guess not in self.model.key_to_index:
            log.error(f"'{guess}' is not in the model's vocabulary.")
            raise UnknownWordException(guess)

        # Compute similarity
        similarity = self.model.similarity(today_word, guess)
        log.info(f"Similarity between '{today_word}' and '{guess}': {similarity}")
        return round(round_similarity(similarity) * 100)

    def get_similar(self, today_word: str, n: int = 10):
        if today_word not in self.model.key_to_index:
            log.error(f"'{today_word}' is not in the model's vocabulary.")
            raise UnknownWordException(today_word)

        # Get most similar words
        similar_words = self.model.most_similar(positive=[today_word], topn=n)
        log.info(f"Top {n} similar words to '{today_word}': {similar_words}")
        return similar_words

