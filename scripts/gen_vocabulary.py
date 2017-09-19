import argparse
from collections import Counter


def gen_vocabulary(file_name):
    vocabs = []
    with open(file_name, 'r') as in_file:
        for line in in_file:
            vocabs.extend(line.split())
    c = Counter(vocabs)
    result = sorted(c, key=c.get, reverse=True)
    for _ in result:
        print _


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='segment english sentence')
    parser.add_argument('f')
    args = parser.parse_args()
    gen_vocabulary(args.f)
