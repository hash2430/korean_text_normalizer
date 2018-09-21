#-*- coding: utf-8 -*-

eng_unit_pattern = "[ ]?(cm|mm|m|km|g|kg|Hz|KHz|GHz)"
other_unit_pattern = "[ ]?(%|℃|㎓)"
number_pattern = "([+-]?\d[\d,]*)[\.]?\d*"
noncount_pattern = "(개월|달러|달라)"
count_pattern = "(시|명|가지|살|마리|포기|송이|수|톨|통|개|벌|척|채|다발|그루|자루|줄|켤레|그릇|잔|마디|상자|사람|곡|병|판|군데|곳|달)"
quote_pattern = """([`"'＂“‘])(.+?)([`"'＂”’])"""
alphabet_pattern = '[A-Z]+'