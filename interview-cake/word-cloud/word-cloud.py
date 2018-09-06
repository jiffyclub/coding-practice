import re

from collections import Counter
from string import punctuation, whitespace


def count_only_words1(input_: str) -> Counter:
    return Counter(
        ''.join(x.lower() for x in input_ if x not in punctuation).split())


print(count_only_words1('I like pie! Do you like pie?'))


def count_only_words_re(input_: str) -> Counter:
    return Counter(
        word.group().lower() for word in re.finditer(r'\w+', input_))


print(count_only_words_re('I like pie! Do you like pie?'))


def yield_words(input_: str) -> str:
    ignored = set(punctuation + whitespace)

    word_start = 0
    in_word = False

    for idx, x in enumerate(input_):
        if x not in ignored and not in_word:
            # start of a word
            in_word = True
            word_start = idx
        elif x in ignored and in_word:
            # end of word
            yield input_[word_start:idx].lower()
            in_word = False


def count_only_words3(input_: str) -> Counter:
    return Counter(yield_words(input_))


print(list(yield_words('I like pie! Do you like pie?')))
print(count_only_words3('I like pie! Do you like pie?'))
