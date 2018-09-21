from ko_dictionary import *
from constant import *
import ast
import re

# 패턴 매치가 일어난 후에 매치된 부위를 한글로 치환하는 함수를 모아둔 모듈
def unit_to_korean(str, is_eng=False):
    num_str, unit_str = str.group(1), str.group(2)
    if is_eng:
        kor_unit_str = eng_unit_dictionary[unit_str]
    else:
        kor_unit_str = other_unit_dictionary[unit_str]
    return num_str + kor_unit_str


def number_to_korean(num_str, is_count=False):
    if is_count:
        num_str, unit_str = num_str.group(1), num_str.group(2)
    else:
        num_str, unit_str = num_str.group(), ""
    num_str = num_str.replace(',', '')
    num = ast.literal_eval(num_str)
    if num == 0:
        return "영"
    check_float = num_str.split('.')
    if len(check_float) == 2:
        digit_str, float_str = check_float
    elif len(check_float) >= 3:
        raise Exception(" [!] Wrong number format")
    else:
        digit_str, float_str = check_float[0], None
    if is_count and float_str is not None:
        raise Exception(" [!] `is_count` and float number does not fit each other")
    digit = int(digit_str)
    if digit_str.startswith("-") or digit_str.startswith("+"): # remove sign even if it is negative
        digit, digit_str = abs(digit), str(abs(digit))
    kor = ""
    size = len(str(digit))
    tmp = []
    for i, v in enumerate(digit_str, start=1): #i: indx, v: value
        v = int(v)
        if v != 0:
            if is_count:
                tmp += count_to_kor1[v]
            else:
                tmp += num_to_kor1[v]
            tmp += num_to_kor3[(size - i) % 4] #만 단위로 끊는다
        if (size - i) % 4 == 0 and len(tmp) != 0:
            kor += "".join(tmp)
            tmp = []
            kor += num_to_kor2[int((size - i) / 4)]
    if is_count:
        if kor.startswith("한") and len(kor) > 1:
            kor = kor[1:]
        if any(word in kor for word in count_tenth_kor):
            kor = re.sub(
                    '|'.join(count_tenth_kor.keys()),
                    lambda x: count_tenth_kor[x.group()], kor)
    if not is_count:
        if kor.startswith("일") and len(kor) > 1:# 맨 처음의 1은 읽지 않는다
            kor = kor[1:]
        if any(word in kor for word in noncount_tenth_kor):
            kor = re.sub(
                    '|'.join(noncount_tenth_kor.keys()),
                    lambda x: noncount_tenth_kor[x.group()], kor)
    #if not is_count and kor.startswith("일") and len(kor) > 1:
    #    kor = kor[1:]
    if float_str is not None:
        if len(kor) == 0:
            kor += "영"
        kor += "쩜 "
        kor += re.sub('\d', lambda x: num_to_kor[x.group()], float_str)
    if num_str.startswith("+"):
        kor = "플러스 " + kor
    elif num_str.startswith("-"):
        kor = "마이너스 " + kor
    return kor + unit_str

def alphabet_to_korean(str):
    text = str.group(0)
    return "".join(upper_to_kor[char] for char in text)