import nltk
import argparse


def segment(file_name):
    with open(file_name, 'r') as in_file:
        for line in in_file:
            line_tokened = nltk.word_tokenize(line.decode('utf-8'))
            print u' '.join(line_tokened).encode('utf-8')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='segment english sentence')
    parser.add_argument('f')
    args = parser.parse_args()
    segment(args.f)
