import re
from hanziconv import HanziConv
from pypinyin import pinyin, Style
from HomophoneSearch.Pinyin2Hanzi import DefaultDagParams, dag
from HomophoneSearch.service import Transfer


dagparams = DefaultDagParams()
user_defined_dict = {}

class ChineseTransfer(Transfer):
    
    @classmethod
    def update_training_set(cls, word) -> None:
        global user_defined_dict
        user_defined_dict[' '.join(cls.word_to_pinyin(word))] = word

    @classmethod
    def text_to_text(cls, word, return_num=10):
        global dagparams
        global user_defined_dict
        
        tone_key_list = cls.word_to_pinyin(word)
        user_word = user_defined_dict.get(' '.join(tone_key_list))
        if user_word: return_num -= 1
        result = dag(
            dagparams,
            tuple([re.sub('\d', '', i) for i in tone_key_list]),
            path_num=return_num
        )
        
        return_list = list(
            set([user_word] + [HanziConv.toTraditional(''.join(i.path)) for i in result])
            )

        return [i for i in return_list if i]
        
    @staticmethod
    def word_to_pinyin(word) -> list:
        tone_list = pinyin(
            word,
            style=Style.TONE3,
            heteronym=True
            )
        return [tone[0] for tone in tone_list]

if __name__ == "__main__":
    print(chineseTransfer.text_to_text('測試'))
