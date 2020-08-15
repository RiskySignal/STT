# coding=utf-8
import os
from zhon.hanzi import punctuation as zhong_punc
import string
import opencc

__current_folder__ = os.path.dirname(__file__)
chinses_charas_path = os.path.join(__current_folder__, "../data/chinese_characters.txt")
chinese_charas = [line.strip() for line in open(chinses_charas_path, 'r', encoding='utf-8').readlines()]
__conventer__ = opencc.OpenCC('t2s.json')


def validate_label(label):
    label = __conventer__.convert(label)
    return_label = ""
    for chara in label:
        if chara in chinese_charas:
            return_label += chara
        else:
            if chara in zhong_punc or chara in string.punctuation:
                return_label += ""
            else:
                return None
    return return_label
