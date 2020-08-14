# coding=utf-8
import argparse
import os
import csv
import glob
from chinese_filter import validate_label

PARAMS = None


def get_parser():
    parser = argparse.ArgumentParser(description="Get characters.")
    parser.add_argument('tsv_folder', help="the folder path of the transcription tsv file.")
    parser.add_argument('--output_file', default="./character.txt", help="the output path, default is './character.txt'.")
    return parser.parse_args()


def main():
    tsv_files = glob.glob(os.path.join(PARAMS.tsv_folder, "*.tsv"))

    pre_chara_sets = set()
    chara_sets = set()
    for csv_file in tsv_files:
        with open(csv_file, encoding='utf-8') as _file_:
            reader = csv.DictReader(_file_, delimiter="\t")
            for line in reader:
                sentence = validate_label(line['sentence'])
                for chara in sentence:
                    chara_sets.add(chara)
                for chara in line['sentence']:
                    pre_chara_sets.add(chara)

    with open(PARAMS.output_file, 'w', encoding='utf-8') as _file_:
        for key in chara_sets:
            _file_.write(key + "\n")

        _file_.write("not in:\n")
        for key in pre_chara_sets:
            if key not in chara_sets:
                _file_.write(key + "\n")

    print("Done!")


if __name__ == '__main__':
    PARAMS = get_parser()
    main()
