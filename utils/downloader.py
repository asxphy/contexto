import gensim
import logging
import gensim.downloader as downloader
import os

# Model configuration
model_path = 'model/glove-twitter-25'
model_name = 'glove-twitter-25'

# Logging setup
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("contexto")

def download_model():
    if not os.path.exists(model_path):
        log.info(f"Model does not exist. Loading Word2Vec model: {model_name}")
        model = downloader.load(model_name)  # Download and load the model
        log.info("Model loaded")
        model.save(model_path)  # Save the model for future use
        log.info(f"Model saved to {model_path}")
    else:
        log.info("Model already exists. Skipping download.")


def round_similarity(similarity):
    if similarity < 0.01:
        return 0.01
    return round(similarity, 2)