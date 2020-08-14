# coding=utf-8
import re


def validate_label(label):
    re.sub('\W+', '', label).replace("_", '')  # 去除标点符号等，保留中/英文字母和数字
    return label
