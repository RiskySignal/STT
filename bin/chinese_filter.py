# coding=utf-8
import os

__current_folder__ = os.path.dirname(__file__)
chinses_charas_path = os.path.join(__current_folder__, "../data/chinese_characters.txt")
chinese_charas = [line.strip() for line in open(chinses_charas_path, 'r', encoding='utf-8').readlines()]


def validate_label(label):
    return_label = ""
    for chara in label:
        if chara in chinese_charas:
            return_label += chara
    return return_label
