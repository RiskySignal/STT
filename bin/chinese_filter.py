# coding=utf-8
import re

__rule__ = re.compile("[^a-zA-Z0-9\u4e00-\u9fa5]")


def validate_label(label):
    __rule__.sub('', label)  # 去除标点符号等，保留中/英文字母和数字
    return label
