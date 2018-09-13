#-*- coding: utf-8 -*-
import re
import ast
from jamo import hangul_to_jamo
# import nltk
# nltk.download('punkt')
from ko_dictionary import *
from patterns import *
from constant import *
from normalization_rules import *
from DictionaryMissException import DictionaryMissException

def is_lead(char):
    return char in JAMO_LEADS

def is_vowel(char):
    return char in JAMO_VOWELS

def is_tail(char):
    return char in JAMO_TAILS

def get_mode(char):
    if is_lead(char):
        return 0
    elif is_vowel(char):
        return 1
    elif is_tail(char):
        return 2
    else:
        return -1

def _get_text_from_candidates(candidates):
    if len(candidates) == 0:
        return ""
    elif len(candidates) == 1:
        return _jamo_char_to_hcj(candidates[0])
    else:
        return j2h(**dict(zip(["lead", "vowel", "tail"], candidates)))

def jamo_to_korean(text):
    text = h2j(text)
    idx = 0
    new_text = ""
    candidates = []
    while True:
        if idx >= len(text):
            new_text += _get_text_from_candidates(candidates)
            break
        char = text[idx]
        mode = get_mode(char)
        if mode == 0:
            new_text += _get_text_from_candidates(candidates)
            candidates = [char]
        elif mode == -1:
            new_text += _get_text_from_candidates(candidates)
            new_text += char
            candidates = []
        else:
            candidates.append(char)
        idx += 1
    return new_text



def compare_sentence_with_jamo(text1, text2):
    return h2j(text1) != h2j(text)

def tokenize(text, as_id=False):
    text = normalize(text)
    tokens = list(hangul_to_jamo(text))
    if as_id:
        return [char_to_id[token] for token in tokens] + [char_to_id[EOS]]
    else:
        return [token for token in tokens] + [EOS]

def tokenizer_fn(iterator):
    return (token for x in iterator for token in tokenize(x, as_id=False))

def normalize(text):
    text = text.strip() #문자열 양쪽에 있는 한 칸 이상의 연속된 공백들을 모두 지운다.
    text = normalize_unit(text)
    text = normalize_number(text)
    text = normalize_english(text)
    text = re.sub('[a-zA-Z]+', normalize_upper, text)
    #text = normalize_quote(text)
    # if include_alphabet(text) != None:
    #     raise DictionaryMissException(text)
    return text

def include_alphabet(text):
    result = False
    result = re.match('[a-zA-Z]+', text)
    return result

def normalize_with_dictionary(text, dic):
    if any(key in text for key in dic.keys()):
        pattern = re.compile('|'.join(re.escape(key) for key in dic.keys()))
        return pattern.sub(lambda x: dic[x.group()], text)
    else:
        return text

def normalize_english(text):
    def fn(m):
        word = m.group()
        word = word.upper()
        if word in english_dictionary:
            return english_dictionary.get(word)
        else:
            return word
    text = re.sub("([A-Za-z]+)", fn, text)
    return text

def normalize_upper(text):
    text = text.group(0)
    # if all([char.isupper() for char in text]):
    #     return "".join(upper_to_kor[char] for char in text)
    # else:
    #     return text
    text = text.upper()
    return "".join(upper_to_kor[char] for char in text)

def normalize_quote(text):
    def fn(found_text):
        from nltk import sent_tokenize # NLTK doesn't along with multiprocessing
        found_text = found_text.group()
        unquoted_text = found_text[1:-1]
        sentences = sent_tokenize(unquoted_text)
        return " ".join(["'{}'".format(sent) for sent in sentences])
    return re.sub(quote_pattern, fn, text)

'''
숫자 뒤에 unit 토큰이 오면 숫자는 냅두고 unit 토큰만 normalize한다.
이렇게 하는 이유는 'm'같은 토큰의 경우 
alphabet normalize를 number normalize보다 먼저하면 m을 미터로 읽을 방법이 없고
number normalize를 먼저하고 이 때 알파벳 unit을 normalize를 해버리면 문자열에 필요한 m이었어도 미터로 읽어버린다.
'''

def normalize_unit(text):
    text = re.sub(number_pattern + eng_unit_pattern,
                  lambda x:unit_to_korean(x, True), text)
    text = re.sub(number_pattern + other_unit_pattern,
                  lambda x:unit_to_korean(x, False), text)
    return text



def normalize_number(text):
    text = normalize_with_dictionary(text, etc_dictionary)
    text = re.sub(number_pattern + noncount_pattern,
                  lambda x: number_to_korean(x, True), text)
    text = re.sub(number_pattern + count_pattern,
                  lambda x: number_to_korean(x, True), text)
    text = re.sub(number_pattern,
                  lambda x: number_to_korean(x, False), text)
    return text