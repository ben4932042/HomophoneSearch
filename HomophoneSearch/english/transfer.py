import re
import collections
from dotenv import load_dotenv, find_dotenv
from HomophoneSearch.service import Transfer
load_dotenv(find_dotenv())

class EnglishTransfer(Transfer):
    
    def update_training_set(word):
        pass

    @staticmethod
    def english_words(text):
        return re.findall('[a-z]+', text.lower())

    @staticmethod
    def train(features):
        model = collections.defaultdict(lambda: 1)
        for f in features:
            model[f] += 1
        return model

    @classmethod
    def load_model(cls):
        try:
            global NWORDS
            if not NWORDS:
                raise
        except:
            NWORDS = cls.train(
                cls.english_words(open(os.getenv("ENGLISH_TRAINING_TEXT")).read())
                )

    @staticmethod
    def edits1(word):
        n = len(word)
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        return set([word[0:i]+word[i+1:] for i in range(n)] +                     
                   [word[0:i]+word[i+1]+word[i]+word[i+2:] for i in range(n-1)] + 
                   [word[0:i]+c+word[i+1:] for i in range(n) for c in alphabet] +
                   [word[0:i]+c+word[i:] for i in range(n+1) for c in alphabet])

    @classmethod
    def known_edits2(cls, word):
        global NWORDS
        return set(e2 for e1 in cls.edits1(word) for e2 in cls.edits1(e1) if e2 in NWORDS)

    @staticmethod
    def known(words):
        global NWORDS
        return set(w for w in words if w in NWORDS)

    @classmethod
    def text_to_text(cls, word) -> list:
        cls.load_model()
        return list(
            cls.known([word]) or cls.known(cls.edits1(word)) or cls.known_edits2(word) or [word]
            )
