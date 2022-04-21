# -----------------------------------------------------------------------------
# Файл реализующий форматирование текста новости.
# -----------------------------------------------------------------------------
from nltk.corpus import stopwords
from pymorphy2 import MorphAnalyzer


# ф-ия проверки символа,отсеевает лишние
def is_not_punctuation(symbol: str) -> bool:
    acceptable_symbols = set(
        'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz \n')

    if symbol in acceptable_symbols:
        return True
    return False


# ф-ия отсеивающая стоп-слова и приводящая к начальной форме другие
def formate_text(text: str) -> list:
    pymorph = MorphAnalyzer()
    stoppers = set(stopwords.words('russian'))

    text_list = ''.join(filter(is_not_punctuation, text.lower())).split()
    result_words = [pymorph.parse(word)[0].normal_form for word in
                    text_list if word not in stoppers]
    return result_words
