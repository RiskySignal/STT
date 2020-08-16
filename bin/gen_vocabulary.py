# coding=utf-8
import argparse
import glob
import os
import csv
from chinese_filter import validate_label

PARAMS = None
__current_folder__ = os.path.dirname(__file__)


def get_parser():
    parser = argparse.ArgumentParser(description="Get characters.")
    parser.add_argument('tsv_folder', help="the folder path of the transcription tsv file.")
    parser.add_argument('--output_file', default=os.path.join(__current_folder__, "../data/chinese_vocabulary.txt"), help="the output path.")
    return parser.parse_args()


def gen_vocabulary():
    tsv_files = glob.glob(os.path.join(PARAMS.tsv_folder, "*.tsv"))
    vocabulary_set = set()

    for tsv_file in tsv_files:
        with open(tsv_file, encoding='utf-8') as _file_:
            reader = csv.DictReader(_file_, delimiter="\t")
            for line in reader:
                sentence = validate_label(line['sentence'])

                if sentence is None:
                    continue
                else:
                    sentence = " ".join(sentence)

                vocabulary_set.add(sentence)

    with open(PARAMS.output_file, 'w', encoding='utf-8') as _file_:
        for sentence in vocabulary_set:
            _file_.write(sentence + "\n")

    print("Done!")


if __name__ == '__main__':
    PARAMS = get_parser()
    gen_vocabulary()
