from abc import ABC, abstractmethod

class Transfer(ABC):
    """transfer abstractmethod"""

    @abstractmethod
    def update_training_set(word):
        """update user defined word"""

    @abstractmethod
    def text_to_text(word):
        """predict word to word_list"""
