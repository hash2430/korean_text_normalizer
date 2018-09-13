#-*- coding: utf-8 -*-

PAD = '_'
EOS = '~'
PUNC = '!\'(),-.:;?'
SPACE = ' '

JAMO_LEADS = "".join([chr(_) for _ in range(0x1100, 0x1113)])
JAMO_VOWELS = "".join([chr(_) for _ in range(0x1161, 0x1176)])
JAMO_TAILS = "".join([chr(_) for _ in range(0x11A8, 0x11C3)])

VALID_CHARS = JAMO_LEADS + JAMO_VOWELS + JAMO_TAILS + PUNC + SPACE
ALL_SYMBOLS = PAD + EOS + VALID_CHARS

char_to_id = {c: i for i, c in enumerate(ALL_SYMBOLS)}
id_to_char = {i: c for i, c in enumerate(ALL_SYMBOLS)}

# Constants for number normalization
num_to_kor1 = [""] + list("일이삼사오육칠팔구")
num_to_kor2 = [""] + list("만억조경해")
num_to_kor3 = [""] + list("십백천")

count_to_kor1 = [""] + ["한","두","세","네","다섯","여섯","일곱","여덟","아홉"]

num_to_kor = {
        '0': '영',
        '1': '일',
        '2': '이',
        '3': '삼',
        '4': '사',
        '5': '오',
        '6': '육',
        '7': '칠',
        '8': '팔',
        '9': '구',
}

upper_to_kor = {
        'A': '에이',
        'B': '비',
        'C': '씨',
        'D': '디',
        'E': '이',
        'F': '에프',
        'G': '지',
        'H': '에이치',
        'I': '아이',
        'J': '제이',
        'K': '케이',
        'L': '엘',
        'M': '엠',
        'N': '엔',
        'O': '오',
        'P': '피',
        'Q': '큐',
        'R': '알',
        'S': '에스',
        'T': '티',
        'U': '유',
        'V': '브이',
        'W': '더블유',
        'X': '엑스',
        'Y': '와이',
        'Z': '지',
}

count_tenth_kor = {
        "한십": "열",
        "십": "열",
        "두십": "스물",
        "세십": "서른",
        "네십": "마흔",
        "다섯십": "쉰",
        "여섯십": "예순",
        "일곱십": "일흔",
        "여덟십": "여든",
        "아홉십": "아흔",  # 아래서부터는 추가
        "한백": "백",
        "두백": "이백",
        "세백": "삼백",
        "네백": "사백",
        "다섯백": "오백",
        "여섯백": "육백",
        "일곱백": "칠백",
        "여덟백": "팔백",
        "아홉백": "구백",
        "한천": "천",
        "두천": "이천",
        "세천": "삼천",
        "네천": "사천",
        "다섯천": "오천",
        "여섯천": "육천",
        "일곱천": "칠천",
        "여덟천": "팔천",
        "아홉천": "구천",
}

noncount_tenth_kor = {
        "일십": "십",
        "일백": "백",
        "일천": "천",
}