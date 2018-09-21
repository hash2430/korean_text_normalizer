#-*- coding: utf-8 -*-

from patterns import *
from normalization_rules import *
from DictionaryMissException import DictionaryMissException

def normalize(text):
    text = text.strip() #문자열 양쪽에 있는 한 칸 이상의 연속된 공백들을 모두 지운다.
    text = normalize_unit(text)
    text = normalize_number(text)
    text = normalize_english(text)
    text = normalize_dictionary_miss_alphabet(text);
    # if include_alphabet(text) != None:
    #     raise DictionaryMissException(text)
    return text

def include_alphabet(text):
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

def normalize_dictionary_miss_alphabet(text):
    text = re.sub(alphabet_pattern,
                  lambda x:alphabet_to_korean(x), text);
    return text

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
                  lambda x: number_to_korean(x, False), text)
    text = re.sub(number_pattern + count_pattern,
                  lambda x: number_to_korean(x, True), text)
    text = re.sub(number_pattern,
                  lambda x: number_to_korean(x, False), text)
    return text