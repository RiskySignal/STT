# coding=utf-8
import os
import string

from pypinyin import pinyin, Style
from zhconv import convert
from zhon.hanzi import punctuation as zhong_punc

__current_folder__ = os.path.dirname(__file__)
chinses_charas_path = os.path.join(__current_folder__, "../data/chinese_characters.txt")
chinese_charas = [line.strip() for line in open(chinses_charas_path, 'r', encoding='utf-8').readlines()]
punctuation = zhong_punc + string.punctuation + " ・─"

tmp_set = set()


def validate_label(label):
    return_label = ""
    label = convert(label, "zh-cn")
    for chara in label:
        if chara in chinese_charas:
            return_label += chara
        else:
            if chara in punctuation:
                return_label += ""
            else:
                if pinyin(chara, style=Style.TONE3, heteronym=False)[0][0] == chara:
                    return None
                else:
                    if chara not in tmp_set:
                        print(chara, pinyin(chara, style=Style.TONE3, heteronym=False))
                        tmp_set.add(chara)
                    return None
    return return_label
